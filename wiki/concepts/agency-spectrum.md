---
title: Agency 光譜：從處理器到多代理
type: concept
sources: [01, 05]
updated: 2026-11-15
---

# Agency 光譜

Agency（能動性）不是有或沒有，而是一個連續的光譜；這張表出自 smolagents 的概念指南。〔raw:05〕

| 等級 | 名稱 | LLM 的輸出決定了什麼 |
|---|---|---|
| ☆☆☆ | Simple processor | 不影響程式流程〔raw:05〕 |
| ★☆☆ | Router | 決定走哪一條基本控制路徑〔raw:05〕 |
| ★★☆ | Tool caller | 決定執行哪個函式、帶什麼參數〔raw:05〕 |
| ★★★ | Multi-step agent | 決定要不要繼續迭代、何時停止〔raw:05〕 |
| ★★★ | Multi-agent | 一個 agentic workflow 可以啟動另一個〔raw:05〕 |

- 原頁面給最後兩級相同的星數。〔raw:05〕
- 判斷方式：看 **LLM 的輸出能控制程式流程到什麼程度**。〔raw:05〕

## ⚠️ 來源差異
- 依照這張表，router 也算一星；但 Anthropic 把 routing 歸類為 workflow，不算 agent。→ [[agent-definitions-compared]]〔raw:01〕〔raw:05〕

## 相關頁面
[[what-is-an-agent]]、[[workflow-vs-agent]]、[[multi-agent-orchestration]]
