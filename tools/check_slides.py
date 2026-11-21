#!/usr/bin/env python3
"""簡報檢查：大綱（slides/outline.md）和成品（slides/index.html）都用同一套規則。
用法：python3 tools/check_slides.py slides/outline.md
      python3 tools/check_slides.py slides/index.html
規則：
  1. 張數 12–15
  2. 每張都要宣告引用的 wiki 頁，而且頁面存在
  3. 投影片上的數字與英文術語，必須出現在它引用的 wiki 頁中（不能用模型記憶補）
"""
import re, sys, pathlib, html

ROOT = pathlib.Path(__file__).resolve().parent.parent
WIKI = {p.stem: p.read_text(encoding="utf-8").lower() for p in (ROOT / "wiki").rglob("*.md")}
TERM = re.compile(r"[A-Za-z][A-Za-z0-9+\-]{2,}|\d+(?:\.\d+)?%?")
# 版面用字、通用字，不需要追溯
STOP = {"llm", "llms", "agent", "agents", "agentic", "api", "apis", "ai", "the", "and", "for",
        "vs", "wiki", "html", "slide", "slides", "next", "prev", "page", "quiz"}

def parse(path):
    text = path.read_text(encoding="utf-8")
    if path.suffix == ".md":
        for m in re.finditer(r"^## (S\d+.*?)\n(.*?)(?=^## S\d+|\Z)", text, re.S | re.M):
            body = m.group(2)
            w = re.search(r"^wiki:\s*(.+)$", body, re.M)
            slugs = [s.strip() for s in w.group(1).split(",")] if w else []
            body = re.sub(r"^wiki:.*$", "", body, flags=re.M)
            body = re.sub(r"^note:.*$", "", body, flags=re.M)   # 講者備註不上投影片
            yield m.group(1).strip(), slugs, body
    else:
        text = re.sub(r"<script.*?</script>|<style.*?</style>", "", text, flags=re.S)
        for m in re.finditer(r'<section[^>]*class="slide[^"]*"[^>]*>(.*?)</section>', text, re.S):
            tag = m.group(0)[: m.group(0).find(">") + 1]
            w = re.search(r'data-wiki="([^"]*)"', tag)
            slugs = [s.strip() for s in w.group(1).split(",") if s.strip()] if w else []
            inner = re.sub(r'<aside class="src".*?</aside>', "", m.group(1), flags=re.S)  # 來源列本身不檢查
            body = html.unescape(re.sub(r"<[^>]+>", " ", inner))
            title = re.search(r"<h[12][^>]*>(.*?)</h[12]>", m.group(1), re.S)
            yield (re.sub(r"<[^>]+>", "", title.group(1)).strip() if title else "(無標題)"), slugs, body

path = pathlib.Path(sys.argv[1])
slides = list(parse(path))
errors = []
if not 12 <= len(slides) <= 15:
    errors.append(f"張數 {len(slides)}，不在 12–15 之間")
for n, (title, slugs, body) in enumerate(slides, 1):
    if not slugs:
        errors.append(f"#{n}「{title}」沒有宣告引用的 wiki 頁"); continue
    missing = [s for s in slugs if s not in WIKI]
    if missing:
        errors.append(f"#{n}「{title}」引用了不存在的 wiki 頁 {missing}"); continue
    src = " ".join(WIKI[s] for s in slugs)
    bad = sorted({t for t in TERM.findall(body)
                  if t.lower() not in STOP and not (t.isdigit() and len(t) == 1) and t.lower() not in src})
    if bad:
        errors.append(f"#{n}「{title}」有內容在引用的 wiki 頁裡找不到：{bad}")

for e in errors:
    print("ERROR", e)
print(f"\n{path.name}：{len(slides)} 張｜{len(errors)} error")
sys.exit(1 if errors else 0)
