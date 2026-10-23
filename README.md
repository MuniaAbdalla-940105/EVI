# Sada

The single source of truth for the **Sada** brand and business: the research, the
strategy, the brand identity, the physical and digital products, the content, and
the software that sells them. All of it is versioned, reviewed, and traceable in one repo.

> Start with [`WORKFLOW.md`](WORKFLOW.md). It explains the phases, which Claude Code
> command to use in each one, and what has to be true before you move on.

## Repository map

| Folder | What lives here | Owner role |
| --- | --- | --- |
| [`docs/00-strategy`](docs/00-strategy) | Vision, mission, OKRs, roadmap | Founder / PM |
| [`docs/01-market`](docs/01-market) | Market sizing, competitors, trends, SWOT/PESTLE | Market analyst |
| [`docs/02-users`](docs/02-users) | Personas, interviews, journey maps, JTBD | UX researcher |
| [`docs/03-business`](docs/03-business) | Business model, BRD, pricing, financials, go-to-market | Business analyst |
| [`docs/04-system-analysis`](docs/04-system-analysis) | SRS, use cases, user stories, domain model, architecture, API, ADRs | System analyst / architect |
| [`docs/05-ux-ui`](docs/05-ux-ui) | Information architecture, flows, wireframes, UI specs, usability tests | UX/UI designer |
| [`brand`](brand) | Brand strategy, voice, logo, colors, typography, brand book | Brand designer |
| [`design-system`](design-system) | Design tokens (source of truth) and component specs | Design + frontend |
| [`products`](products) | One folder per product: spec, materials, costing, content, images | Product developer |
| [`content`](content) | Website copy, social, blog, email, campaigns, translations | Content writer |
| [`apps/web`](apps/web) | Frontend application | Frontend engineer |
| [`apps/api`](apps/api) | Backend application | Backend engineer |
| [`infra`](infra) | Infrastructure as code, environments, deployment | DevOps |
| [`operations`](operations) | Legal, finance, suppliers, customer support | Operations |
| [`scripts`](scripts) | Repo tooling (catalog validation, etc.) | Everyone |
| [`.claude`](.claude) | Claude Code skills (slash commands) and specialist subagents | Everyone |

## Quick start with Claude Code

```text
/project-status                         # where are we, what's next
/market-analysis <market + region>      # phase 1
/business-analysis                      # phase 2
/brand-identity                         # phase 3 (incl. logo SVG concepts)
/new-product <product idea>             # phase 4, repeat per product
/system-analysis                        # phase 5
/ux-design <flow or screen>             # phase 6
/feature US-012                         # phase 7, build one user story end to end
/adr <decision>                         # any time a significant decision is made
/release                                # phase 8
```

## Conventions (summary)

Full rules live in [`CLAUDE.md`](CLAUDE.md).

- **Everything is Markdown with front matter** (`id`, `status`, `owner`, `updated`).
- **IDs link the chain:** `MI` market insight → `BR` business requirement → `FR` functional
  requirement → `US` user story → `SCR` screen → PR → test. Products use `PRD-###`.
- **Status flow:** `draft` → `review` → `approved` → `deprecated`.
- **One branch per piece of work** (`research/…`, `brand/…`, `product/…`, `feat/…`, `infra/…`),
  merged through a pull request.
