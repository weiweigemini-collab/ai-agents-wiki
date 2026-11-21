---
title: 工具與 ACI（Agent-Computer Interface）
type: concept
sources: [01, 02, 04, 05]
updated: 2026-11-15
---

# 工具與 ACI

## 為什麼需要工具
- LLM 本身只能產生文字；聊天介面能做出圖片，是因為開發者加了工具讓模型呼叫。〔raw:05〕
- 模型負責產生「工具呼叫」，周圍的程式負責真正執行。〔raw:05〕
- 工具讓 agent 取得模型權重裡沒有的資訊，例如即時資料、程式執行、私有資料。〔raw:02〕

## 工具的三種類型（OpenAI）
- **Data**：取得脈絡，例如查資料庫、讀 PDF、網路搜尋。〔raw:04〕
- **Action**：改變外部系統，例如寄信、更新紀錄。〔raw:04〕
- **Orchestration**：把其他 agent 當成工具來用。〔raw:04〕

## ACI：替模型設計介面
- 工具定義值得投入和主 prompt 一樣多的 prompt engineering。〔raw:01〕
- 站在模型的角度想：只看描述和參數，能不能一看就懂怎麼用？要附範例、邊界情況、輸入格式。〔raw:01〕
- **Poka-yoke（防呆）**：修改參數設計，讓模型比較難犯錯。〔raw:01〕
- 實例：模型離開根目錄後常用錯相對路徑，改成強制使用絕對路徑後就不再出錯。〔raw:01〕
- 工具的關鍵不只是「有」，還要知道何時、如何使用（MRKL 的教訓）。〔raw:02〕
- 一個 action 不等於一個 tool，一個 action 可能會用到好幾個工具。〔raw:05〕

## 相關頁面
[[augmented-llm]]、[[mcp]]、[[agent-loop]]、[[guardrails-and-oversight]]
