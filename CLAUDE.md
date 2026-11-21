# Schema：AI Agents LLM Wiki

這份檔案是 Wiki 的「憲法」（Karpathy LLM Wiki 的第三層 schema）。
人與 LLM 一起維護它；LLM 每次 ingest / query / lint 前都要先讀這份檔案。

## 三層結構
| 層 | 路徑 | 誰寫 | 規則 |
|---|---|---|---|
| Raw sources | `raw/` | 人挑選、工具擷取 | **不可修改**。每份檔頭記錄 URL、取得日期、取得方式 |
| Wiki | `wiki/` | LLM | 人讀、LLM 寫；所有事實句必須能追溯到 raw |
| Schema | `CLAUDE.md` | 人 + LLM | 規則改了要在 `wiki/log.md` 記一筆 |

## 頁面類型與命名
- `wiki/sources/<slug>.md`：一篇 raw 對應一頁來源摘要
- `wiki/concepts/<slug>.md`：概念頁（一個概念一頁）
- `wiki/comparisons/<slug>.md`：跨來源比較、矛盾整理
- `wiki/analyses/<slug>.md`：query 產生、值得保存的答案（回存）
- `wiki/overview.md`：全主題總覽；`wiki/index.md`：目錄；`wiki/log.md`：只能 append 的日誌
- 檔名一律小寫英文、連字號分隔

## 每頁必備 frontmatter
```yaml
---
title: 中文標題
type: source | concept | comparison | analysis | overview
sources: [raw 檔名, ...]      # concept/comparison/analysis 至少 1 個
updated: YYYY-MM-DD
---
```
- 內文的事實句後面用 `〔raw:檔名〕` 標註來源
- LLM 自己加的比喻或說明必須標 `〔註解〕`，**不可**冒用〔raw:〕（2026-11-15 新增，見 log）
- 引用核對：標了〔raw:XX〕的句子中，英文術語與數字必須真的出現在 raw/XX（lint 自動檢查）
- 頁面互連用 `[[slug]]`（不含資料夾），每個概念頁至少連出 1 個、被連入 1 個
- 來源之間說法不一致時，**不要自己選邊**：在頁面加「⚠️ 來源差異」段落，並在 comparisons 建頁

## 操作流程
### Ingest（一次一篇，先討論、後生成）
1. 讀 raw → 2. 在對話中列出 3–5 個重點與人確認 → 3. 寫 source 頁
4. 更新/新增相關 concept 頁 → 5. 更新 index.md → 6. 在 log.md append
7. 跑 `python3 tools/lint.py --ingest`（尚未建立的連結只算 warning），有 error 就修到 0 才算完成
8. 人工引用抽查：隨機挑 3 句，回 raw 確認意思一致（lint 只能核對英文術語與數字，中文的意思要靠人工）
- 全部 ingest 完後跑 `python3 tools/lint.py`（嚴格模式：斷連結也算 error）

### Query
1. 先讀 `index.md` 找頁面 → 2. 讀相關頁 → 3. 合成答案並引用 `[[slug]]`
4. 答案有保存價值就回存到 `wiki/analyses/`

### Lint（自動 + 人工）
自動（tools/lint.py）：frontmatter 完整、sources 指向存在的 raw、`[[連結]]` 不斷、無孤兒頁、index 涵蓋所有頁、每個事實段落有〔raw:〕標註。
人工：矛盾、過時說法、缺少的概念頁。

## 簡報產生規則（Query 的一種輸出）
- 簡報只能用 Wiki 內容，不可直接讀 raw、不可用模型記憶補內容
- 每張投影片標記 `data-wiki="slug,slug"`，由 `tools/check_slides.py` 檢查
- 觀眾：修過 AI 入門課的同學（可用 LLM、prompt、API 等名詞，不必解釋）
