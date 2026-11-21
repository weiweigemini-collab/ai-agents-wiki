---
title: MCP（Model Context Protocol）
type: concept
sources: [01, 06]
updated: 2026-11-15
---

# MCP：給 agent 用的標準工具接口

## 要解決的問題
- 每接一個新資料源都要寫一套客製整合，系統很難擴大。〔raw:06〕
- MCP 用一個通用、開放的標準取代這些零散的整合。〔raw:06〕
- 常見比喻：像 AI 應用的 USB-C 接口。〔註解〕（這個比喻出自官方文件與二手文章，不是發表文原文；見 raw/06 的備註）

## 架構
| 角色 | 是什麼 |
|---|---|
| MCP server | 把資料或工具透過協定公開出來（例如 GitHub、Slack、Postgres）〔raw:06〕 |
| MCP client | 連接 server 的 AI 應用〔raw:06〕 |

- 連線是安全、雙向的。〔raw:06〕

## 和 agent 的關係
- Anthropic 把 MCP 列為實作 augmented LLM（檢索、工具、記憶）的一種方式。〔raw:01〕 → [[augmented-llm]]
- 願景：AI 在不同工具和資料集之間移動時，能保有脈絡。〔raw:06〕

## 相關頁面
[[tools-and-aci]]、[[augmented-llm]]
