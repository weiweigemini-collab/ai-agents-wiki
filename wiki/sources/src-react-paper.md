---
title: 來源摘要｜ReAct 論文（Yao et al.）
type: source
sources: [03]
updated: 2026-11-15
---

# ReAct: Synergizing Reasoning and Acting in Language Models

**一句話**：讓 LLM 把「推理」和「行動」交錯進行，比只推理或只行動都好。〔raw:03〕

## 重點
- 以前推理（如 chain-of-thought）和行動（如產生動作計畫）是分開研究的。〔raw:03〕
- 推理幫模型建立、追蹤、更新計畫；行動讓模型從外部取得資訊。〔raw:03〕 → [[agent-loop]]
- HotpotQA、Fever：接上簡單的 Wikipedia API，就能減少 CoT 的幻覺與錯誤傳遞。〔raw:03〕
- ALFWorld、WebShop：絕對成功率比模仿學習和強化學習方法分別高 34% 和 10%，而且只用了 1–2 個 in-context 範例。〔raw:03〕
- 額外好處：人類比較看得懂它的推理過程，也比較容易信任和除錯。〔raw:03〕

## 書目資訊
- arXiv v1：2022-10-06；v3：2023-03-10（ICLR 2023 定稿）〔raw:03〕 → [[source-discrepancies]]
