---
title: Workflow vs Agent
type: concept
sources: [01]
updated: 2026-11-15
---

# Workflow vs Agent

## 定義
- **Workflow**：LLM 和工具依照**預先寫好的程式路徑**來編排。〔raw:01〕
- **Agent**：LLM **自己動態決定**流程和要用哪些工具，掌控任務怎麼完成。〔raw:01〕
- Anthropic 把兩者統稱為 agentic systems，差別在「流程由誰決定」。〔raw:01〕

## 怎麼選
| | Workflow | Agent |
|---|---|---|
| 適合 | 定義清楚、需要可預測和一致性的任務〔raw:01〕 | 需要彈性、由模型做決策的情境〔raw:01〕 |
| 代價 | 比較不彈性〔raw:01〕 | 延遲、成本較高，錯誤可能累積〔raw:01〕 |

## 一個好記的說法
- 誰在開車？Workflow 是工程師事先畫好路線，agent 是 LLM 邊開邊決定下一個路口。〔註解〕（這是本 Wiki 自己加的比喻，不是來源原文）

## 相關頁面
[[what-is-an-agent]]、[[agency-spectrum]]、[[workflow-patterns]]、[[when-to-use-agents]]、[[agent-definitions-compared]]
