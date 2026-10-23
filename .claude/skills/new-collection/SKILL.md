---
name: new-collection
description: Plan a Sada clothing collection or drop (concept, mood, color and fabric story, line plan, critical path) and create its products with tech packs. Use when designing a season, capsule, or drop.
argument-hint: "<season or theme, e.g. SS27 resort capsule>"
---

# New collection

1. Make sure a trend report for this season and category from the last 3 months exists in
   `docs/01-market/trends/`; if not, run `/trend-research` first.
2. Create `products/collections/COL-###-<slug>.md` from `templates/products/collection.md`.
3. In parallel, delegate:
   - `fashion-designer`: concept, mood, color story, line plan (styles, roles, price tiers).
   - `textile-specialist`: fabric story; create or reuse `materials/fabrics/FAB-###` for each fabric.
4. Check the line plan against `docs/03-business/pricing.md` (target margins) and the brand. Present
   the line plan to the founder for approval before creating products.
5. For each approved style, run the `/new-product` flow with the apparel template, then have
   `garment-technologist` complete `tech-pack.md` and `size-chart.md` and `content-writer` write `content.md`.
6. Fill the critical path with dates working back from launch; run
   `python3 scripts/validate_catalog.py` and `consistency-reviewer`.
