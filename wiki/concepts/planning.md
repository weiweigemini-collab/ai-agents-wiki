---
title: 規劃（Planning）與自我反思
type: concept
sources: [02]
updated: 2026-11-15
---

# 規劃與自我反思

## 任務拆解
- **Chain of Thought**：讓模型「一步一步想」，把難題拆成簡單步驟，同時讓推理過程看得見。〔raw:02〕
- **Tree of Thoughts**：每一步產生多個想法，形成一棵樹，再用 BFS/DFS 搜尋。〔raw:02〕
- 拆解的方式有三種：簡單的 prompt（例如 "Steps for XYZ"）、針對任務的指示、人類輸入。〔raw:02〕
- **LLM+P**：把長期規劃交給外部的傳統規劃器（PDDL），LLM 負責翻譯問題與結果。〔raw:02〕

## 自我反思
- **ReAct**：交錯進行推理和行動，格式是 Thought / Action / Observation → [[agent-loop]]〔raw:02〕
- **Reflexion**：偵測兩種失敗——軌跡很長卻沒成功（規劃沒效率）、連續重複同一動作得到同樣結果（幻覺）；反思內容最多保留 3 條在工作記憶中。〔raw:02〕
- 在 AlfWorld 上，幻覺比規劃沒效率更常見。〔raw:02〕

## 限制
- LLM 遇到意外錯誤時很難調整計畫，不如人類從試錯中學習那麼穩健。〔raw:02〕 → [[agent-challenges]]

## 相關頁面
[[what-is-an-agent]]、[[agent-loop]]
