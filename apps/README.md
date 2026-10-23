# Apps

| App | Purpose |
| --- | --- |
| `web/` | Customer-facing frontend (storefront / web app) |
| `api/` | Backend: business logic, data, integrations (payments, shipping, CMS) |

The stack is decided in `docs/04-system-analysis/adr/` before code is added. Once chosen, record
the install/build/test/lint commands in each app's README and in the root `CLAUDE.md`.

Inputs each app builds from:
- **web**: `docs/05-ux-ui/ui/` screen specs, `design-system/tokens/`, `api/openapi.yaml`
- **api**: `docs/04-system-analysis/srs.md`, `domain-model.md`, `api/openapi.yaml`
- Both: user stories in `docs/04-system-analysis/user-stories/`
