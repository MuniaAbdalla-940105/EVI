---
title: Standards baseline
status: draft
owner: ""
updated: 2026-10-23
---

# Standards baseline

Every agent and every person working on EVI follows these. They are the **floor**, not the
ceiling. Versions change, so before relying on one for a decision, check the official source for the
current edition and update the "Checked" column.

Trends (what's fashionable or new this season) are a different thing: they change every few months
and live in dated, sourced reports in `docs/01-market/trends/`, produced by `/trend-research`.

## Digital product

| Area | Standard | Target | Checked |
| --- | --- | --- | --- |
| Accessibility | WCAG 2.2, level AA (WCAG 3 is still a draft) | 0 axe violations; manual keyboard and screen-reader pass | 2026-10 |
| Accessibility law | European Accessibility Act (enforced from June 2025) and local equivalents in each target market | e-commerce must comply if selling to EU consumers | 2026-10 |
| Performance | Core Web Vitals | LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1 at the 75th percentile, mobile | 2026-10 |
| Web security | OWASP Top 10 (latest edition) and OWASP ASVS 5.0 level 2 | No high/critical findings open at release | 2026-10 |
| Payments | PCI DSS 4.x | Never touch card data: use the payment provider's hosted checkout or fields | 2026-10 |
| Privacy | GDPR (EU/UK) and the data protection law of each target market | Consent before non-essential cookies; data map in `operations/legal/` | 2026-10 |
| Design tokens | W3C Design Tokens Community Group format | `design-system/tokens/*.json` | 2026-10 |
| SEO | Semantic HTML, schema.org `Product` / `Offer` structured data, hreflang for each language | | 2026-10 |
| Localization | Unicode CLDR for dates, numbers, currency; full RTL layout support if Arabic is a target language | | 2026-10 |
| Code | TypeScript strict mode, lint and format in CI, tests for each acceptance criterion | | 2026-10 |

## Markets: Egypt and the Gulf

To verify with a local lawyer or official source before launch; listed so nothing is missed.

| Area | What to check | Checked |
| --- | --- | --- |
| Company and tax | Egyptian company registration, tax card, VAT; how sales into each Gulf country are taxed (VAT, customs duty) | — |
| Consumer protection | Egypt's Consumer Protection Law and each Gulf country's rules on online sales, returns, and Arabic-language information | — |
| Personal data | Egypt's Personal Data Protection Law (Law 151 of 2020), Saudi PDPL, UAE PDPL; consent and parental consent for customers under 18 | — |
| Marketing to minors | Rules for advertising to and collecting data from Gen Alpha customers (under 18) on each platform and in each country | — |
| Textile labelling | Saudi (SASO) and Gulf (GSO) textile labelling requirements: fibre content, care, origin, Arabic text | — |
| Payments | Licensed payment gateways for an Egypt-registered company selling in EGP and Gulf currencies; cash on delivery rules | — |

## Apparel and textiles

| Area | Standard | Use | Checked |
| --- | --- | --- | --- |
| Care labels | ISO 3758 care symbols | Every garment's care label | 2026-10 |
| Fibre content labelling | EU Textile Regulation 1007/2011; US FTC Textile Act and Care Labeling Rule; local rules for each target market | Exact fibre % and names on labels and product pages | 2026-10 |
| Harmful substances | OEKO-TEX STANDARD 100, REACH (EU) | Certificate on file for each fabric | 2026-10 |
| Organic / recycled claims | GOTS (organic), GRS / RCS (recycled) | Only claim with a valid transaction certificate | 2026-10 |
| Green claims | EU rules on environmental claims; avoid vague claims like "eco-friendly" | Every sustainability claim is specific and evidenced | 2026-10 |
| Digital Product Passport | EU Ecodesign (ESPR): textiles are a priority group; requirements are still being adopted | Track; design the data model so fabric and origin data is captured from day one | 2026-10 |
| Sizing | ISO 8559 body dimensions; brand size chart in each product's `size-chart.md` | Points of measure and grading | 2026-10 |
| Fabric testing | ISO 105 (colourfastness), ISO 6330 / ISO 5077 (washing and dimensional change), ISO 12945 (pilling), ISO 13934 (tensile strength) | Required tests listed per fabric in `materials/fabrics/` | 2026-10 |
| Quality inspection | AQL sampling per ISO 2859-1 (commonly 2.5 major / 4.0 minor) | Pre-shipment inspection | 2026-10 |

The "Checked" date means the entry was written in October 2026 from general knowledge. Verify each one
against the official source the first time it matters for a real decision, and record the source.
