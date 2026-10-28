---
id: ADR-0001
title: Technology stack for the EVI store and back office
status: proposed   # the founder accepts, changes, or rejects this
date: 2026-10-28
links: []          # add FR/NFR IDs once the SRS exists
---

# ADR-0001: Technology stack

## Context

EVI is a direct-to-consumer clothing brand. The software must sell clothing online (catalog with
sizes and colors, body-shape fits, size charts, outfit building, cart, checkout, payments, shipping, returns,
tax), publish campaign content in Arabic (right-to-left) and English, and meet `docs/standards.md`
(WCAG 2.2 AA, Core Web Vitals, OWASP, PCI DSS, privacy).

Decided by the founder on 2026-10-23:

- Markets: **launch in Egypt** (decided 2026-10-28), the Gulf later; company registered in Egypt. EGP first,
  Gulf currencies later; cash on delivery and Paymob-type card and wallet payments in Egypt (MI-007).
- **No Shopify.** EVI owns its platform and code.
- **Self-hosted** (decided 2026-10-24): EVI runs the commerce engine on its own managed hosting rather
  than a vendor cloud, to keep costs at the minimum.
- The founder knows **Angular, Django, and .NET**, has about 2 hours a day for the whole business, and will
  mostly review rather than write code; Claude writes and explains the code.

This proposal is written before the BRD and SRS exist. Re-check it against them before accepting.

## Options considered

| Option | Founder already knows | Pros | Cons |
| --- | --- | --- | --- |
| **A. Saleor (Python/Django commerce engine, GraphQL API) + Next.js storefront** | Django | Commerce basics ready: products, variants, stock, cart, checkout, orders, returns, promotions, **channels per country and currency**, taxes, admin dashboard. Built on Django, so the core is readable to the founder. Open source (BSD). Official Next.js storefront to start from | Regional payment providers need a small "payment app" each (Paymob, Fawry, Tap, Tabby, Tamara) unless ready ones exist; Next.js is new to the founder |
| **B. Medusa (Node.js/TypeScript commerce engine) + Next.js storefront** | No | Same commerce basics; one language (TypeScript) everywhere; custom modules run inside the engine | Whole stack new to the founder |
| **C. Django + django-oscar (or fully custom Django) + Angular storefront** | Django, Angular | Everything familiar; full control | More to build (checkout, promotions, multi-currency, admin polish); Angular storefronts need extra work for SEO; slower to launch |
| **D. .NET (nopCommerce) + Angular** | .NET, Angular | Familiar; mature open-source .NET commerce | Smaller ecosystem for regional payments and modern headless storefronts; heavier hosting |

## Decision (proposed, revised 2026-10-28)

**Option B: Medusa + Next.js, self-hosted.** The first draft recommended Saleor because of the founder's
Django experience. Research on 2026-10-28 changed the recommendation:

| Factor | Saleor | Medusa |
| --- | --- | --- |
| Paymob (Egypt's main gateway) | No ready app found; must be built | No ready plugin found; must be built |
| How a new payment method is added | "Payment App": a separate service talking through webhooks; Saleor's docs mark this feature as Feature Preview | Payment provider module inside the engine; several community providers exist as examples (PayPal, Przelewy24, iPay) |
| EVI's own features (body-shape fit, outfit builder, size advice) | Separate apps talking through webhooks | Modules inside the engine: fewer moving parts |
| Languages | Python backend, TypeScript storefront | TypeScript everywhere |
| Founder familiarity | Django underneath (helpful for reading code) | New, but the founder mainly reviews; Claude writes the code |
| Fallback if self-hosting becomes a burden | Saleor Cloud, expensive | Medusa Cloud from about US$29/month |

Payments must be custom-built either way, so the founder's Django familiarity no longer outweighs Medusa's
simpler extension model, single language, and cheaper fallback. Saleor remains a valid option A.

| Layer | Choice |
| --- | --- |
| Commerce backend `apps/api` | Medusa (Node.js, TypeScript), self-hosted |
| EVI-specific logic | Medusa modules: body-shape fit, outfit builder, size recommendation |
| Payments | Custom Paymob provider (cards, wallets) and cash on delivery for Egypt; Gulf providers later |
| Storefront `apps/web` | Next.js (React), Arabic and English |
| Admin | Medusa admin dashboard, extended with EVI screens |
| Database and cache | PostgreSQL and Redis (managed) |
| Styling | Tailwind CSS themed from `design-system/tokens`; accessible components (Radix UI); right-to-left support |
| Email | Transactional email service (e.g. Resend or Postmark) |
| Analytics | PostHog or GA4, consent-managed |
| Testing | Vitest, Playwright, axe-core, Lighthouse CI |
| Hosting | Storefront on Vercel; Medusa, PostgreSQL, and Redis on a managed host near Egypt |
| Monitoring | Sentry, uptime checks, tested backups |
| CI/CD and security | GitHub Actions, Dependabot, CodeQL, secret scanning, Claude Code review on pull requests |

All library versions are pinned at setup time to the current stable releases.

Sources (accessed 2026-10-28): [Saleor payments docs](https://docs.saleor.io/docs/3.x/developer/payments),
[Paymob developer docs](https://developers.paymob.com/paymob-docs/developers),
[Medusa custom payment providers discussion](https://github.com/medusajs/medusa/discussions/15785),
[Medusa PayPal guide](https://docs.medusajs.com/resources/integrations/guides/paypal).

## Consequences

- **Payment gateways must be confirmed before accepting this ADR:** which gateways can contract with an
  Egypt-registered company, which currencies they settle, and whether ready payment plugins exist for Medusa.
  A short comparison goes in `docs/04-system-analysis/payments.md` in phase 5.
- EVI owns security updates, backups, uptime, and PCI compliance (kept minimal with hosted payment fields).
- Hosting and service costs go into `docs/03-business/financial-model.md`; no per-order platform fee.
- Licence and hosting costs (checked 2026-10-23, verify on vendor pages before deciding):

  | | Saleor | Medusa |
  | --- | --- | --- |
  | Licence | BSD-3, free to self-host | MIT core, free to self-host (some Enterprise features under separate terms) |
  | Self-hosted infrastructure | About US$10–25/month on a small managed host (third-party guide) | Similar; Node.js, PostgreSQL, Redis, 2 GB RAM per instance |
  | Vendor-managed cloud | Saleor Cloud; third-party sources conflict (about US$159 to US$1,599/month) | Medusa Cloud from US$29/month (Develop), US$99 (Launch), US$299 (Scale), plus usage |

  With a minimum budget, both are affordable if self-hosted. If self-hosting ever becomes a burden,
  Medusa Cloud is far cheaper than Saleor Cloud.
  Sources: [Medusa Cloud pricing](https://docs.medusajs.com/cloud/pricing), [Medusa licence](https://github.com/medusajs/medusa),
  [Saleor on Railway](https://railway.com/deploy/saleor), [Saleor pricing overview](https://gappsy.com/tools/saleor/).
- Next.js and Medusa are new to the founder; both use TypeScript and components, close to Angular.
  Claude writes and explains the code.
- When accepted: scaffold `apps/web` and `apps/api`, add build, lint, test, and CodeQL jobs to CI, and record
  the commands in `CLAUDE.md`.
- Revisit if Medusa blocks a must-have requirement in the SRS; option A (Saleor) is the fallback.
