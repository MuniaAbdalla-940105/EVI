# EVI

The single source of truth for the **EVI** brand and business: the research, the
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
| [`docs/standards.md`](docs/standards.md) | Standards baseline: accessibility, security, performance, textile testing, labelling | Everyone |
| [`brand`](brand) | Brand strategy, voice, logo, colors, typography, brand book | Brand designer |
| [`design-system`](design-system) | Design tokens (source of truth) and component specs | Design + frontend |
| [`products`](products) | Collections, plus one folder per product: tech pack, size chart, specs, costing, content, images | Fashion designer, garment technologist |
| [`materials`](materials) | Fabric and trim library with test results and certificates | Textile specialist |
| [`content`](content) | Website copy, social, blog, email, campaigns, translations | Content writer |
| [`apps/web`](apps/web) | Frontend application | Frontend engineer |
| [`apps/api`](apps/api) | Backend application | Backend engineer |
| [`infra`](infra) | Infrastructure as code, environments, deployment | DevOps |
| [`operations`](operations) | Legal, finance, suppliers, customer support | Operations |
| [`templates`](templates) | Every document template, in one place | Everyone |
| [`scripts`](scripts) | Catalog validation, PDF export for factories | Everyone |
| [`.claude`](.claude) | Claude Code skills (slash commands) and specialist subagents | Everyone |

## Quick start with Claude Code

```text
/orchestrate "<goal>"                   # the maestro: plans, delegates to specialists, reviews
/project-status                         # where are we, what's next
/market-analysis <market + region>      # phase 1
/business-analysis                      # phase 2
/brand-identity                         # phase 3 (incl. logo SVG concepts)
/trend-research <topic>                 # dated, sourced trends (fashion, UX, tech)
/new-collection <season>                # phase 4: collection, then its products
/new-product <product idea>             # phase 4, one product
/factory-pack <stage> <id>              # phase 4: RFQ, samples, PO, inspection PDFs for factories
/system-analysis                        # phase 5
/ux-design <flow or screen>             # phase 6
/feature US-012                         # phase 7, build one user story end to end
/adr <decision>                         # any time a significant decision is made
/release                                # phase 8
/code-review, /security-review          # built-in reviews before merging code
```

The proposed technology stack is in [`ADR-0001`](docs/04-system-analysis/adr/0001-tech-stack.md),
waiting for your decision.

## Conventions (summary)

Full rules live in [`CLAUDE.md`](CLAUDE.md).

- **Everything is Markdown with front matter** (`id`, `status`, `owner`, `updated`).
- **IDs link the chain:** `MI` market insight → `BR` business requirement → `FR` functional
  requirement → `US` user story → `SCR` screen → PR → test. Clothing uses `COL` collection → `PRD` product → `FAB`/`TRM` materials.
- **Clean repo:** only real content in working folders; templates live in `templates/`.
- **Status flow:** `draft` → `review` → `approved` → `deprecated`.
- **One branch per piece of work** (`research/…`, `brand/…`, `product/…`, `feat/…`, `infra/…`),
  merged through a pull request.
