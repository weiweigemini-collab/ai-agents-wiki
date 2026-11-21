---
title: 五種 Workflow 模式
type: concept
sources: [01]
updated: 2026-11-15
---

# 五種 Workflow 模式（Anthropic）

| 模式 | 做法 | 何時用 / 例子 |
|---|---|---|
| Prompt chaining | 拆成固定的連續步驟，每一步處理上一步的輸出，中間可加程式「關卡」檢查〔raw:01〕 | 寫大綱 → 檢查大綱 → 依大綱寫全文〔raw:01〕 |
| Routing | 先分類輸入，再送到專門的後續流程〔raw:01〕 | 客服問題分流；簡單題給小模型、難題給大模型〔raw:01〕 |
| Parallelization | 拆成獨立子任務同時跑（sectioning），或同一任務跑多次再投票（voting）〔raw:01〕 | 一個模型回答、另一個同時做安全審查；多個 prompt 一起找程式漏洞〔raw:01〕 |
| Orchestrator-workers | 中央 LLM 依輸入**動態**拆解任務、分派給 worker、再彙整〔raw:01〕 | 多檔案的程式修改；多來源的資料搜尋〔raw:01〕 |
| Evaluator-optimizer | 一個 LLM 產生內容，另一個評估並給回饋，循環修正〔raw:01〕 | 有明確評估標準時，例如文學翻譯〔raw:01〕 |

- 這些積木不是規定，可以依需求組合，但只有在能證明效果更好時才增加複雜度。〔raw:01〕
- Orchestrator-workers 和 parallelization 的差別：子任務是不是事先定好。〔raw:01〕

## 相關頁面
[[workflow-vs-agent]]、[[multi-agent-orchestration]]、[[augmented-llm]]
