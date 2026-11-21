---
title: 什麼是 AI Agent？
type: concept
sources: [02, 04, 05]
updated: 2026-11-15
---

# 什麼是 AI Agent？

## 三種說法
- **Hugging Face**：利用 AI 模型和環境互動，達成使用者設定目標的系統；結合推理、規劃和行動（常透過外部工具）。〔raw:05〕
- **OpenAI**：「代替你獨立完成任務的系統」；由 LLM 掌控工作流程的執行，並且會使用工具。〔raw:04〕
- **Lilian Weng**：以 LLM 為大腦，搭配規劃、記憶、工具使用三個元件。〔raw:02〕

## 拆解成元件
| 元件 | 角色 |
|---|---|
| 大腦：LLM | 推理、規劃、決定下一步〔raw:02〕〔raw:05〕 |
| 規劃 Planning | 拆解子目標、反思與修正〔raw:02〕 |
| 記憶 Memory | 短期記憶 = context 內的資訊；長期記憶 = 外部向量資料庫〔raw:02〕 |
| 工具 Tools（身體） | 能做什麼，取決於被給了哪些工具〔raw:05〕 |
| 指令 Instructions | 明確的行為準則與 guardrails〔raw:04〕 |

## Alfred 煮咖啡
- 管家 Alfred 聽到「我想要一杯咖啡」→ 理解語言 → 規劃步驟 → 使用咖啡機（工具）→ 送上咖啡。〔raw:05〕

## 什麼「不是」agent
- 沒有讓 LLM 掌控流程的應用，例如簡單的 chatbot、單輪 LLM 呼叫、情緒分類器。〔raw:04〕

## 相關頁面
[[agency-spectrum]]、[[workflow-vs-agent]]、[[agent-loop]]、[[planning]]、[[memory]]、[[tools-and-aci]]、[[agent-definitions-compared]]
