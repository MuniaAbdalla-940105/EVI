---
name: factory-pack
description: Prepare and export the documents a factory needs for Sada clothing (RFQ, tech pack, size spec, samples and fit comments, purchase order, vendor manual, QC inspection) as PDFs to send. Use when contacting factories, requesting quotes or samples, placing an order, or inspecting a shipment.
argument-hint: "rfq COL-### | sample PRD-### | order <factory> | inspect PO-###"
---

# Factory pack

First list what's missing from the founder (factory names, quantities, target prices, dates, Incoterm) and ask.

| Stage | Documents to prepare | Saved in |
| --- | --- | --- |
| **rfq**: ask for quotes | RFQ (`templates/factory/rfq.md`), tech pack + size spec per style, vendor manual | `operations/production/RFQ-###-<slug>.md` |
| **sample**: request or comment on samples | Tech pack (current version), round section in `samples.md` | `products/PRD-###/samples.md` |
| **order**: place bulk order | PO (`templates/factory/purchase-order.md`), approved tech packs, vendor manual | `operations/production/PO-###-<factory>.md` |
| **inspect**: before shipping | QC inspection (`templates/factory/qc-inspection.md`) | `operations/production/QC-###-<po>.md` |

Steps:
1. Check the inputs are complete: tech pack has BOM, construction, points of measure, grading, labels;
   fabrics and trims are `approved`; `operations/suppliers/vendor-manual.md` exists (create it from
   `templates/factory/vendor-manual.md` on first use); the factory has a profile in `operations/suppliers/`
   (from `templates/factory/supplier-profile.md`). List any gap and stop if it blocks the stage.
2. Write or update the documents above. The PO quantities and prices must match `costing.md` and the
   RFQ award.
3. Export to PDF (git-ignored, never committed):
   `scripts/export_pdf.sh exports/<stage>-<id> <file.md> [...]` (needs pandoc and Chrome/Chromium;
   if either is missing, use the pdf skill). Embed flats with Markdown image links so they appear in the PDF.
   Name files so the factory can read them: `SADA_<PRD>_<style>_techpack_v<version>.pdf`.
4. If the factory works in another language, add a translated copy of the tech pack and PO beside the
   English one; English stays the reference version.
5. Report the list of PDFs to send. Sending them is the founder's job unless they ask otherwise.
