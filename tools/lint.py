#!/usr/bin/env python3
"""Wiki 自動 lint：依 CLAUDE.md 的規則檢查 wiki/。
用法：python3 tools/lint.py        → 有 error 時 exit code = 1
"""
import re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
WIKI, RAW = ROOT / "wiki", ROOT / "raw"
RAW_IDS = {p.name.split("-")[0] for p in RAW.glob("*.md")}       # 00, 01, ...
SPECIAL = {"index", "log"}                                       # 不需 frontmatter
REQ = ["title", "type", "sources", "updated"]
TAG = re.compile(r"〔raw:([0-9]{2})〕")
LINK = re.compile(r"\[\[([a-z0-9-]+)\]\]")

INGEST = "--ingest" in sys.argv
errors, warns = [], []
RAW_TEXT = {p.name.split("-")[0]: p.read_text(encoding="utf-8").lower() for p in RAW.glob("*.md")}
TERM = re.compile(r"[A-Za-z][A-Za-z0-9+\-]{2,}|\d+(?:\.\d+)?%?")
STOP = {"llm", "llms", "agent", "agents", "api", "apis", "raw", "the", "and", "for", "vs"}

def unsupported_terms(line, ids):
    """引用核對：標了〔raw:XX〕的句子裡，英文術語與數字必須真的出現在那些 raw 檔中。"""
    body = TAG.sub("", LINK.sub("", line))
    src = " ".join(RAW_TEXT.get(i, "") for i in ids)
    bad = []
    for t in TERM.findall(body):
        if t.lower() in STOP or (t.isdigit() and len(t) == 1):
            continue
        if t.lower() not in src:
            bad.append(t)
    return bad
pages = {p.stem: p for p in WIKI.rglob("*.md")}
inbound = {s: set() for s in pages}

def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None, text
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    return fm, text[m.end():]

for slug, path in pages.items():
    rel = path.relative_to(ROOT)
    text = path.read_text(encoding="utf-8")
    for target in LINK.findall(text):
        if target not in pages:
            # ingest 進行中，連到「還沒寫的頁」是正常的 → 只警告；最終檢查才算 error
            (warns if INGEST else errors).append(f"{rel}: 連結 [[{target}]] 指向尚未建立的頁")
        elif target != slug and slug != "index":
            inbound[target].add(slug)
    if slug in SPECIAL:
        continue
    fm, body = frontmatter(text)
    if fm is None:
        errors.append(f"{rel}: 缺少 frontmatter"); continue
    for k in REQ:
        if not fm.get(k):
            errors.append(f"{rel}: frontmatter 缺 `{k}`")
    declared = set(re.findall(r"[0-9]{2}", fm.get("sources", "")))
    for d in declared - RAW_IDS:
        errors.append(f"{rel}: sources 指向不存在的 raw `{d}`")
    used = set(TAG.findall(body))
    for u in used - RAW_IDS:
        errors.append(f"{rel}: 內文引用不存在的 raw `{u}`")
    for u in used - declared:
        errors.append(f"{rel}: 內文引用 raw:{u} 但 frontmatter sources 沒列")
    if fm.get("type") in {"concept", "comparison", "analysis"}:
        # 事實段落必須有〔raw:〕標註；「## 相關頁面」段落與表格表頭除外
        section, in_code = "", False
        for i, line in enumerate(body.splitlines(), 1):
            s = line.strip()
            if s.startswith("```"):
                in_code = not in_code; continue
            if in_code or not s:
                continue
            if s.startswith("#"):
                section = s; continue
            if "相關頁面" in section or re.match(r"^\|?[\s:\-|]+\|?$", s):
                continue
            if s.startswith("|") and i < len(body.splitlines()) and \
               re.match(r"^\|?[\s:\-|]+\|?$", body.splitlines()[i].strip() if i < len(body.splitlines()) else ""):
                continue  # 表頭列
            if s.startswith(">"):
                continue  # 引言框：由上下文的事實句負責
            if s.startswith("|"):
                # 表格逐格檢查：每格可以各自標〔raw:〕或〔註解〕，但同一格不能兩者都有
                cells = [c.strip() for c in s.strip("|").split("|")]
                for c in cells:
                    if "〔註解〕" in c and TAG.search(c):
                        errors.append(f"{rel}:{i}: 同一格不能同時標〔註解〕和〔raw:〕")
                if not any(TAG.search(c) or "〔註解〕" in c for c in cells):
                    errors.append(f"{rel}:{i}: 表格列缺〔raw:〕標註 → {s[:40]}…")
                bad = unsupported_terms(s, TAG.findall(s)) if TAG.search(s) else []
                if bad:
                    errors.append(f"{rel}:{i}: 引用核對失敗，raw 中找不到 {bad}")
                continue
            if "〔註解〕" in s:
                if TAG.search(s):
                    errors.append(f"{rel}:{i}: 同一句不能同時標〔註解〕和〔raw:〕")
                continue  # LLM 自己的比喻/說明：允許，但必須明確標示
            if not TAG.search(s):
                errors.append(f"{rel}:{i}: 事實句缺〔raw:〕標註 → {s[:40]}…")
            else:
                bad = unsupported_terms(s, TAG.findall(s))
                if bad:
                    errors.append(f"{rel}:{i}: 引用核對失敗，raw 中找不到 {bad}")
        if not LINK.search(body):
            errors.append(f"{rel}: 沒有任何 [[連結]] 連出去")

# 孤兒頁、index 覆蓋率
index_text = pages["index"].read_text(encoding="utf-8") if "index" in pages else ""
for slug, path in pages.items():
    if slug in SPECIAL:
        continue
    if f"[[{slug}]]" not in index_text:
        errors.append(f"index.md 沒有列出 [[{slug}]]")
    if path.parent.name in {"concepts", "comparisons"} and not inbound[slug]:
        errors.append(f"{path.relative_to(ROOT)}: 孤兒頁（除了 index 沒有任何頁面連到它）")

# 來源差異提醒（人工檢查用）
for slug, path in pages.items():
    if "⚠️ 來源差異" in path.read_text(encoding="utf-8"):
        warns.append(f"{path.relative_to(ROOT)}: 含來源差異段落，請人工確認比較頁已更新")

for e in errors:
    print("ERROR", e)
for w in warns:
    print("WARN ", w)
print(f"\n共 {len(pages)} 頁｜{len(errors)} error｜{len(warns)} warning")
sys.exit(1 if errors else 0)
