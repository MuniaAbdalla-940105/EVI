# CLAUDE.md: working rules for this repo

This repo holds the **whole Sada business**, not just its software. Treat every folder
as a deliverable that people outside engineering (founders, designers, suppliers,
marketers) will read.

## Where things go

| If you are producing… | Put it in… |
| --- | --- |
| Vision, OKRs, roadmap | `docs/00-strategy/` |
| Market size, competitors, trends | `docs/01-market/` (one file per competitor in `competitors/`) |
| Personas, interviews, journeys | `docs/02-users/` |
| Business model, BRD, pricing, financials, GTM | `docs/03-business/` |
| Requirements, use cases, stories, data model, architecture, API | `docs/04-system-analysis/` |
| Architecture / tech / business decisions | `docs/04-system-analysis/adr/NNNN-title.md` |
| IA, flows, wireframes, UI specs | `docs/05-ux-ui/` |
| Brand strategy, voice, logo, brand book | `brand/` |
| Colors, type, spacing, radii (as data) | `design-system/tokens/*.json`, **never hard-code these elsewhere** |
| A product (physical or digital) | `products/PRD-###-slug/` copied from `products/_template/` |
| Marketing copy, posts, emails, translations | `content/` |
| Code | `apps/web`, `apps/api`, `infra` |
| Legal, finance, suppliers, support | `operations/` |

Each folder has a `README.md` that lists its expected files. Read it before writing there,
and keep its index up to date when you add a file.

## Document rules

1. Every document starts with front matter:
   ```yaml
   ---
   id: BR-004            # optional for docs that aren't individually referenced
   title: Customers can reorder a past order
   status: draft         # draft | review | approved | deprecated
   owner: "@github-handle"
   updated: 2026-10-23
   links: [MI-002, FR-011]
   ---
   ```
2. **IDs.** `MI` market insight, `PER` persona, `BR` business requirement, `FR` functional
   requirement, `NFR` non-functional requirement, `UC` use case, `US` user story,
   `SCR` screen, `PRD` product, `ADR` decision. IDs are never reused; take the next free number
   (`grep -rho "BR-[0-9]*" docs | sort -u | tail -1`).
3. **Traceability.** A requirement links to the insight or goal that justifies it, and a story
   links to its requirement. A PR that implements a story names the `US-###` in its title.
4. **Evidence over opinion.** Market and business numbers carry a source link and an access date.
   If a number is an estimate, label it `Assumption:` and state how it was derived. Never invent
   statistics, quotes, or interview results.
5. Approved documents change only through a PR, and the PR says why.

## Brand and design rules

- The brand's colors, fonts, and spacing come only from `design-system/tokens/`. Brand docs
  and app code both reference tokens by name (`color.primary.600`), never raw hex.
- Logos are authored as SVG in `brand/logo/`. Exports (PNG, favicon, social sizes) are generated
  from the SVG master, not drawn separately.
- All customer-facing copy follows `brand/voice-and-tone.md`.

## Products

- Each product folder must pass `python3 scripts/validate_catalog.py` (CI runs it).
- Cost and price figures in `products/*/costing.md` must agree with `docs/03-business/pricing.md`.

## Code rules (once the stack is chosen)

- Stack choices are recorded as ADRs before code is written.
- Each feature branch implements one user story and includes its tests.
- Fill in build, test, and lint commands here as soon as `apps/` has real code.

## Workflow

Follow the phases in `WORKFLOW.md`. Project skills in `.claude/skills/` implement each phase;
specialist subagents in `.claude/agents/` can run research or review in parallel.
