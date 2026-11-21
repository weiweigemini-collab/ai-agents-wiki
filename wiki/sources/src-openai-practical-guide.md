---
title: 來源摘要｜OpenAI〈A practical guide to building agents〉
type: source
sources: [04]
updated: 2026-11-15
---

# OpenAI〈A practical guide to building agents〉（2025）

**一句話**：Agent 是「代替你獨立完成任務的系統」，由模型、工具、指令三要素組成；從單一 agent 開始，每一層都要加上 guardrails。〔raw:04〕

## 重點
- 定義與「什麼不是 agent」→ [[what-is-an-agent]]〔raw:04〕
- 何時該用：複雜決策、難以維護的規則、大量非結構化資料 → [[when-to-use-agents]]〔raw:04〕
- 工具三類：Data、Action、Orchestration → [[tools-and-aci]]〔raw:04〕
- Run loop 的結束條件 → [[agent-loop]]〔raw:04〕
- 多代理：manager pattern 與 decentralized（handoff）pattern → [[multi-agent-orchestration]]〔raw:04〕
- Guardrails 分層防護與人類介入的時機 → [[guardrails-and-oversight]]〔raw:04〕
