---
name: design-system
description: Maintain Sada's design system (W3C-format design tokens in design-system/tokens and component specs in design-system/components), including contrast checks and the token-to-code pipeline.
---

# Design system

- **Tokens:** edit `design-system/tokens/core.json` (raw scales) and `semantic.json` (aliases,
  light/dark). Never put raw values into brand docs or app code.
- **Contrast:** after any color change, compute WCAG contrast for every text/surface pair in
  `semantic.json` (write a small script if needed) and report the table.
- **Components:** spec each in `components/<name>.md` from `templates/design-system/component.md`: anatomy, variants, states,
  tokens used, keyboard/ARIA behaviour, do/don't.
- **Code pipeline:** once the frontend stack ADR is accepted, set up token build (e.g. Style
  Dictionary) so `apps/web` consumes generated CSS variables / theme, and record the command in `CLAUDE.md`.
- Offer to publish a living style-guide page as an Artifact (swatches, type scale, components).
