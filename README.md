# AI Agents LLM Wiki ＋ 教學 HTML 簡報

生成式 AI 作業：先建立「AI Agents」主題的 LLM Wiki，再用這個 Wiki 當作唯一的知識來源，製作一份教學型 HTML 簡報。

- **Wiki 網頁**：https://<你的帳號>.github.io/ai-agents-wiki/
- **教學簡報**：https://<你的帳號>.github.io/ai-agents-wiki/slides/

> 把 `<你的帳號>` 換成你的 GitHub 帳號；如果 repo 不叫 `ai-agents-wiki`，網址的最後一段也要跟著改。

---

## 繳交項目對照

| # | 繳交項目 | 在哪裡 |
|---|---|---|
| 1 | LLM Wiki 主題與簡短介紹 | 本頁開頭；Wiki 網頁首頁 |
| 2 | LLM Wiki 連結或成果 | Wiki 網頁；原始檔在 [`wiki/`](wiki/)、[`raw/`](raw/)、[`CLAUDE.md`](CLAUDE.md) |
| 3 | 教學 HTML 簡報連結 | 簡報網頁；原始檔 [`slides/index.html`](slides/index.html) |
| 4 | loop / graph 流程圖或說明 | [`docs/workflow-and-reflection.md`](docs/workflow-and-reflection.md) 第一～四節 |
| 5 | 一次實際執行的結果或檢查紀錄 | [`wiki/log.md`](wiki/log.md)（每次 ingest、lint、簡報檢查的實際結果） |
| 6 | 反思 | [`docs/workflow-and-reflection.md`](docs/workflow-and-reflection.md) 第五節 |

## Wiki 與簡報怎麼對應

- Wiki 的每一句事實都標有 `〔raw:XX〕`，指向 `raw/` 裡的原始資料；LLM 自己加的比喻標為 `〔註解〕`。
- 簡報的每一張都用 `data-wiki="..."` 宣告用了哪些 Wiki 頁；頁底的來源標籤可以點，會直接跳到那一頁 Wiki。
- `tools/check_slides.py` 會檢查：投影片上的數字和英文術語，一定要出現在它引用的 Wiki 頁裡。

## 資料夾結構

```
├── index.html                 # Wiki 網頁（由 wiki/ 自動產生）
├── slides/
│   ├── index.html             # 教學 HTML 簡報（14 張）
│   └── outline.md             # 簡報大綱
├── CLAUDE.md                  # Schema：Wiki 的規則
├── raw/                       # 7 份原始資料（不可修改）
├── wiki/
│   ├── index.md / overview.md / log.md
│   ├── sources/               # 6 頁來源摘要
│   ├── concepts/              # 14 頁概念
│   └── comparisons/           # 2 頁比較
├── tools/
│   ├── lint.py                # Wiki 檢查（格式、連結、引用核對）
│   ├── check_slides.py        # 簡報檢查（大綱和 HTML 共用）
│   ├── build_wiki_site.py     # wiki/ → Wiki 網頁
│   └── build_pages.py         # 產生這個 GitHub 版本
└── docs/
    └── workflow-and-reflection.md
```

## 流程摘要

```
討論 → 取得資料 → 討論重點 → [ Ingest 一篇 → Lint → 人工抽查 ] × 6 → 嚴格 Lint
     → Query Wiki → 大綱 → 檢查大綱 → 產生 HTML → 檢查 HTML → 截圖檢查
```

詳細流程圖、重複與檢查節點、設計理由和反思，請見 [`docs/workflow-and-reflection.md`](docs/workflow-and-reflection.md)。

## 自己重跑檢查

需要 Python 3（產生 Wiki 網頁另需 `pip install markdown`）：

```bash
python3 tools/lint.py                          # Wiki：0 error 才算通過
python3 tools/check_slides.py slides/outline.md
python3 tools/check_slides.py slides/index.html
```

## 資料來源

| raw | 來源 |
|---|---|
| 00 | Andrej Karpathy, *LLM Wiki*（方法論） |
| 01 | Anthropic, *Building effective agents* |
| 02 | Lilian Weng, *LLM Powered Autonomous Agents* |
| 03 | Yao et al., *ReAct: Synergizing Reasoning and Acting in Language Models* |
| 04 | OpenAI, *A practical guide to building agents* |
| 05 | Hugging Face Agents Course, *What is an Agent?* |
| 06 | Anthropic, *Introducing the Model Context Protocol* |

`raw/` 是用網頁擷取工具整理的重點筆記，不是全文；每份檔頭都有原始網址與取得日期。
