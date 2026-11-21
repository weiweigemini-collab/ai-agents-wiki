---
url: https://huggingface.co/learn/agents-course/unit1/what-are-agents
title: What is an Agent? (AI Agents Course, Unit 1)
author: Hugging Face
published: 2025 (course page; no exact date on page)
retrieved: 2026-11-15
method: WebFetch 擷取重點（非全文）
---

# What is an Agent? — extracted notes

## Alfred analogy
- Alfred hears "I would like a coffee please" → understands natural language → reasons & plans (go to kitchen, use coffee machine, brew, bring back) → acts using tools he knows (coffee machine) → delivers coffee.

## Formal definition
- An Agent is a system that leverages an AI model to interact with its environment in order to achieve a user-defined objective. It combines reasoning, planning, and execution of actions (often via external tools).
- "Agency" = ability to interact with the environment.

## Two main parts
1. Brain (AI model): reasoning & planning; decides which actions.
2. Body (capabilities & tools): what the agent is equipped to do; actions limited by what it's given (humans can't fly but can walk, run, jump, grab).

## Spectrum of agency (table from smolagents conceptual guide)
| Stars | Level | Meaning |
|---|---|---|
| ☆☆☆ | Simple processor | output has no impact on program flow |
| ★☆☆ | Router | output determines basic control flow |
| ★★☆ | Tool caller | output determines function execution (which function, which args) |
| ★★★ | Multi-step agent | output controls iteration and program continuation |
| ★★★ | Multi-agent | one agentic workflow can start another |
(The page gives the last two the same rating.)

## Models
- Most common: LLM (text in, text out), e.g., GPT-4, Llama, Gemini. Also VLMs (images). Course focuses on LLMs.

## How agents take actions
- LLMs can only generate text. Chat UIs make images because developers added tools (Eiffel Tower made of broccoli via image-generation tool).
- The model generates the tool call; surrounding code executes it.
- Agent can perform any task implemented via Tools. Ex: send_message_to("Manager", ...).
- Tool design is very important. An Action is not the same as a Tool — one action may use several tools.

## Example tasks
- Personal virtual assistants; customer service chatbots; video game NPCs.

## Summary
- Agent uses an AI model (typically LLM) as reasoning core to: understand natural language; reason & plan; interact with environment (gather info, act, observe results).
- Course workflow: Thought → Action → Observation.
