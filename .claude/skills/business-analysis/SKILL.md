---
name: business-analysis
description: Produce Sada's business analysis (business model canvas, value proposition, BRD with BR-### requirements, pricing, financial model, go-to-market, risks) in docs/03-business, grounded in market and user research.
---

# Business analysis

1. Read `docs/00-strategy/`, `docs/01-market/insights.md`, and `docs/02-users/personas/`.
   If they are empty, warn the user and ask whether to proceed on stated assumptions.
2. Draft, in order, each in `docs/03-business/`:
   1. `business-model-canvas.md`
   2. `value-proposition.md` (one canvas per primary persona)
   3. `brd.md`: objectives, scope, stakeholders, `BR-###` table where each row links the MI/PER
      that justifies it, with MoSCoW priority and a measurable success metric
   4. `pricing.md`: strategy with competitor price evidence, target and minimum margin
   5. `financial-model.md`: cost structure, 3-year monthly/quarterly projection, break-even,
      sensitivity on the 3 riskiest assumptions. For detailed models, also create an `.xlsx`
      (use the xlsx skill) and summarise it here.
   6. `go-to-market.md`: launch segment, channels, messaging pillars, budget, funnel KPIs
   7. `stakeholders.md` (map + RACI) and `risks.md`
3. Label every assumption. End with decisions the founder needs to make.
