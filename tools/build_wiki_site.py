#!/usr/bin/env python3
"""把 wiki/、raw/、CLAUDE.md 轉成一個可瀏覽的單頁 HTML（site/wiki.html）。
用法：python3 tools/build_wiki_site.py
Wiki 改了之後重跑這支程式，再重新發布即可。
"""
import json, re, pathlib, html
import markdown

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "site" / "wiki.html"
md = lambda t: markdown.markdown(t, extensions=["tables", "fenced_code"])

def split_fm(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}, text
    fm = dict(l.split(":", 1) for l in m.group(1).splitlines() if ":" in l)
    return {k.strip(): v.strip() for k, v in fm.items()}, text[m.end():]

def render(body):
    out = md(body)
    out = re.sub(r"\[\[([a-z0-9-]+)\]\]", r'<a class="wl" href="#\1">\1</a>', out)
    out = re.sub(r"〔raw:([0-9]{2})〕", r'<a class="cite" href="#raw-\1" title="原始資料 \1">raw:\1</a>', out)
    out = out.replace("〔註解〕", '<span class="note-tag" title="本 Wiki 自己加的說明，不是來源原文">註解</span>')
    return out

pages, groups = {}, {"總覽": [], "概念": [], "比較": [], "來源摘要": [], "原始資料 raw": [], "規則與紀錄": []}
GROUP_OF = {"concepts": "概念", "comparisons": "比較", "sources": "來源摘要"}

for p in sorted((ROOT / "wiki").rglob("*.md")):
    fm, body = split_fm(p.read_text(encoding="utf-8"))
    slug = p.stem
    title = fm.get("title") or (re.search(r"^# (.+)$", body, re.M) or [None, slug])[1]
    meta = ""
    if fm:
        meta = f'類型：{fm.get("type","")}｜來源：{fm.get("sources","")}｜更新：{fm.get("updated","")}'
    pages[slug] = {"title": title, "meta": meta, "html": render(body), "path": str(p.relative_to(ROOT))}
    g = GROUP_OF.get(p.parent.name)
    if slug in ("index", "overview"):
        g = "總覽"
    elif slug == "log":
        g = "規則與紀錄"
    if g:
        groups[g].append(slug)

for p in sorted((ROOT / "raw").glob("*.md")):
    fm, body = split_fm(p.read_text(encoding="utf-8"))
    rid = "raw-" + p.name.split("-")[0]
    meta = "　".join(f"{k}：{html.escape(v)}" for k, v in fm.items())
    pages[rid] = {"title": f'{p.name.split("-")[0]}｜{fm.get("title","").strip(chr(34))}', "meta": meta,
                  "html": '<p class="raw-note">原始資料（不可修改）。Wiki 頁面裡的 raw 標籤都連到這裡。</p>' + md(body),
                  "path": str(p.relative_to(ROOT))}
    groups["原始資料 raw"].append(rid)

pages["schema"] = {"title": "Schema（CLAUDE.md）", "meta": "Wiki 的規則：三層結構、頁面格式、ingest / query / lint 流程",
                   "html": md((ROOT / "CLAUDE.md").read_text(encoding="utf-8")), "path": "CLAUDE.md"}
groups["規則與紀錄"].insert(0, "schema")
groups["總覽"].sort(key=lambda s: s != "index")

n_concept = len(groups["概念"]); n_src = len(groups["來源摘要"]); n_raw = len(groups["原始資料 raw"])
intro = f"""
<div class="intro">
<p><b>主題：AI Agents</b>。依照 Karpathy 的 LLM Wiki 架構建立：原始資料（raw）由人挑選、不可修改；
Wiki 頁面由 LLM 撰寫與維護；schema 規定格式與流程。</p>
<p>內容：{n_raw} 份原始資料（1 份方法論＋{n_src} 篇主題資料）、{n_src} 頁來源摘要、{n_concept} 頁概念、
{len(groups["比較"])} 頁比較。每一句事實都標有 <a class="cite" href="#raw-01">raw:XX</a>，點下去可以看原始資料；
LLM 自己加的比喻標為 <span class="note-tag">註解</span>。</p>
</div>"""
pages["index"]["html"] = intro + pages["index"]["html"]

import sys
TEMPLATE = (ROOT / "tools" / "wiki_template.html").read_text(encoding="utf-8")
# --slides-link URL：在左側欄加上「教學簡報」連結（GitHub Pages 版用）
if "--slides-link" in sys.argv:
    url = sys.argv[sys.argv.index("--slides-link") + 1]
    TEMPLATE = TEMPLATE.replace('<input id="q"',
        f'<a class="slides-link" href="{url}">開啟教學簡報</a>\n  <input id="q"')
if "--out" in sys.argv:
    OUT = pathlib.Path(sys.argv[sys.argv.index("--out") + 1]).resolve()
out = TEMPLATE.replace("/*PAGES*/null", json.dumps(pages, ensure_ascii=False)) \
              .replace("/*GROUPS*/null", json.dumps(groups, ensure_ascii=False))
OUT.parent.mkdir(exist_ok=True)
OUT.write_text(out, encoding="utf-8")
print(f"寫入 {OUT}：{len(pages)} 頁")
