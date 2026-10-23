---
name: adr
description: Record an architecture, technology, or significant business decision for Sada as an ADR in docs/04-system-analysis/adr.
argument-hint: "<decision to make>"
---

# Architecture Decision Record

1. Next number: `ls docs/04-system-analysis/adr | sort | tail -1`.
2. Copy `templates/system/adr.md` to `docs/04-system-analysis/adr/NNNN-<slug>.md`.
3. Fill context (link FR/NFR/BR), at least 2 real options with pros and cons, the recommendation, and consequences.
4. Leave `status: proposed` unless the user explicitly accepts it. If it supersedes an earlier ADR,
   update that ADR's status to `superseded by ADR-NNNN`.
