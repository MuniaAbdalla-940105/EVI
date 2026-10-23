# Products

Every collection and product Sada sells. Filled in phase 4, every season.

| Path | Contents | Template |
| --- | --- | --- |
| `collections/COL-###-<slug>.md` | Concept, color and fabric story, line plan, critical path | `templates/products/collection.md` |
| `PRD-###-<slug>/` (clothing) | product, tech pack, size chart, specs, sourcing, costing, content, assets | `templates/products/apparel/` |
| `PRD-###-<slug>/` (other) | product, specs, sourcing, costing, content, assets | `templates/products/product/` |

`python3 scripts/validate_catalog.py` checks every product folder and prints the catalog. CI runs it.
