---
url: https://www.anthropic.com/news/model-context-protocol
title: Introducing the Model Context Protocol
author: Anthropic
published: 2024-11-25
retrieved: 2026-11-15
method: WebFetch 擷取重點（非全文）
note: 原本想抓 modelcontextprotocol.io 官方文件，但該網址不在本工作區允許清單內，改用官方發表文
---

# Introducing the Model Context Protocol — extracted notes

- Open standard for connecting AI assistants to systems where data lives: content repositories, business tools, development environments. Goal: help frontier models produce better, more relevant responses.
- Problem: models are constrained by isolation from data — trapped behind information silos and legacy systems. Every new data source requires its own custom implementation → hard to scale.
- Solution: "a universal, open standard" replacing fragmented integrations with a single protocol.
- Architecture: developers expose data via **MCP servers**, or build AI applications (**MCP clients**) that connect to these servers. Secure, two-way connections.
- Released: (1) MCP specification and SDKs; (2) local MCP server support in Claude Desktop apps; (3) open-source repository of MCP servers.
- Pre-built servers: Google Drive, Slack, GitHub, Git, Postgres, Puppeteer.
- Early adopters: Block, Apollo; dev tools Zed, Replit, Codeium, Sourcegraph (help agents retrieve context for coding tasks).
- Created by David Soria Parra and Justin Spahr-Summers; developed as collaborative open-source project.
- Vision: AI systems maintain context as they move between tools and datasets.
- (Widely used analogy in docs/secondary sources: "like a USB-C port for AI applications".)
