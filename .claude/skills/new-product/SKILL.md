---
name: new-product
description: Create a new Sada product (physical or digital) with its full package (concept, specs and materials, sourcing, costing and margin, marketing content, assets) under products/PRD-###-slug. Use when designing, adding, or updating a product.
argument-hint: "<product idea>"
---

# New product

1. Find the next free ID: `ls products | grep -o 'PRD-[0-9]*' | sort | tail -1`.
2. `cp -r products/_template products/PRD-###-<slug>`.
3. Read `docs/02-users/personas/`, `docs/03-business/pricing.md`, `brand/voice-and-tone.md`, and
   existing products (avoid overlap; keep the range coherent).
4. Fill, asking the user for anything you can't reasonably infer:
   - `product.md`: concept, persona, insight, positioning vs named competitor products, variants/SKUs.
   - `specs.md`: materials (with sustainability and certification notes), dimensions,
     construction, care, compliance relevant to the category and target markets, packaging.
   - `sourcing.md`: candidate supplier *types* and questions to ask. Do not invent named suppliers
     or quotes; leave them for the user to fill.
   - `costing.md`: BOM and landed cost (estimates labelled), price, margin. Compare to the target
     margin in `pricing.md`; flag it if below.
   - `content.md`: names (3 options), tagline, short/long descriptions, SEO, social captions,
     packaging text, FAQs, all in the brand voice.
   - `assets/`: optional SVG concept sketch or packaging layout.
5. Add the product to the catalog table in `products/README.md`.
6. Run `python3 scripts/validate_catalog.py` and fix errors.
7. If the product needs new app capability (e.g. a configurator), propose `FR`/`US` entries for `/system-analysis`.
