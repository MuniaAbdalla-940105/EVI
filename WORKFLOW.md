# Sada: end-to-end project workflow

This is how Sada goes from an idea to a launched brand with products, a website/app, and
operations, all managed in this repository with Claude Code.

```
 0 Foundation ─► 1 Discovery ─► 2 Business ─► 3 Brand ─┬─► 4 Collect./products─────────────┐
                 (market+users)  analysis      identity │                            ▼
                                                        └─► 5 System ─► 6 UX/UI ─► 7 Build ─► 8 Deploy ─► 9 Launch & grow
                                                            analysis    + design              & operate      │
                                                                         system                              │
                       ▲                                                                                     │
                       └──────────────────── feedback, metrics, new insights ◄───────────────────────────────┘
```

Phases 3 and 4 run in parallel with 5 and 6 once phase 2 is approved. Phase 9 feeds back into
phase 1: the workflow is a loop, not a line.

---

## How work moves through the repo

1. **Plan it as an issue.** Each piece of work is a GitHub issue built from a template in
   `.github/ISSUE_TEMPLATE/` (research, business, brand, product, feature, bug). Labels mark
   the phase (`phase:1-discovery`, …) and the discipline.
2. **Branch.** One branch per issue: `research/…`, `business/…`, `brand/…`, `product/…`,
   `design/…`, `feat/…`, `fix/…`, `infra/…`, `content/…`.
3. **Do it with Claude Code.** Run the phase's skill (table below). Claude writes the
   documents, assets, or code in the right folder using the templates.
4. **Review in a pull request.** The PR template asks for the IDs touched and a checklist. CI checks
   the product catalog and (once code exists) builds and tests the apps.
5. **Merge sets `status: approved`.** Approved docs are the baseline the next phase builds on.

### Claude Code building blocks

| Mechanism | Where | Used for |
| --- | --- | --- |
| `CLAUDE.md` | repo root | Rules Claude follows in every session: folders, IDs, evidence, tokens |
| Skills (slash commands) | `.claude/skills/<name>/SKILL.md` | One repeatable procedure per phase, e.g. `/new-product` |
| Subagents | `.claude/agents/*.md` | Specialists (market analyst, UX designer, reviewer…) that can run in parallel |
| Web search / fetch | built in | Market data, competitor research, with sources cited |
| GitHub integration | built in | Issues, PRs, CI status, review comments |
| Artifacts | built in | Shareable pages: brand book preview, pitch deck, dashboards |
| Scheduled tasks | built in | e.g. a monthly competitor scan or weekly status report |

---

## Who does what: the maestro, the specialists, and sessions

```
                         YOU (founder, decision maker)
                    approve gates · choose direction · set prices
                                     │
                         MAESTRO = main Claude session
              runs /orchestrate: plans, delegates, integrates, reviews
                                     │
     ┌──────────────┬───────────────┼────────────────┬──────────────────┐
  Research &     Brand &        Clothing          Software          Review
  business       content        products                            (every PR)
  market-analyst brand-designer fashion-designer  system-analyst    consistency-reviewer
  business-      content-writer textile-specialist ux-designer      code-reviewer
  analyst                       garment-technologist engineer       security-reviewer
                                product-developer   qa-engineer
                                                    devops
                                     │
                    THE REPO = shared memory for everyone
        (docs, IDs, standards, decisions; nothing important lives only in a chat)
```

**You** are the decision maker. Claude proposes and builds; you approve each phase gate, the brand
direction, prices, suppliers, and the tech stack (ADRs stay `proposed` until you accept them).
Each phase below lists what Claude needs from you, and every Claude response ends with a
"What I need from you" list.

**The maestro** is the Claude session you're talking to. With `/orchestrate "<goal>"` it plans
the work against this workflow, launches specialist subagents in parallel, reads and reconciles
their output, runs the reviewers, and comes back with results and the decisions you need to make.

**Subagents** (`.claude/agents/`) are specialists launched by the maestro inside one session. Each
starts with a fresh context, does one task, and reports back to the maestro only. **Subagents don't
talk to each other**: the maestro carries information between them, and they share work through
files in the repo.

**Sessions.** Use one session per workstream that runs for hours or days, for example "SS27
collection", "brand identity", "build the store". Sessions don't share memory. They coordinate
through:
1. **The repo** (main channel): each session works on its own branch and merges via PR, so every
   other session sees approved work on `main`.
