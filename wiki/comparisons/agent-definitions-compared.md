---
title: 比較｜三個來源怎麼定義 agent
type: comparison
sources: [01, 04, 05]
updated: 2026-11-15
---

# 「Agent」的定義比較

| | Anthropic | OpenAI | Hugging Face |
|---|---|---|---|
| 核心判準 | LLM 動態決定自己的流程與工具〔raw:01〕 | LLM 掌控工作流程的執行，並使用工具〔raw:04〕 | 用 AI 模型和環境互動以達成目標〔raw:05〕 |
| 有預設流程的系統 | 叫 workflow，不算 agent〔raw:01〕 | 沒讓 LLM 控制流程就不是 agent〔raw:04〕 | 屬於光譜的低階（router ★☆☆）〔raw:05〕 |
| 定義形式 | 二分法（workflow / agent）〔raw:01〕 | 二分法（是 / 不是）〔raw:04〕 | 連續光譜〔raw:05〕 |

## 共識
- 三者都同意：關鍵在於 **LLM 對流程的控制程度**，以及**能不能透過工具和環境互動**。〔raw:01〕〔raw:04〕〔raw:05〕

## 差異
- 「routing 算不算 agent」三方說法不同：Anthropic 歸為 workflow，HF 給一顆星。〔raw:01〕〔raw:05〕
- 本 Wiki 不替來源選邊；教學時建議用「光譜」的角度呈現，再說明 Anthropic 的界線畫在哪裡。〔註解〕

## 相關頁面
[[what-is-an-agent]]、[[workflow-vs-agent]]、[[agency-spectrum]]、[[source-discrepancies]]
