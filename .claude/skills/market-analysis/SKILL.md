---
name: market-analysis
description: Research a market for Sada (sizing, trends, competitors, SWOT/PESTLE) with web sources and write it into docs/01-market. Use for market research, competitor analysis, or market sizing.
argument-hint: "<category> in <region>"
---

# Market analysis

Input: `$ARGUMENTS` (category and region). Ask for them if missing, then read `docs/00-strategy/vision.md`.

1. **Define the market** (category, geography, segments) in `docs/01-market/market-analysis.md`.
2. **Research with web search.** Prefer industry reports, government statistics, company filings,
   reputable press. Record every source in `sources.md` (title, publisher, URL, access date).
3. **Size it:** TAM/SAM/SOM, top-down *and* bottom-up where possible. Show the arithmetic.
   Anything not directly sourced is labelled `Assumption:`.
4. **Competitors:** identify 5–10. For each, copy `competitors/_template.md` to
   `competitors/<slug>.md` and fill it from their site, pricing pages, and reviews. For more than
   three, spawn `market-analyst` subagents in parallel, one per competitor. Then build
   `competitor-matrix.md` with a positioning map (Mermaid quadrantChart).
5. Write `swot.md` and `pestle.md`.
6. Promote the most decision-relevant findings to `insights.md` as `MI-###` with confidence levels.
7. Finish with a short summary: the 3 biggest opportunities, the 3 biggest risks, and open
   questions that only customer interviews can answer (feed `/user-research`).

Never fabricate figures, quotes, or sources. If data is unavailable, say so.