2. **GitHub issues and PRs**: what's planned, in progress, blocked, and why.
3. **Direct messages** (cloud sessions only): a cloud session can start another session and send it
   a task, and sessions can message each other. Useful for hand-offs, but the result still has to land
   in the repo.

A good rhythm: one maestro session per phase or workstream; it delegates to subagents; it merges to `main`;
the next session starts from what's on `main`.

### Quality and review gates

| Check | Who / what | When |
| --- | --- | --- |
| Consistency (IDs, traceability, tokens, voice, margins, sources) | `consistency-reviewer` | Every PR |
| Code correctness, tests, contract, accessibility, performance | `code-reviewer` agent, built-in `/code-review` | Every code PR |
| Security (OWASP, payments, secrets, personal data, dependencies) | `security-reviewer` agent, built-in `/security-review` | PRs touching auth, payments, data, infra; every release |
| Automated tests (unit, end-to-end, accessibility, performance) | `qa-engineer` writes them; CI runs them | Every code PR |
| Product catalog and tokens valid | CI (`scripts/validate_catalog.py`) | Every PR |
| Dependency updates and vulnerability alerts | Dependabot; CodeQL once code exists | Weekly / every PR |
| Standards baseline | `docs/standards.md`, which every agent follows | Always |

### Staying current (2026 and beyond)

Claude's built-in knowledge has a cutoff, so the agents don't *assume* they know current trends:
- **Standards** (WCAG, OWASP, ISO textile tests, labelling law) live in `docs/standards.md`, with a
  "checked" date. Verify them against the official source before a real decision.
- **Trends** (fashion, color, fabrics, e-commerce UX, marketing) are researched fresh with `/trend-research`,
  saved as dated, sourced reports in `docs/01-market/trends/`. Design agents must cite the latest report or
  research it first. Run it each season, and schedule it quarterly if you like.

---

## Phase 0: Foundation

**Goal:** agree what Sada is and set up the workspace.
**You provide:** what Sada sells, for whom, where, at what price level; your vision in your own words; budget and launch date.

| Do | Output | Claude Code |
| --- | --- | --- |
| Write vision, mission, problem statement | `docs/00-strategy/vision.md` | conversation plus the template |
| Set 2–3 quarterly objectives | `docs/00-strategy/okrs.md` | |
| Draft the high-level roadmap | `docs/00-strategy/roadmap.md` | |
| Create GitHub labels, milestones per phase | GitHub | `/project-status` suggests them |

**Gate:** vision approved by the founders.

## Phase 1: Discovery (market analysis and user research)

**Goal:** prove the market exists and understand who buys.
**You provide:** target region and customer; competitors you already know; 5–10 people from your target group to interview (or approval to start with assumption-based personas).

| Do | Output |
| --- | --- |
| Market sizing (TAM / SAM / SOM), trends, regulations | `docs/01-market/market-analysis.md` |
| Competitor teardown (offer, pricing, channels, brand, reviews) | `docs/01-market/competitors/<name>.md`, `competitor-matrix.md` |
| SWOT and PESTLE | `docs/01-market/swot.md`, `pestle.md` |
| Insights with IDs (`MI-###`) | `docs/01-market/insights.md` |
| Interview guide, interview notes, synthesis | `docs/02-users/interviews/` |
| Personas and jobs-to-be-done | `docs/02-users/personas/PER-###.md` |
| Customer journey maps | `docs/02-users/journeys/` |

**Claude Code:** `/market-analysis "<category> in <region>"` (uses web search and cites
sources), `/user-research` (interview guide, synthesis, personas). Run the
`market-analyst` subagent on several competitors in parallel.

**Gate:** at least 5 sourced insights, 2+ personas grounded in real interviews.

## Phase 2: Business analysis

**Goal:** a business that makes money, stated as requirements.
**You provide:** budget, target margin, price range, sales channels (online only, marketplaces, boutiques), and approval of the BRD and pricing.

| Do | Output |
| --- | --- |
| Business Model Canvas and value proposition | `docs/03-business/business-model-canvas.md`, `value-proposition.md` |
| Business Requirements Document (`BR-###`) | `docs/03-business/brd.md` |
| Pricing strategy and unit economics | `docs/03-business/pricing.md` |
| Financial model (costs, revenue, break-even) | `docs/03-business/financial-model.md` (+ `.xlsx` if needed) |
| Go-to-market: channels, launch plan, KPIs | `docs/03-business/go-to-market.md` |
| Risk register | `docs/03-business/risks.md` |

