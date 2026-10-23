---
id: ADR-0001
title: Technology stack for the Sada store and back office
status: proposed   # the founder accepts, changes, or rejects this
date: 2026-10-23
links: []          # add FR/NFR IDs once the SRS exists
---

# ADR-0001: Technology stack

## Context

Sada is a direct-to-consumer clothing brand. The software must sell clothing online (catalog with
sizes and colors, size charts, cart, checkout, payments, shipping, returns, tax), publish
editorial and campaign content, possibly in several languages including right-to-left, and meet
`docs/standards.md` (WCAG 2.2 AA, Core Web Vitals, OWASP, PCI DSS, privacy).
We want the frontend and our own logic in this repo, but we shouldn't rebuild commodity commerce
(checkout, payments, tax, inventory) as a small team.

This proposal is written before the BRD and SRS exist. Re-check it against them before accepting.

## Options considered

| Option | Pros | Cons |
| --- | --- | --- |
| **A. Hosted Shopify theme** | Fastest launch, lowest cost, huge app ecosystem, trusted checkout | Limited custom UX; theme code (Liquid) is less flexible; less ownership |
| **B. Shopify as commerce backend + custom Next.js storefront (headless)** | Trusted checkout, payments, tax, inventory, and multi-market handled by Shopify; full design freedom and performance in our own frontend; small custom backend for our logic | Two systems to run; Shopify subscription and fees; some features need Shopify apps or API work |
| **C. Open-source commerce (Medusa) + Next.js + PostgreSQL** | Full ownership and customisation, no platform fees, all code in the repo | We own payments integration, tax, security patches, hosting, and uptime; slower to launch |

## Decision (proposed)

**Option B** for launch, with the commerce layer behind a small adapter in `apps/web` so moving to C later
stays possible.

| Layer | Choice | Why |
| --- | --- | --- |
| Language | TypeScript (strict) everywhere | One language for web and API; types catch errors |
| Frontend `apps/web` | Next.js (React, App Router, server components) | SEO, fast first load, image optimisation, i18n routing, large ecosystem |
| Styling | Tailwind CSS themed from `design-system/tokens` via Style Dictionary; accessible primitives (Radix UI) | Tokens stay the single source of truth; accessible components out of the box; RTL via logical properties |
| Commerce | Shopify (Storefront API for catalog/cart; Shopify checkout; Shopify Markets for currencies and languages) | Checkout, payments, tax, inventory, and PCI scope handled by the platform |
| Backend `apps/api` | Node.js service (Hono or Next.js route handlers) for webhooks, back-office automations, integrations | Only the logic Shopify doesn't cover; keeps the API contract in `openapi.yaml` |
| Database (for our own data) | PostgreSQL (managed, e.g. Neon or Supabase) with Drizzle ORM | Only if `apps/api` needs to store its own data |
| Content | Shopify metaobjects at first; add a headless CMS (Sanity or Payload) if editorial needs outgrow it | Avoids an extra system until needed |
| Email / CRM | Klaviyo (or Shopify Email to start) | Standard for fashion DTC: flows, segmentation |
| Analytics | GA4 + Shopify analytics, or PostHog; consent-managed | Funnel and product analytics within privacy rules |
| Testing | Vitest (unit), Playwright (end-to-end), axe-core (accessibility), Lighthouse CI (performance) | Maps to the standards baseline |
| Hosting | Vercel for `apps/web`; Vercel/Fly.io/Render for `apps/api` | Managed, preview deploys per PR |
| Monitoring | Sentry (errors, performance), uptime check | Know about failures before customers report them |
| CI/CD and security | GitHub Actions; Dependabot; CodeQL; secret scanning; Claude Code review on PRs | Automated checks on every change |
| Design hand-off | Figma (optional) ↔ tokens in the repo | Designers can work visually; the repo stays the source of truth |

All library versions are pinned at setup time to the current stable releases.

## Consequences

- Monthly platform costs (Shopify plan and apps, hosting, email) go into `docs/03-business/financial-model.md`.
- Checkout look-and-feel is limited to what Shopify allows; everything before checkout is fully custom.
- When this ADR is accepted: scaffold `apps/web` and `apps/api`, add build/lint/test/CodeQL jobs to CI,
  and record the commands in `CLAUDE.md`.
- Revisit if the yearly volume makes platform fees exceed the cost of running option C, or if we need
  checkout customisation Shopify can't provide.
