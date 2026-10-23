# Infrastructure

| Path | Purpose |
| --- | --- |
| `environments.md` | dev / staging / prod: URLs, hosting, who can deploy |
| `<iac-tool>/` | Infrastructure as code (Terraform, Pulumi, or the host's config), chosen by ADR |
| `runbooks/` | Deploy, rollback, incident response, backup restore |

Secrets never go in this repo: use the host's secret store or GitHub Actions secrets.