**Claude Code:** `/business-analysis`. Claude reads phase 1 and drafts each document,
linking every `BR` to the `MI`/`PER` that justifies it.

**Gate:** BRD and pricing approved; every BR traces to an insight.

## Phase 3: Brand identity

**Goal:** a recognisable, consistent brand.
**You provide:** the name's meaning and story, brands you like and dislike, any must-have colors or symbols, languages (e.g. Arabic and English), and your pick of logo concept.

| Do | Output |
| --- | --- |
| Brand strategy: purpose, positioning, personality, archetype | `brand/strategy.md` |
| Voice and tone, with do/don't examples | `brand/voice-and-tone.md` |
| Logo brief → concepts → final (SVG master + exports) | `brand/logo/` |
| Color, type, spacing **as tokens** | `design-system/tokens/*.json` |
| Imagery and photography direction | `brand/imagery.md` |
| Brand book (compiled guidelines) | `brand/brand-book.md`, shareable as an Artifact |

**Claude Code:** `/brand-identity`. Claude writes the strategy, drafts several SVG logo
concepts you can preview, and produces the token files. For final logo polish you can bring
the SVG into Figma/Illustrator and commit the result back to `brand/logo/final/`.

**Gate:** final logo committed; tokens approved; voice guide approved.

## Phase 4: Collections and products (repeats every season or drop)

**Goal:** every product the brand sells is designed, specified, sourced, costed, and has its content ready.
**You provide:** season and launch date, number of styles, target cost and price per style, approval of the line plan, known factories or mills, quantities, Incoterm (who pays shipping), fit feedback on each sample, and sending the factory PDFs.

For clothing, work collection-first:

1. `/trend-research "<category> <season> <region>"` produces a dated trend report.
2. `/new-collection "<season>"`: `fashion-designer` builds the concept, mood, color story, and line plan;
   `textile-specialist` builds the fabric story in `materials/fabrics/FAB-###`. You approve the line plan.
3. Each style becomes `products/PRD-###-slug/` from `templates/products/apparel/`:

| File | Contents | Specialist |
| --- | --- | --- |
| `product.md` | Concept, persona, positioning, collection, fabrics, variants, status | fashion-designer / product-developer |
| `tech-pack.md` | Flats, BOM, construction, points of measure, grading, colorways, labels, quality | garment-technologist |
| `samples.md` | Every sample round: measurements, fit comments, decisions | garment-technologist |
| `size-chart.md` | Customer size chart and fit notes | garment-technologist |
| `specs.md` | Materials summary, care (ISO 3758), compliance, packaging | textile-specialist |
| `sourcing.md` | Factories, MOQ, lead time, samples | product-developer |
| `costing.md` | BOM cost, landed cost, price, margin | product-developer |
| `content.md` | Names, descriptions, SEO, social, label text, FAQs | content-writer |
| `assets/` | Flats (SVG), sketches, photos, packaging artwork | fashion-designer |

Non-clothing products use `templates/products/product/`.

4. Working with factories, `/factory-pack` prepares each stage's documents and exports them as PDFs
   (in `exports/`, never committed) for you to send:

| Stage | What the factory receives | Kept in the repo |
| --- | --- | --- |
| Find a factory | Vendor manual, RFQ, tech packs | `operations/suppliers/`, `operations/production/RFQ-###` |
| Samples | Tech pack, fit comments per round | `products/PRD-###/samples.md` |
| Bulk order | Purchase order, approved tech packs, vendor manual | `operations/production/PO-###` |
| Before shipping | Inspection report (pass / fail) | `operations/production/QC-###` |

**Claude Code:** `/new-collection`, `/new-product`, `/factory-pack`, or `/orchestrate "prepare the SS27 collection"`.
CI runs `scripts/validate_catalog.py` (apparel products must include a tech pack, size chart, and samples file).

**Gate:** product `status: approved` requires an approved PP sample, fabric tests passed, costing
within target margin, and approved content.

## Phase 5: System analysis

**Goal:** turn business requirements into a buildable system specification.
**You provide:** must-have website features, markets and currencies, payment and shipping preferences, and acceptance of the tech stack (ADR-0001).

