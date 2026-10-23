# Design system

Tokens are the **single source of truth** for color, type, spacing, radius, shadow, and motion.
Brand docs describe *why*; tokens hold *what*; apps consume tokens generated into CSS variables
or a theme object (pipeline chosen in an ADR, e.g. Style Dictionary).

| Path | Purpose |
| --- | --- |
| `tokens/core.json` | Raw palette and scales (no meaning) |
| `tokens/semantic.json` | Meaningful aliases (`color.text.primary` → `{color.neutral.900}`), incl. dark mode |
| `components/<name>.md` | Component spec: anatomy, variants, states, a11y, do/don't |

Format follows the W3C Design Tokens Community Group format (`$value`, `$type`).
Every text/background pair in `semantic.json` must pass WCAG 2.2 AA contrast.
