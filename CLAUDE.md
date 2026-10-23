# CLAUDE.md: working rules for this repo

This repo holds the **whole Sada business**, not just its software. Treat every folder
as a deliverable that people outside engineering (founders, designers, suppliers,
marketers) will read.

## How Claude communicates

- Be direct. Lead with the answer or the result. No filler, no repeating the question, no long preambles.
- Use short sentences, tables, and lists. Explain jargon in plain words the first time.
- Report facts: what was done, what was checked, what failed. Don't overstate.
- **End every response with "What I need from you"**: a numbered list of the specific inputs,
  files, or decisions needed, each with a recommended answer where one makes sense. If nothing is needed,
  write "Nothing. Next I will …".
- At the start of a phase or skill, first list what's missing from the founder and ask for it, instead of guessing.

## Keep the repo clean

- A file exists only when it has real content. No empty stubs, placeholder files, `.gitkeep`, or
  half-filled templates in working folders. Create a folder when its first real file is written.
- Templates live only in `templates/`. Copy a template, fill it, and delete any section that doesn't
  apply. Never leave HTML comments or `<placeholder>` text in a finished document.
- No drafts, scratch notes, logs, or exports outside their intended folder. Temporary work goes outside the repo.
- File names: lowercase, hyphenated, prefixed with their ID where they have one (`PER-001-layla.md`).
- When you add, rename, or remove a file, update its folder's `README.md` table if the README lists it.
- Before committing, run `git status` and remove anything that doesn't belong.

## Where things go

| If you are producing… | Put it in… |
| --- | --- |
| Vision, OKRs, roadmap | `docs/00-strategy/` |
| Market size, competitors | `docs/01-market/` (one file per competitor in `competitors/`) |
| Trend reports (dated, sourced) | `docs/01-market/trends/YYYY-MM-topic.md` |
| Standards every deliverable must meet | `docs/standards.md` (read before design, product, or code work) |
| Personas, interviews, journeys | `docs/02-users/` |
| Business model, BRD, pricing, financials, GTM | `docs/03-business/` |
| Requirements, use cases, stories, data model, architecture, API | `docs/04-system-analysis/` |
| Architecture / tech / business decisions | `docs/04-system-analysis/adr/NNNN-title.md` |
| IA, flows, wireframes, UI specs | `docs/05-ux-ui/` |
| Brand strategy, voice, logo, brand book | `brand/` |
| Colors, type, spacing, radii (as data) | `design-system/tokens/*.json`, **never hard-code these elsewhere** |
| A collection or drop | `products/collections/COL-###-slug.md` |
| A product | `products/PRD-###-slug/` copied from `templates/products/apparel/` (clothing) or `templates/products/product/` |
| Fabrics and trims | `materials/fabrics/FAB-###-slug.md`, `materials/trims/TRM-###-slug.md` |
| Marketing copy, posts, emails, translations | `content/` |
| Templates for all of the above | `templates/` (only there) |
| Code | `apps/web`, `apps/api`, `infra` |
| Legal, finance, suppliers, support | `operations/` |

Each folder has a `README.md` listing the files that belong there and their template. Read it before writing.

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
   `SCR` screen, `COL` collection, `PRD` product, `FAB` fabric, `TRM` trim, `ADR` decision. IDs are never reused; take the next free number
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

- Clothing products reference fabrics and trims by `FAB`/`TRM` ID and include `tech-pack.md` and `size-chart.md`.
- Fibre, care, and sustainability claims need a certificate or test report behind them (`docs/standards.md`).
- Each product folder must pass `python3 scripts/validate_catalog.py` (CI runs it).
- Cost and price figures in `products/*/costing.md` must agree with `docs/03-business/pricing.md`.

## Code rules (once the stack is chosen)

- Stack choices are recorded as ADRs before code is written. The proposed stack is `ADR-0001`.
- Each feature branch implements one user story and includes its tests.
- Fill in build, test, and lint commands here as soon as `apps/` has real code.

## Workflow and team

Follow the phases in `WORKFLOW.md`. Project skills in `.claude/skills/` implement each phase.
For multi-discipline goals, act as the maestro via `/orchestrate`: delegate to the specialist
subagents in `.claude/agents/`, integrate their work, and run the reviewers before merging:
`consistency-reviewer` on every PR, plus `code-reviewer` and `security-reviewer` on code, infra,
and anything touching payments or personal data.

Don't present remembered trends as current. Use `docs/01-market/trends/` or `/trend-research`.
