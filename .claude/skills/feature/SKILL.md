---
name: feature
description: Implement one Sada user story end to end (frontend and/or backend, tests, docs, pull request) from its US-### spec. Use when building a feature.
argument-hint: "US-###"
---

# Implement a feature

1. Read `docs/04-system-analysis/user-stories/$ARGUMENTS*.md`, its linked FR, screen specs
   (`docs/05-ux-ui/ui/SCR-*`), `api/openapi.yaml`, and relevant ADRs. Stop and ask if the story has no
   acceptance criteria or the stack ADR isn't accepted.
2. Branch `feat/$ARGUMENTS-<slug>`.
3. Plan the change briefly (files, API changes, data migrations) before writing code.
4. Implement backend (contract first: update `openapi.yaml` if needed), then frontend using
   design-system tokens and components only.
5. Tests: one per acceptance criterion at minimum; run the repo's lint/test/build commands from `CLAUDE.md`.
6. Update docs: story `status`, `traceability.md` (add PR), screen spec if the UI changed.
7. Commit, push, and open a PR titled `$ARGUMENTS: <title>` using the PR template.
