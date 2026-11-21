---
url: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
title: LLM Wiki (idea file)
author: Andrej Karpathy
published: 2026-04-04
retrieved: 2026-11-15
method: WebFetch 擷取重點（非全文；頁面 107,212 字元，擷取涵蓋前 100,000 字元）
role: 方法論來源（說明本 Wiki 的建法），不計入主題資料
---

# LLM Wiki: Outline (extracted notes)

## Core idea
- Standard RAG retrieves raw documents at query time and re-derives answers each time, so nothing accumulates.
- The LLM incrementally builds and maintains a persistent, interlinked markdown wiki between the human and the raw sources. "The wiki is a persistent, compounding artifact."
- Human curates sources and asks questions; the LLM does summarizing, cross-referencing, filing, bookkeeping.

## Three layers
1. Raw sources — curated articles, papers, images, data. LLM reads, never modifies. Source of truth.
2. The wiki — LLM-generated markdown: summaries, entity pages, concept pages, comparisons, overview, synthesis. LLM owns it; human reads it.
3. The schema — e.g. CLAUDE.md / AGENTS.md: structure, conventions, workflows. Co-evolved by human and LLM.

## Operations
- Ingest: add source → LLM reads, discusses takeaways, writes summary page, updates index, revises related entity/concept pages, appends log. One source may touch 10–15 pages. One-at-a-time (supervised) or batch; record choice in schema.
- Query: search wiki, read relevant pages, synthesize cited answer. Output forms: markdown, tables, slide decks (Marp), charts, canvases. File valuable answers back into the wiki.
- Lint: periodic health check — contradictions, stale claims, orphan pages, missing concept pages, missing cross-references, data gaps fillable by web search. Suggest new questions/sources.

## index.md / log.md
- index.md: content-oriented catalog; each page with link + one-line summary (+ optional metadata), grouped by category. Updated every ingest; read first during query. Works at ~100 sources / hundreds of pages without embedding RAG.
- log.md: chronological, append-only record of ingests, queries, lint passes. Consistent prefix (date, operation, title) so unix tools can parse.

## Extras (optional)
Obsidian (graph view, backlinks), YAML frontmatter + Dataview, Marp slides, web clipper, raw/assets/ for images, qmd search, git for history. Intentionally abstract; all components optional.
