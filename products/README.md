# Products

Every product Sada sells, physical or digital, has one folder: `PRD-###-slug/`, copied from
`_template/`. Run `/new-product "<idea>"` to create one.

| File | Contents |
| --- | --- |
| `product.md` | Concept, target persona, positioning, variants, status (front matter is validated) |
| `specs.md` | Materials, dimensions, components, care, certifications, compliance |
| `sourcing.md` | Suppliers, MOQ, lead times, sample log |
| `costing.md` | Bill of materials, landed cost, price, margin |
| `content.md` | Names, descriptions, SEO, social captions, packaging and label text, FAQs |
| `assets/` | Sketches, renders, photos, packaging artwork |

`python3 scripts/validate_catalog.py` checks every product folder and prints the catalog.

## Catalog

| ID | Name | Category | Status | Price |
| --- | --- | --- | --- | --- |
| | | | | |
