---
url: https://arxiv.org/abs/2210.03629
title: "ReAct: Synergizing Reasoning and Acting in Language Models"
author: Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao (Princeton, Google Research)
published: 2022-10-06 (v1); v3 2023-03-10 (ICLR 2023 camera-ready)
retrieved: 2026-11-15
method: WebFetch 擷取 arXiv 摘要頁 + 搜尋結果中的 PDF 引言片段
---

# ReAct — extracted notes

## Core idea
- Reasoning (e.g., chain-of-thought) and acting (e.g., action plan generation) had been studied separately.
- ReAct prompts LLMs to generate reasoning traces and task-specific actions in an **interleaved** manner.
- Reasoning traces help the model induce, track, and update action plans and handle exceptions ("reason to act"); actions let it interface with external sources (knowledge bases, environments) to gather information ("act to reason").
- Human analogy (intro): cooking — reasoning and acting interleave (check ingredients, adjust plan).

## Tasks & results
- HotpotQA (QA) and Fever (fact verification): with a simple Wikipedia API, ReAct overcomes hallucination and error propagation prevalent in chain-of-thought reasoning. Best overall: ReAct combined with CoT (internal + external knowledge).
- ALFWorld & WebShop (interactive decision making): outperforms imitation and reinforcement learning methods by absolute success rate of **34%** and **10%** respectively, prompted with only one or two in-context examples.

## Claimed benefits
- Better performance than baselines; improved human interpretability, trustworthiness, diagnosability.
