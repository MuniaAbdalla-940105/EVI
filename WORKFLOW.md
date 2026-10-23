# Sada: end-to-end project workflow

This is how Sada goes from an idea to a launched brand with products, a website/app, and
operations, all managed in this repository with Claude Code.

```
 0 Foundation ─► 1 Discovery ─► 2 Business ─► 3 Brand ─┬─► 4 Products ──────────────┐
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

## Phase 0: Foundation

**Goal:** agree what Sada is and set up the workspace.

| Do | Output | Claude Code |
| --- | --- | --- |
| Write vision, mission, problem statement | `docs/00-strategy/vision.md` | conversation plus the template |
| Set 2–3 quarterly objectives | `docs/00-strategy/okrs.md` | |
| Draft the high-level roadmap | `docs/00-strategy/roadmap.md` | |
| Create GitHub labels, milestones per phase | GitHub | `/project-status` suggests them |

**Gate:** vision approved by the founders.

## Phase 1: Discovery (market analysis and user research)

**Goal:** prove the market exists and understand who buys.

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

## Phase 4: Products (runs per product, repeatedly)

**Goal:** every product the brand sells is fully specified, costed, and has its content ready.

Each product is a folder `products/PRD-###-slug/`:

| File | Contents |
| --- | --- |
| `product.md` | Concept, target persona, positioning, variants, status, links |
| `specs.md` | Materials, dimensions, components, care, certifications |
| `sourcing.md` | Suppliers, MOQ, lead time, samples log |
| `costing.md` | Bill of materials, landed cost, price, margin |
| `content.md` | Name, tagline, short + long description, SEO, social captions, packaging text, FAQs |
| `assets/` | Sketches, renders, photos, packaging artwork |

**Claude Code:** `/new-product "<idea>"` creates the folder from the template, fills each
file, and checks margin against `pricing.md`. CI runs `scripts/validate_catalog.py`.

**Gate:** product `status: approved` requires specs, costing within target margin, and approved content.

## Phase 5: System analysis

**Goal:** turn business requirements into a buildable system specification.

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

- `apps/web`: frontend, consumes `design-system/tokens` (generated into CSS variables/theme).
- `apps/api`: backend, implements `api/openapi.yaml`.
- Each story is its own branch `feat/US-###-slug` and PR, with tests.

**Claude Code:** `/feature US-###`. Claude reads the story, screen spec, and API contract,
then implements, tests, and opens a PR. Use `/code-review` before merging.

**Gate:** CI green; acceptance criteria demonstrated; no open review threads.

## Phase 8: Deploy and operate

**Goal:** reliable, repeatable releases.

| Do | Output |
| --- | --- |
| Environments (dev / staging / prod), IaC | `infra/` |
| CI/CD pipelines | `.github/workflows/` |
| Monitoring, alerts, backups, runbooks | `infra/runbooks/` |
| Release notes and versioning | `CHANGELOG.md`, GitHub releases |

**Claude Code:** `/release` prepares the changelog, checks CI, and tags the release.

## Phase 9: Launch and grow

**Goal:** customers, revenue, learning.

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
| 9–10 | First 1–3 products | `/new-product` |
| 10–12 | SRS, stories, architecture, stack ADR | `/system-analysis`, `/adr` |
| 12–14 | Core flows, wireframes, prototype | `/ux-design` |
