---
name: project-status
description: Report where the EVI project stands across all phases (strategy, market, business, brand, products, system analysis, UX, build, deploy, launch) and recommend the next steps. Use when asked for status, progress, "what's next", or a weekly report.
---

# Project status

1. Read `WORKFLOW.md` for the phases and their gates.
2. For each phase, inspect its folders: list documents and their front-matter `status`
   (`draft`/`review`/`approved`), count IDs (`MI`, `PER`, `BR`, `FR`, `US`, `SCR`, `PRD`, `ADR`), and
   flag empty templates.
3. Check traceability gaps: BRs without an MI/PER link, FRs without a BR, stories without an FR,
   products failing `python3 scripts/validate_catalog.py`.
4. If GitHub tools are available, include open issues and PRs grouped by `phase:` label.
5. Output a table: phase | gate met? | done | in progress | missing. Then list the top 3
   next actions, each with the skill to run.
