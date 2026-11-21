# Index｜AI Agents LLM Wiki

> Query 時先讀這頁。每頁一行摘要。

## 來源摘要（sources/）
- [[src-anthropic-effective-agents]]：workflow vs agent、五種模式、三大原則
- [[src-weng-autonomous-agents]]：LLM 大腦 + 規劃 / 記憶 / 工具；三大挑戰
- [[src-react-paper]]：Thought/Action/Observation；ALFWorld +34%、WebShop +10%
- [[src-openai-practical-guide]]：模型 / 工具 / 指令；run loop；manager 與 handoff；guardrails
- [[src-hf-what-is-an-agent]]：Alfred 比喻、大腦／身體、agency 光譜
- [[src-anthropic-mcp]]：MCP 發表文：client/server、預建 server

## 總覽
- [[overview]]：一句話定義、閱讀順序、跨來源的共同結論

## 比較（comparisons/）
- [[agent-definitions-compared]]：Anthropic / OpenAI / HF 的定義對照
- [[source-discrepancies]]：來源差異與時效紀錄

## 概念（concepts/）
- [[workflow-vs-agent]]：流程是預先寫好的，還是由 LLM 自己決定
- [[augmented-llm]]：LLM + 檢索 + 工具 + 記憶的基本積木
- [[workflow-patterns]]：chaining / routing / parallel / orchestrator / evaluator
- [[when-to-use-agents]]：先求簡單；OpenAI 的三個判斷條件
- [[tools-and-aci]]：工具類型、ACI、防呆設計
- [[what-is-an-agent]]：三個來源的定義、元件拆解、Alfred 比喻
- [[planning]]：CoT、ToT、LLM+P、ReAct、Reflexion
- [[memory]]：人類記憶的對照、向量檢索
- [[agent-challenges]]：context 有限、長期規劃、介面不可靠、錯誤累積
- [[agent-loop]]：Thought → Action → Observation 與停止條件
- [[multi-agent-orchestration]]：先單一 agent；manager vs decentralized
- [[guardrails-and-oversight]]：七種 guardrail、何時交給人類
- [[agency-spectrum]]：☆☆☆ 到 ★★★ 的五個等級
- [[mcp]]：標準化的工具與資料接口
