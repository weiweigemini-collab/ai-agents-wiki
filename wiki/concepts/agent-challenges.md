---
title: Agent 的挑戰與風險
type: concept
sources: [01, 02]
updated: 2026-11-15
---

# Agent 的挑戰與風險

## Weng 列出的三大挑戰
1. **Context 長度有限**：歷史紀錄、指令、API 說明都要塞進有限的 context。〔raw:02〕
2. **長期規劃困難**：遇到意外錯誤時難以調整計畫。〔raw:02〕
3. **自然語言介面不可靠**：輸出可能格式錯誤或不照指示，所以 agent 程式裡有很多都在處理輸出解析。〔raw:02〕

## Anthropic 提醒的風險
- 成本較高，而且錯誤會一步步累積（compounding errors）。〔raw:01〕
- 建議在沙盒環境中大量測試，並加上適當的 guardrails。〔raw:01〕

## 模型自評不可靠
- ChemCrow 案例：用 LLM 評分時它和 GPT-4 差不多，但化學專家明顯偏好 ChemCrow，代表在專業領域 LLM 不一定能正確評估自己的表現。〔raw:02〕

## 相關頁面
[[guardrails-and-oversight]]、[[planning]]、[[memory]]