| Do | Output |
| --- | --- |
| Software Requirements Spec: `FR-###`, `NFR-###` | `docs/04-system-analysis/srs.md` |
| Use cases (`UC-###`) | `docs/04-system-analysis/use-cases/` |
| User stories with acceptance criteria (`US-###`) | `docs/04-system-analysis/user-stories/` |
| Domain / data model (Mermaid ER diagram) | `docs/04-system-analysis/domain-model.md` |
| Architecture (C4 context + container diagrams) | `docs/04-system-analysis/architecture.md` |
| API contract | `docs/04-system-analysis/api/openapi.yaml` |
| Tech stack and other decisions | `docs/04-system-analysis/adr/` |
| Traceability matrix BR → FR → US | `docs/04-system-analysis/traceability.md` |

**Claude Code:** `/system-analysis`, `/adr "<decision>"`.

**Gate:** stack ADR accepted; MVP stories have acceptance criteria; traceability has no gaps.

## Phase 6: UX/UI and design system

**Goal:** validated designs and a component library built on the brand tokens.
**You provide:** feedback on flows and prototypes, and 5 people for usability tests.

| Do | Output |
| --- | --- |
| Information architecture / sitemap | `docs/05-ux-ui/information-architecture.md` |
| User flows (Mermaid) | `docs/05-ux-ui/flows/` |
| Wireframes (low-fi, can be HTML) | `docs/05-ux-ui/wireframes/` |
| UI screen specs (`SCR-###`) linked to stories | `docs/05-ux-ui/ui/` |
| Usability test plans and results | `docs/05-ux-ui/usability-tests/` |
| Component specs (anatomy, states, a11y) | `design-system/components/` |

**Claude Code:** `/ux-design "<flow>"` produces flows, wireframes, and specs, and can
publish a clickable HTML prototype as an Artifact for stakeholder review. `/design-system`
maintains tokens and component specs.

**Gate:** MVP flows usability-tested; components specified; WCAG 2.2 AA contrast passes.

## Phase 7: Build (frontend and backend)

**Goal:** working software, story by story.
**You provide:** access to accounts (Shopify, hosting, domain) set up by you, and review of each finished feature on the preview link.

- `apps/web`: frontend, consumes `design-system/tokens` (generated into CSS variables/theme).
- `apps/api`: backend, implements `api/openapi.yaml`.
- Each story is its own branch `feat/US-###-slug` and PR, with tests.

**Claude Code:** `/feature US-###`. Claude reads the story, screen spec, and API contract,
then implements, tests, and opens a PR. Use `/code-review` before merging.

**Gate:** CI green; acceptance criteria demonstrated; no open review threads.

## Phase 8: Deploy and operate

**Goal:** reliable, repeatable releases.
**You provide:** domain name, legal pages (terms, privacy, returns) reviewed by a lawyer, and go/no-go for launch.

| Do | Output |
| --- | --- |
| Environments (dev / staging / prod), IaC | `infra/` |
| CI/CD pipelines | `.github/workflows/` |
| Monitoring, alerts, backups, runbooks | `infra/runbooks/` |
| Release notes and versioning | `CHANGELOG.md`, GitHub releases |

**Claude Code:** `/release` prepares the changelog, checks CI, and tags the release.

## Phase 9: Launch and grow

**Goal:** customers, revenue, learning.
**You provide:** launch date, marketing budget, social accounts, and photos from the photoshoot.

| Do | Output |
| --- | --- |
| Website and product page copy | `content/website/` |
| Launch campaign, social calendar, emails | `content/campaigns/`, `content/social/`, `content/email/` |
| Translations | `content/localization/` |
| Support FAQs and macros | `operations/support/` |
| KPI review vs OKRs; new insights back into `01-market/insights.md` | `docs/00-strategy/okrs.md` |

**Claude Code:** the `content-writer` subagent writes on-voice copy from `brand/voice-and-tone.md`
and product `content.md`. A scheduled task can run `/project-status` weekly.

---

## Suggested first two weeks

| Day | Work | Command |
| --- | --- | --- |
| 1 | Vision, OKRs, roadmap draft | (chat) → `docs/00-strategy/` |
| 2–4 | Market analysis + 5–8 competitor teardowns | `/market-analysis` |
| 3–7 | 5–10 customer interviews, synthesis, personas | `/user-research` |
| 6–8 | Business model, BRD, pricing | `/business-analysis` |
| 8–10 | Brand strategy, logo concepts, tokens | `/brand-identity` |
| 8–10 | Trend report and first collection line plan | `/trend-research`, `/new-collection` |
| 10–12 | SRS, stories, architecture; accept or change ADR-0001 (stack) | `/system-analysis`, `/adr` |
| 12–14 | Core flows, wireframes, prototype | `/ux-design` |
