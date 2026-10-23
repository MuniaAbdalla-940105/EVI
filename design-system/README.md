# Design system

The single source of truth for color, type, spacing, radius, shadow, and motion. Created in phase 3,
extended in phase 6.

| File | Contents | Template |
| --- | --- | --- |
| `tokens/core.json` | Raw palette and scales | — |
| `tokens/semantic.json` | Named roles (`color.text.primary`), light and dark | — |
| `components/<name>.md` | Component specs | `templates/design-system/component.md` |

Tokens use the W3C Design Tokens format:

```json
{ "color": { "text": { "primary": { "$value": "{color.neutral.900}", "$type": "color" } } } }
```

Every text/background pair must pass WCAG 2.2 AA contrast.
