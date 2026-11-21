---
title: 記憶（Memory）
type: concept
sources: [02]
updated: 2026-11-15
---

# Agent 的記憶

| 人類記憶 | Agent 的對應 |
|---|---|
| 感官記憶（幾秒） | 原始輸入的 embedding 表示〔raw:02〕 |
| 短期／工作記憶（約 7 項、20–30 秒） | in-context learning，受 context window 長度限制〔raw:02〕 |
| 長期記憶（情節、語意、程序性） | 外部向量資料庫，需要時再檢索〔raw:02〕 |

- 長期記憶通常存成 embedding，再用最大內積搜尋（MIPS）的近似最近鄰演算法快速查找，例如 LSH、HNSW、FAISS、ScaNN。〔raw:02〕
- Generative Agents 的記憶流：用「新近程度、重要性、相關性」三個分數來檢索記憶。〔raw:02〕

## 相關頁面
[[what-is-an-agent]]、[[augmented-llm]]、[[agent-challenges]]
