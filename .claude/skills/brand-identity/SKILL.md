---
name: brand-identity
description: Create or evolve Sada's brand identity (strategy, positioning, voice and tone, logo concepts as SVG, color and type tokens, imagery, brand book). Use for anything about the logo, brand, colors, fonts, or brand guidelines.
---

# Brand identity

Read `docs/00-strategy/vision.md`, `docs/02-users/personas/`, and `docs/01-market/competitor-matrix.md` first.

1. **Strategy:** `brand/strategy.md`: purpose, positioning statement, 3–5 personality traits
   ("this, not that"), archetype, promise, name story. Check differentiation against competitors' brands.
2. **Voice:** `brand/voice-and-tone.md` with examples per context (product page, social,
   error message, support) and language.
3. **Logo:**
   - Fill `brand/logo/brief.md` with the user.
   - Draft 3–5 distinct directions as hand-written SVG in `brand/logo/concepts/NN-<idea>.svg`
     (clean paths, `viewBox`, no embedded raster, readable at 16px). Add `concepts/README.md`
     explaining each idea.
   - Show them: publish a comparison page as an Artifact (light and dark backgrounds, small
     and large sizes) so the user can choose.
   - For the chosen direction, produce `final/logo-primary.svg`, `logo-mark.svg`,
     `logo-mono.svg`, `logo-reversed.svg`. Note in `brand/logo/README.md` that a designer may refine
     these in a vector tool and commit the result back.
4. **Color and type:** choose the palette and fonts (prefer open-licensed fonts, e.g. Google Fonts;
   check script support for every target language). Write values **only** into
   `design-system/tokens/core.json` and `semantic.json` (light and dark). Verify every text/background
   pair in `semantic.json` meets WCAG AA (4.5:1 body, 3:1 large text); compute ratios, don't guess.
   Explain choices in `brand/color.md` and `brand/typography.md`.
5. **Imagery:** `brand/imagery.md`: photo style, illustration, icon set.
6. **Brand book:** compile `brand/brand-book.md`, and offer to publish it as an Artifact page.
