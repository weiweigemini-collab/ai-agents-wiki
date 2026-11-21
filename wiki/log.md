# Log（只能 append）

## [2026-11-15] schema | 建立 CLAUDE.md
- 與使用者討論後決定：主題 AI Agents、觀眾為修過 AI 入門課的同學、由 LLM 搜尋挑選資料

## [2026-11-15] fetch | 取得 7 份 raw
- 00 Karpathy gist（方法論）、01–06 主題資料
- 問題：modelcontextprotocol.io 不在允許清單內 → 改抓 Anthropic 官方 MCP 發表文（raw/06）
- 問題：Karpathy gist 擷取只涵蓋前 100,000 / 107,212 字元 → 檔頭已註明

## [2026-11-15] discuss | 6 篇重點與概念頁結構，經使用者確認後才開始生成

## [2026-11-15] ingest | 01 Anthropic Building effective agents
- 新增：src-anthropic-effective-agents、workflow-vs-agent、augmented-llm、workflow-patterns、when-to-use-agents、tools-and-aci
- lint #1：11 error，全部是「連到尚未建立的頁」→ ingest 途中這是正常的，lint 改成 `--ingest` 模式時只算 warning
- 新增「引用核對」：標了〔raw:XX〕的句子中，英文術語與數字必須真的出現在 raw/XX
- 人工抽查發現：workflow-vs-agent 的「誰在開車」比喻是 LLM 自己寫的，卻標成〔raw:01〕→ 新增〔註解〕標籤，並寫進 schema
- 人工抽查發現：when-to-use-agents、tools-and-aci 在 ingest 01 時就引用了 02/04/05（因為 raw 檔已經存在，LLM 提前讀了）→ 內容正確，但違反「一次一篇」；後續 ingest 時再複核這兩頁

## [2026-11-15] ingest | 02 Weng LLM Powered Autonomous Agents
- 新增：src-weng-autonomous-agents、what-is-an-agent、planning、memory、agent-challenges
- 發現來源差異：ReAct 年份（Weng 寫 2023、arXiv 初版 2022）→ 待建 source-discrepancies
- lint #2：3 error
  - memory.md 寫了「表達力不如 attention」，但 raw/02 裡沒有這句（WebFetch 原始輸出有，存成 raw 時被我精簡掉了）→ raw 不可改，所以刪掉 wiki 這句
  - agent-challenges.md 的「demo」不在 raw 中 → 改寫成 raw 有的說法
  - src-weng 的 frontmatter 漏列 03 → 補上
- 心得：錯誤源頭在「取得資料 → 存 raw」這一步太早精簡；之後的 raw 盡量保留原句

## [2026-11-15] ingest | 03 ReAct 論文
- 新增：src-react-paper、agent-loop（同時整合 01/02/04/05 的說法）

## [2026-11-15] ingest | 04 OpenAI practical guide
- 新增：src-openai-practical-guide、multi-agent-orchestration、guardrails-and-oversight
- 複核：when-to-use-agents、tools-and-aci 先前提早引用的 04 內容，逐句和 raw/04 對照後都一致
- lint #3：1 error——「SQL injection」不在 raw/04 裡（又是存 raw 時精簡掉的）→ 刪除。這是同類錯誤第二次出現

## [2026-11-15] ingest | 05 Hugging Face What is an Agent
- 新增：src-hf-what-is-an-agent、agency-spectrum；建立 agent-definitions-compared

## [2026-11-15] ingest | 06 Anthropic MCP
- 新增：src-anthropic-mcp、mcp；建立 source-discrepancies、overview
- lint #4（嚴格模式）：3 error
  - 表格列同時有〔raw:〕和〔註解〕被誤判 → lint 改成逐格檢查（工具本身的 bug）
  - agency-spectrum 的 frontmatter 漏列 01 → 補上
  - 人工抽查：mcp 的「USB-C」比喻其實不在發表文原文 → 改標〔註解〕
- lint #5：0 error、2 warning（兩個來源差異段落都已收進 comparisons，經人工確認）
- Wiki 完成：6 篇來源摘要、14 個概念頁、2 個比較頁、overview、index、log

## [2026-11-15] query | 為簡報產生大綱
- 依 CLAUDE.md：先讀 index → overview 的閱讀順序 → 各概念頁
- 大綱 slides/outline.md：check_slides 0 error（14 張）
- HTML 第一版：check_slides 1 error——第 5 張寫了「CoT」，但引用的 planning 頁只有「Chain of Thought」→ 產生 HTML 時模型自己縮寫了，改回 Wiki 的寫法
- HTML 第二版：0 error
- 視覺檢查（headless Chrome 逐張截圖）：
  - 互動 bug：在第 6 張按過「下一步」後，焦點留在按鈕上，方向鍵翻頁失效 → 修正鍵盤事件
  - 第 9–13 張下方空白太多 → 放大字級；14 張都沒有溢出、沒有 JS 錯誤

## [2026-11-15] docs | 撰寫 docs/workflow-and-reflection.md（loop/graph 設計與反思，依本 log 撰寫）

## [2026-11-21] publish | 建立可瀏覽的 Wiki 網頁
- tools/build_wiki_site.py：把 wiki/、raw/、CLAUDE.md 轉成單頁 HTML（site/wiki.html），檢查 33 頁之間沒有斷連結

## [2026-11-21] publish | 準備 GitHub Pages 版本
- tools/build_pages.py：產生 docs-ready 資料夾，最外層 index.html = Wiki，slides/index.html = 簡報；簡報頁底的 Wiki 來源標籤改成可以點，直接跳到對應的 Wiki 頁
