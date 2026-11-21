#!/usr/bin/env python3
"""產生可以直接上傳到 GitHub 的資料夾（含 GitHub Pages 網頁）。
用法：python3 tools/build_pages.py <輸出資料夾>
結果：
  <輸出>/index.html          → Wiki 網頁（GitHub Pages 首頁）
  <輸出>/slides/index.html   → 簡報；頁底 Wiki 來源標籤可以點，跳到 ../#slug
  其餘：raw/ wiki/ CLAUDE.md tools/ docs/ slides/outline.md README.md（原樣複製）
"""
import re, sys, shutil, subprocess, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = pathlib.Path(sys.argv[1]).resolve()
if OUT.exists():
    shutil.rmtree(OUT)
OUT.mkdir(parents=True)

for name in ["raw", "wiki", "tools", "docs"]:
    shutil.copytree(ROOT / name, OUT / name, ignore=shutil.ignore_patterns("__pycache__"))
for name in ["CLAUDE.md", "README.md"]:
    shutil.copy(ROOT / name, OUT / name)
(OUT / "slides").mkdir()
shutil.copy(ROOT / "slides" / "outline.md", OUT / "slides" / "outline.md")
(OUT / ".nojekyll").write_text("")   # 讓 GitHub Pages 原樣提供檔案

# Wiki 網頁 → 最外層 index.html
subprocess.run([sys.executable, str(ROOT / "tools" / "build_wiki_site.py"),
                "--slides-link", "slides/", "--out", str(OUT / "index.html")], check=True)

# 簡報：頁底來源標籤變成連結
s = (ROOT / "slides" / "index.html").read_text(encoding="utf-8")
def linkify(m):
    return re.sub(r"<code>([a-z0-9-]+)</code>",
                  r'<a href="../#\1" title="開啟 Wiki 頁：\1"><code>\1</code></a>', m.group(0))
s = re.sub(r'<aside class="src">.*?</aside>', linkify, s, flags=re.S)
s = s.replace(".src code{", ".src a{color:inherit;text-decoration:none}.src a:hover code{background:#C9D1DC}\n.src code{")
(OUT / "slides" / "index.html").write_text(s, encoding="utf-8")
print(f"完成：{OUT}")
