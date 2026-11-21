---
url: https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf
title: A practical guide to building agents
author: OpenAI
published: 2025 (PDF, 32 pages; no exact date on page)
retrieved: 2026-11-15
method: WebFetch 擷取 PDF 重點（非全文）
---

# A practical guide to building agents — extracted notes

## What is an agent
- "Agents are systems that independently accomplish tasks on your behalf."
- Workflow = sequence of steps to meet a user's goal (resolve support issue, book reservation, commit code, generate report).
- Core traits: (1) LLM manages workflow execution and decisions — recognizes completion, corrects actions, can halt and transfer control back to user on failure; (2) accesses tools to gather context and take actions, choosing dynamically based on current state, within guardrails.
- NOT agents: apps that use LLM but don't let it control workflow execution — simple chatbots, single-turn LLMs, sentiment classifiers.

## When to build
- Where deterministic/rule-based approaches fall short. Rules engine = checklist; agent = seasoned investigator.
- Criteria: (1) complex decision-making (refund approval), (2) difficult-to-maintain rules (vendor security reviews), (3) heavy reliance on unstructured data (home insurance claims).
- Otherwise a deterministic solution may suffice.

## Design foundations
- Model (reasoning/decisions), Tools (functions/APIs), Instructions (guidelines & guardrails).
- Model selection: prototype with most capable model for baseline; swap smaller models where results hold; set up evals.
- Tool types: Data (retrieve context), Action (change systems), Orchestration (agents as tools).
- Legacy systems without APIs: computer-use models operate UIs.
- Instructions: use existing documents (SOPs, scripts, policies); break down tasks; define clear actions; capture edge cases; can auto-generate instructions with advanced models.

## Orchestration
- Single-agent first. Run loop continues until exit condition: final-output tool invoked; model responds without tool calls; error; max turns.
- Prompt templates with policy variables instead of many prompts.
- Split to multi-agent when: complex logic (many conditionals) or tool overload (similar/overlapping tools, not raw count; some handle 15+ distinct tools, others struggle with <10 overlapping).
- Multi-agent modeled as graphs: agents = nodes; edges = tool calls (manager) or handoffs (decentralized).
  - Manager pattern: central manager delegates to specialized agents via tool calls, keeps control (ex: translate to Spanish/French/Italian).
  - Decentralized pattern: one-way handoffs between peers transferring conversation state (ex: triage agent → order management agent).

## Guardrails
- Layered defense; complement authentication/authorization/access control.
- Types: relevance classifier, safety classifier (jailbreaks/prompt injections), PII filter, moderation, tool safeguards (risk rating low/medium/high by read-only vs write, reversibility, permissions, financial impact), rules-based protections (blocklists, input length limits, regex), output validation.
- Build: start with data privacy & content safety; add as edge cases appear; balance security vs UX.
- Agents SDK: optimistic execution; guardrails run concurrently; tripwire raises exception.

## Human intervention
- Especially early in deployment; helps find failures and edge cases.
- Triggers: exceeding failure thresholds (retries/actions); high-risk actions (cancel orders, large refunds, payments).

## Conclusion
- Strong foundations (capable model, well-defined tools, clear instructions); start with single agent; guardrails at every stage; deploy incrementally.
