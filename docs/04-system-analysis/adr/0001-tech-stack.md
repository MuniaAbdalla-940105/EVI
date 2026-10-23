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
sizes and colors, body-shape fits, size charts, outfit building, cart, checkout, payments, shipping, returns,
tax), publish campaign content in Arabic (right-to-left) and English, and meet `docs/standards.md`
(WCAG 2.2 AA, Core Web Vitals, OWASP, PCI DSS, privacy).

Decided by the founder on 2026-10-23:

- Markets: the Gulf and Egypt; company registered in Egypt. Several currencies (EGP, SAR, AED, KWD, QAR,
  BHD, OMR), cross-border shipping, and local payment methods (cash on delivery in Egypt, buy-now-pay-later
  in the Gulf; see MI-007).
- **No Shopify.** EVI owns its platform and code.
- The founder knows **Angular, Django, and .NET**, and will maintain and review the system. Familiar
  technology matters more than fashionable technology.

This proposal is written before the BRD and SRS exist. Re-check it against them before accepting.

## Options considered

| Option | Founder already knows | Pros | Cons |
| --- | --- | --- | --- |
| **A. Saleor (Python/Django commerce engine, GraphQL API) + Next.js storefront** | Django | Commerce basics ready: products, variants, stock, cart, checkout, orders, returns, promotions, **channels per country and currency**, taxes, admin dashboard. Built on Django, so the core is readable to the founder. Open source (BSD). Official Next.js storefront to start from | Regional payment providers need a small "payment app" each (Paymob, Fawry, Tap, Tabby, Tamara) unless ready ones exist; Next.js is new to the founder |
| **B. Medusa (Node.js/TypeScript commerce engine) + Next.js storefront** | No | Same commerce basics; one language (TypeScript) everywhere; custom modules run inside the engine | Whole stack new to the founder |
| **C. Django + django-oscar (or fully custom Django) + Angular storefront** | Django, Angular | Everything familiar; full control | More to build (checkout, promotions, multi-currency, admin polish); Angular storefronts need extra work for SEO; slower to launch |
| **D. .NET (nopCommerce) + Angular** | .NET, Angular | Familiar; mature open-source .NET commerce | Smaller ecosystem for regional payments and modern headless storefronts; heavier hosting |

## Decision (proposed)

**Option A: Saleor + Next.js.** It reuses the founder's Django knowledge for the business core, and gives the
store the best search-engine and speed results for the customer-facing side.

| Layer | Choice | Why |
| --- | --- | --- |
| Commerce backend `apps/api` | Saleor (Python, Django, GraphQL) | Commerce basics built in; Django underneath |
| EVI-specific logic | Saleor apps (small services) in Python, for body-shape fit, outfit builder, size recommendation, and regional payments | Keeps EVI's own code separate from the engine, so upgrades stay easy |
| Storefront `apps/web` | Next.js (React, server-side rendering), starting from Saleor's storefront | Fast pages, good SEO, Arabic and English routing |
| Admin | Saleor dashboard, extended with EVI screens where needed | No separate back office to build at launch |
| Database and cache | PostgreSQL (managed) and Redis | What Saleor requires; managed for backups |
| Payments | Hosted payment pages or embedded fields: Egypt (e.g. Paymob, Fawry, Kashier), Gulf (e.g. Tap, Checkout.com), buy-now-pay-later (e.g. Tabby, Tamara), and cash on delivery | Local methods; card data never touches EVI's servers |
| Styling | Tailwind CSS themed from `design-system/tokens`; accessible components (Radix UI) | Tokens stay the single source of truth; right-to-left support |
| Content | A headless CMS for campaigns and lookbooks (Payload or Strapi), or Saleor's pages to start | Editorial content without code changes |
| Email | Transactional email service (e.g. Resend or Postmark) | Reliable order emails |
| Analytics | PostHog or GA4, consent-managed | Funnel analytics within privacy rules |
| Testing | pytest (backend), Vitest (storefront), Playwright (end-to-end), axe-core (accessibility), Lighthouse CI (speed) | Maps to the standards baseline |
| Hosting | Storefront on Vercel; Saleor, PostgreSQL, and Redis on a managed platform close to Gulf and Egypt users | Preview deploys per pull request |
| Monitoring | Sentry, uptime checks, tested database backups | Know about failures before customers do |
| CI/CD and security | GitHub Actions, Dependabot, CodeQL, secret scanning, Claude Code review on pull requests | Automated checks on every change |

All library versions are pinned at setup time to the current stable releases.

## Consequences

- **Payment gateways must be confirmed before accepting this ADR:** which gateways can contract with an
  Egypt-registered company, which currencies they settle, and whether Saleor payment apps already exist.
  A short comparison goes in `docs/04-system-analysis/payments.md` in phase 5.
- EVI owns security updates, backups, uptime, and PCI compliance (kept minimal with hosted payment fields).
- Hosting and service costs go into `docs/03-business/financial-model.md`; no per-order platform fee.
- The founder will learn Next.js; it is React-based and closer to Angular than it looks (components,
  TypeScript, routing). Claude writes and explains the code.
- When accepted: scaffold `apps/web` and `apps/api`, add build, lint, test, and CodeQL jobs to CI, and record
  the commands in `CLAUDE.md`.
- Revisit if Saleor blocks a must-have requirement in the SRS; option B (Medusa) is the fallback.
