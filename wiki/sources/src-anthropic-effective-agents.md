---
title: 來源摘要｜Anthropic〈Building effective agents〉
type: source
sources: [01]
updated: 2026-11-15
---

# Anthropic〈Building effective agents〉（2024-12-19）

**一句話**：做 agent 不用從複雜框架開始，最成功的團隊都是把簡單、可組合的模式拼起來。〔raw:01〕

## 重點
- 把所有變體統稱為 agentic systems，再細分成 **workflow**（預先寫好的程式路徑）和 **agent**（LLM 自己決定流程與工具）。〔raw:01〕 → [[workflow-vs-agent]]
- 基本積木是 **augmented LLM**：LLM 加上檢索、工具、記憶。〔raw:01〕 → [[augmented-llm]]
- 五種 workflow 模式：prompt chaining、routing、parallelization、orchestrator-workers、evaluator-optimizer。〔raw:01〕 → [[workflow-patterns]]
- Agent 的實作常常只是「LLM 根據環境回饋使用工具，然後不斷循環」。〔raw:01〕 → [[agent-loop]]
- 三大原則：保持簡單、讓規劃步驟透明、用心設計 agent-computer interface（ACI）。〔raw:01〕 → [[tools-and-aci]]
- 先找最簡單的解法，必要時才增加複雜度。〔raw:01〕 → [[when-to-use-agents]]

## 時效提醒
- 頁面編者註說文中部分工具描述已經過時，所以本 Wiki 不收錄框架和模型名稱。〔raw:01〕
