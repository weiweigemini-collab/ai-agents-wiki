---
url: https://www.anthropic.com/engineering/building-effective-agents
title: Building effective agents
author: Erik Schluntz, Barry Zhang (Anthropic)
published: 2024-12-19
retrieved: 2026-11-15
method: WebFetch 擷取重點（非全文）
note: 頁面編者註表示文中部分工具描述自 2024-12 以來已改變
---

# Building effective agents — extracted notes

## Intro
- Worked with dozens of teams building LLM agents. Most successful implementations used simple, composable patterns, not complex frameworks.

## Definitions
- "Agent" has no single definition. Anthropic calls all variants **agentic systems**, with an architectural distinction:
  - **Workflows**: LLMs and tools orchestrated through predefined code paths.
  - **Agents**: LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks.

## When (not) to use agents
- Find the simplest solution; increase complexity only when needed — may mean no agentic system at all.
- Agentic systems trade latency and cost for better task performance.
- Workflows: predictability/consistency for well-defined tasks. Agents: flexibility and model-driven decision-making at scale.
- Often a single LLM call with retrieval and in-context examples is enough.

## Frameworks
- Examples: Claude Agent SDK, Strands Agents SDK (AWS), Rivet, Vellum.
- Abstraction layers can obscure prompts/responses, harder to debug; tempt unnecessary complexity.
- Start with LLM APIs directly; if using a framework, understand underlying code.

## Building block: augmented LLM
- LLM + retrieval + tools + memory. Model generates its own search queries, selects tools, decides what to retain.
- MCP is one way to implement these augmentations.

## Workflow patterns
1. Prompt chaining — sequential steps, each call processes previous output; programmatic "gate" checks between steps. Use when task decomposes into fixed subtasks; trades latency for accuracy. Ex: write outline → check against criteria → write document.
2. Routing — classify input, direct to specialized follow-up. Ex: customer service query types; easy questions to small model, hard to capable model.
3. Parallelization — sectioning (independent subtasks in parallel) or voting (same task multiple times). Ex: guardrail model screens while another answers; multiple prompts review code for vulnerabilities.
4. Orchestrator-workers — central LLM dynamically breaks down tasks, delegates to workers, synthesizes. Subtasks not predefined. Ex: multi-file coding changes; multi-source search.
5. Evaluator-optimizer — one LLM generates, another evaluates and gives feedback, in a loop. Use when clear evaluation criteria and iterative refinement adds measurable value. Ex: literary translation; multi-round search.

## Agents
- Begin with a human command or discussion; plan and operate independently; may return to human for info/judgment.
- At each step obtain "ground truth" from environment (tool results, code execution) to assess progress.
- Can pause at checkpoints/blockers for human feedback; stopping conditions such as max iterations.
- Implementation is often just an LLM using tools based on environmental feedback in a loop → toolset design and documentation crucial.
- Use for open-ended problems where number of steps can't be predicted or hardcoded; requires trust; suits scaling in trusted environments.
- Risks: higher costs, compounding errors → extensive testing in sandboxed environments with guardrails.
- Examples: SWE-bench coding agent; "computer use" reference implementation.

## Three core principles
1. Maintain simplicity in agent design.
2. Prioritize transparency by explicitly showing the agent's planning steps.
3. Carefully craft the agent-computer interface (ACI) through thorough tool documentation and testing.

## Appendix 1: Agents in practice
- Good fit: conversation + action, clear success criteria, feedback loops, meaningful human oversight.
- Customer support: tools for customer data, order history, KB; actions like refunds; success measurable (some charge only for successful resolutions).
- Coding agents: verifiable via automated tests; agents can iterate on test results; SWE-bench Verified from PR description alone; human review still crucial.

## Appendix 2: Prompt engineering your tools
- Tool definitions deserve as much prompt-engineering attention as overall prompts.
- Give model enough tokens to think; keep formats close to natural internet text; avoid formatting overhead (counting lines, escaping).
- ACI: put yourself in model's shoes; include example usage, edge cases, input formats, boundaries; write like a docstring for a junior developer; test many inputs; **poka-yoke** tools.
- SWE-bench anecdote: spent more time optimizing tools than the overall prompt; model erred with relative paths → required absolute paths → used flawlessly.
