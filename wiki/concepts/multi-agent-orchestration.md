---
title: 多代理編排（Multi-agent Orchestration）
type: concept
sources: [01, 04]
updated: 2026-11-15
---

# 多代理編排

## 先從單一 agent 開始
- OpenAI 建議先用單一 agent，逐步加工具，不要一開始就上複雜架構。〔raw:04〕
- 該拆成多個 agent 的兩個訊號：邏輯太複雜（很多巢狀條件）、工具太多又彼此相似。〔raw:04〕
- 重點是工具「相似、重疊」，不是數量：有的系統能處理 15 個以上不同的工具，有的不到 10 個重疊工具就出錯；先改善工具名稱和描述，真的不行再拆。〔raw:04〕

## 兩種模式（把系統看成 graph：agent 是節點）
| 模式 | 邊（edge）是什麼 | 特色 | 例子 |
|---|---|---|---|
| Manager | 工具呼叫〔raw:04〕 | 中央 manager 分派任務給專門 agent 再彙整，自己保有主控權和與使用者的互動〔raw:04〕 | 翻譯成西、法、義三種語言，各交給一個 agent〔raw:04〕 |
| Decentralized | Handoff（交棒）〔raw:04〕 | 單向轉交控制權和對話狀態，沒有中央彙整〔raw:04〕 | 分流 agent 把訂單問題交給訂單管理 agent〔raw:04〕 |

- Manager pattern 很像 Anthropic 的 orchestrator-workers：中央 LLM 動態拆解任務、分派、彙整。〔raw:01〕〔raw:04〕 → [[workflow-patterns]]

## 相關頁面
[[workflow-patterns]]、[[agency-spectrum]]
