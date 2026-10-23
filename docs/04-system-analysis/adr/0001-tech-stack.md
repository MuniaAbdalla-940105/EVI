---
id: ADR-0001
title: Technology stack for the EVI store and back office
status: proposed   # the founder accepts, changes, or rejects this
date: 2026-10-23
links: []          # add FR/NFR IDs once the SRS exists
---

# ADR-0001: Technology stack

## Context

EVI is a direct-to-consumer clothing brand. The software must sell clothing online (catalog with
sizes and colors, body-shape fits, size charts, cart, checkout, payments, shipping, returns, tax), publish
editorial and campaign content in Arabic (right-to-left) and English, and meet `docs/standards.md`
(WCAG 2.2 AA, Core Web Vitals, OWASP, PCI DSS, privacy).

Markets (decided 2026-10-23): the Gulf and Egypt, with the company registered in Egypt. That means
several currencies (EGP, SAR, AED, KWD, QAR, BHD, OMR), cross-border shipping and duties, and local
payment methods.

**Founder decision (2026-10-23): no Shopify.** EVI owns its commerce platform and code. The founder has
built e-commerce sites for clients before.

This proposal is written before the BRD and SRS exist. Re-check it against them before accepting.

## Options considered

| Option | Pros | Cons |
| --- | --- | --- |
| **A. Medusa (open-source commerce, Node.js/TypeScript) + Next.js storefront** | Commerce basics ready (products, variants, inventory, cart, orders, returns, regions, currencies, taxes, admin dashboard); same language as the frontend; modular, so custom logic (body-shape fit, outfit builder) fits in as modules; no platform fees; MIT licence | We host and patch it; regional payment providers (Paymob, Fawry, Tap, Tabby, Tamara) need provider modules, which may have to be written |
| **B. Saleor (open-source commerce, Python, GraphQL) + Next.js storefront** | Mature, strong multi-channel and multi-currency, good dashboard | Second language (Python) next to the TypeScript frontend; customisation through apps and webhooks rather than in-process code |
| **C. Fully custom (Next.js + own API + PostgreSQL)** | Total control; exactly what EVI needs | Rebuilds solved problems (inventory, orders, returns, promotions, admin) and takes far longer; more places for bugs |

## Decision (proposed)

**Option A: Medusa + Next.js**, all TypeScript, all in this repo.

| Layer | Choice | Why |
| --- | --- | --- |
| Language | TypeScript (strict) everywhere | One language for storefront, commerce, and tools |
| Storefront `apps/web` | Next.js (React, App Router, server components) | SEO, fast first load, image optimisation, Arabic/English routing |
| Commerce backend `apps/api` | Medusa, with custom modules for body-shape fit, outfit builder, and size recommendation | Commerce basics for free; EVI's differentiators as our own code |
| Admin | Medusa admin dashboard, extended with EVI screens (fit data, collections, drops) | No separate back-office build at launch |
| Database and cache | PostgreSQL (managed) and Redis | What Medusa requires; managed for backups and uptime |
| Payments | Hosted payment pages or embedded fields from regional gateways, through Medusa payment provider modules: Egypt (e.g. Paymob, Fawry, Kashier), Gulf (e.g. Tap, Checkout.com), buy-now-pay-later (e.g. Tabby, Tamara), plus cash on delivery where customers expect it | Local cards, wallets, and instalments; card data never touches EVI's servers, keeping PCI scope minimal |
| Shipping | Provider modules for regional carriers and a fulfilment partner (chosen in phase 8) | Cross-border delivery and returns |
| Styling | Tailwind CSS themed from `design-system/tokens` via Style Dictionary; accessible primitives (Radix UI) | Tokens stay the single source of truth; right-to-left via logical properties |
| Content | Headless CMS (Payload, TypeScript, self-hosted) for campaigns, lookbooks, and pages | Editorial content without code changes |
| Search | PostgreSQL search at launch; Meilisearch if the catalogue grows | Arabic and English search, filters by size, fit, colour |
| Email | Transactional email service (e.g. Resend or Postmark) for orders; marketing tool chosen in phase 9 | Reliable order emails first |
| Analytics | PostHog or GA4, consent-managed | Funnel and product analytics within privacy rules |
| Testing | Vitest (unit), Playwright (end-to-end), axe-core (accessibility), Lighthouse CI (performance) | Maps to the standards baseline |
| Hosting | Storefront on Vercel; Medusa, PostgreSQL, and Redis on a managed platform (e.g. Railway, Render, or a cloud provider) close to Gulf and Egypt users | Preview deploys per pull request; low latency in the region |
| Monitoring | Sentry, uptime checks, database backups with tested restores | Know about failures before customers do |
| CI/CD and security | GitHub Actions; Dependabot; CodeQL; secret scanning; Claude Code review on pull requests | Automated checks on every change |

All library versions are pinned at setup time to the current stable releases.

## Consequences

- **Payment gateways must be confirmed before accepting this ADR:** which gateways can contract with an
  Egypt-registered company, settle in which currencies, and whether ready Medusa provider modules exist or
  must be written. A short gateway comparison goes in `docs/04-system-analysis/payments.md` during phase 5.
- EVI is responsible for security updates, backups, uptime, and PCI compliance (kept minimal with hosted
  payment fields). The `devops` and `security-reviewer` agents own these checks.
- Hosting and service costs go into `docs/03-business/financial-model.md`; no per-order platform fee.
- When accepted: scaffold `apps/web` and `apps/api`, add build, lint, test, and CodeQL jobs to CI, and record
  the commands in `CLAUDE.md`.
- Revisit if Medusa blocks a must-have requirement in the SRS; option B is the fallback.
