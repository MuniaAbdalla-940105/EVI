# Products

Every collection and product EVI sells. Filled in phase 4, every season.

| Path | Contents | Template |
| --- | --- | --- |
| `fit-system.md` | Body shapes, the three pant fits (Straight, Curvy, Full), and shape-finder rules | — |
| `collections/COL-###-<slug>.md` | Concept, color and fabric story, line plan, critical path | `templates/products/collection.md` |
| `PRD-###-<slug>/` (clothing) | product, tech pack, size chart, samples and fit comments, specs, sourcing, costing, content, assets | `templates/products/apparel/` |
| `PRD-###-<slug>/` (other) | product, specs, sourcing, costing, content, assets | `templates/products/product/` |

Current collection: `collections/COL-001-launch.md` (concept).

`python3 scripts/validate_catalog.py` checks every product folder and prints the catalog. CI runs it.
