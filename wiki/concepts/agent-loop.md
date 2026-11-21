---
title: Agent Loop：Thought → Action → Observation
type: concept
sources: [01, 02, 03, 04, 05]
updated: 2026-11-15
---

# Agent Loop

## 核心循環
- ReAct 把推理和行動交錯進行：Thought（想）→ Action（做）→ Observation（看結果），然後重複。〔raw:02〕〔raw:03〕
- Hugging Face 課程也把 agent 的工作流程描述成 Thought → Action → Observation。〔raw:05〕
- Anthropic：agent 的實作常常只是「LLM 根據環境回饋使用工具，然後不斷循環」。〔raw:01〕
- 每一步都要從環境取得「ground truth」（工具結果、程式執行結果）來判斷進度。〔raw:01〕

## 迴圈什麼時候停？（OpenAI 的 run loop 結束條件）
- 呼叫了「最終輸出」工具〔raw:04〕
- 模型回應時沒有呼叫任何工具〔raw:04〕
- 發生錯誤〔raw:04〕
- 達到最大回合數〔raw:04〕
- Anthropic 也建議設停止條件，例如最大迭代次數，並在檢查點或卡住時暫停、請人類回饋。〔raw:01〕

## 為什麼要交錯，而不是先全部想完？
- 只推理容易產生幻覺和錯誤傳遞；接上外部工具取得資訊後，問題就減少了。〔raw:03〕
- 推理軌跡讓人看得懂 agent 在做什麼，比較容易信任和除錯。〔raw:03〕

## 示意
```
Thought: 我需要知道 X 的出生年
Action: search("X")
Observation: X 生於 1990 年……
Thought: 有答案了
Action: finish("1990")
```
> 上面的範例是本 Wiki 為了教學自己寫的，格式依照 ReAct 的 Thought / Action / Observation。

## 相關頁面
[[planning]]、[[tools-and-aci]]、[[what-is-an-agent]]、[[guardrails-and-oversight]]
