---
name: system-analysis
description: Turn Sada's business requirements into a system specification (SRS with FR/NFR, use cases, user stories with acceptance criteria, domain model, C4 architecture, OpenAPI contract, traceability matrix) in docs/04-system-analysis.
---

# System analysis

1. Read `docs/03-business/brd.md`, personas, and `docs/05-ux-ui/` if present.
2. `srs.md`: derive `FR-###` from each `BR` (keep the link) and `NFR-###` (performance, security,
   privacy/data protection, accessibility WCAG 2.2 AA, localization/RTL if relevant, availability).
3. Use cases for each actor goal in `use-cases/` from `templates/system/use-case.md`.
4. User stories in `user-stories/` from `templates/system/user-story.md`, INVEST-sized, Given/When/Then criteria, and
   a release tag (`mvp`, `v1.1`, …).
5. `domain-model.md`: Mermaid `erDiagram` with attributes and cardinalities.
6. `architecture.md`: C4 context and container diagrams (Mermaid), integrations (payments,
   shipping, email, analytics, CMS), auth, data storage, hosting.
7. Propose the tech stack as `adr/0001-tech-stack.md` (options table, recommendation, trade-offs)
   and leave it `proposed` for the user to accept.
8. `api/openapi.yaml`: OpenAPI 3.1 for MVP stories.
9. `traceability.md`: BR → FR → US (→ SCR → PR later). List any gaps.
