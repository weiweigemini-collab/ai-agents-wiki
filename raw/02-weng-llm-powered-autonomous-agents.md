---
url: https://lilianweng.github.io/posts/2023-06-23-agent/
title: LLM Powered Autonomous Agents
author: Lilian Weng (Lil'Log)
published: 2023-06-23
retrieved: 2026-11-15
method: WebFetch 擷取重點（非全文）
---

# LLM Powered Autonomous Agents — extracted notes

## 1. Overview
- LLM functions as the agent's brain, complemented by: **Planning**, **Memory**, **Tool use**.
- Planning: subgoal decomposition; reflection and refinement of past actions.
- Memory: short-term = in-context learning; long-term = external vector store + fast retrieval.
- Tool use: call external APIs for info missing from weights (current info, code execution, proprietary sources).

## 2. Task decomposition
- Chain of Thought (Wei et al. 2022): "think step by step"; more test-time computation; interpretable.
- Tree of Thoughts (Yao et al. 2023): multiple thoughts per step → tree; BFS/DFS; states evaluated by classifier prompt or majority vote.
- Decomposition by (1) simple prompting ("Steps for XYZ.\n1."), (2) task-specific instructions, (3) human inputs.
- LLM+P (Liu et al. 2023): external classical planner via PDDL; LLM translates problem → planner → translate back.

## 3. Self-reflection
- ReAct (Yao et al. 2023): reasoning + acting; action space = task actions + language. Template: Thought / Action / Observation, repeated. Outperforms Act-only baseline.
- Reflexion (Shinn & Labash 2023): dynamic memory + self-reflection; binary reward; heuristic detects inefficient planning (long trajectory w/o success) and hallucination (consecutive identical actions → same observation); reflections from two-shot examples, up to three kept in working memory. On AlfWorld, hallucination more common than inefficient planning.
- Chain of Hindsight (Liu et al. 2023): fine-tune on sequences of past outputs annotated with feedback.
- Algorithm Distillation (Laskin et al. 2023): cross-episode histories in RL.

## 4. Memory (mapping to human memory)
- Sensory memory → embedding representations of raw inputs.
- Short-term / working memory (~7 items, 20–30 s) → in-context learning, limited by context window.
- Long-term memory (explicit: episodic, semantic; implicit: procedural) → external vector store.
- MIPS with ANN algorithms: LSH, ANNOY, HNSW, FAISS, ScaNN.

## 5. Tool use
- MRKL (Karpas et al. 2022): LLM routes to expert modules (calculator, weather API). Lesson: knowing when/how to use tools is crucial.
- TALM, Toolformer: fine-tune LM to use tool APIs.
- ChatGPT Plugins, OpenAI function calling as practical examples.
- HuggingGPT: ChatGPT as task planner → model selection → task execution → response generation.
- API-Bank: 53 tools, 264 dialogues, 568 API calls; 3 levels: call API, retrieve API, plan API.

## 6. Case studies
- ChemCrow: 13 expert tools, ReAct format; LLM-based eval rated it ≈ GPT-4, but human experts strongly favored ChemCrow → LLMs may not judge own performance well in expert domains.
- Boiko et al. 2023: scientific discovery agent; risk test.
- Generative Agents (Park et al. 2023): 25 characters in a sandbox; memory stream, retrieval (recency, importance, relevance), reflection, planning & reacting; emergent social behavior.
- AutoGPT: autonomous agent; reliability issues; much code is format parsing.
- GPT-Engineer: generates code repo from task; asks clarifying questions first.

## 7. Challenges
- Finite context length.
- Long-term planning and task decomposition; hard to adjust plans after unexpected errors.
- Reliability of natural language interface: formatting errors, rebellious behavior → much code parses output.
