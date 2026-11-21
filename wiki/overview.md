---
title: 總覽｜AI Agents
type: overview
sources: [01, 02, 03, 04, 05, 06]
updated: 2026-11-15
---

# AI Agents 總覽

一句話：**AI Agent 是讓 LLM 在迴圈裡自己決定下一步、透過工具和環境互動，直到完成任務的系統。**〔註解〕（綜合 [[what-is-an-agent]] 的三個定義）

## 建議閱讀順序（也就是簡報的骨架）
1. 是什麼 → [[what-is-an-agent]]、[[agency-spectrum]]、[[agent-definitions-compared]]
2. 由什麼組成 → [[augmented-llm]]、[[planning]]、[[memory]]、[[tools-and-aci]]
3. 怎麼運作 → [[agent-loop]]
4. 怎麼搭 → [[workflow-vs-agent]]、[[workflow-patterns]]、[[multi-agent-orchestration]]、[[mcp]]
5. 何時用、要注意什麼 → [[when-to-use-agents]]、[[agent-challenges]]、[[guardrails-and-oversight]]

## 跨來源的三個共同結論
- 從簡單開始，有需要才增加複雜度。〔raw:01〕〔raw:04〕
- 工具（和工具說明）的品質決定 agent 的品質。〔raw:01〕〔raw:05〕
- 要有停止條件、guardrails 和人類介入點。〔raw:01〕〔raw:04〕
