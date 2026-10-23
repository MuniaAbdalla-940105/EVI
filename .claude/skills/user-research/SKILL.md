---
name: user-research
description: Plan and synthesize customer research for Sada (screener, interview guide, interview synthesis, personas, journey maps, jobs-to-be-done) in docs/02-users.
---

# User research

Ask which step the user needs:

- **Plan:** write `docs/02-users/interviews/guide.md` (goals, screener, 10–15 open, non-leading
  questions mapped to open questions from `docs/01-market/`).
- **Capture:** turn pasted notes or transcripts into `interviews/YYYY-MM-DD-<alias>.md`.
  Strip names, phone numbers, emails, and other personal data.
- **Synthesize:** cluster themes across interviews into `interviews/synthesis.md` with counts
  ("7 of 9 mentioned …") and verbatim quotes.
- **Personas:** from the synthesis only, write `personas/PER-###-<name>.md` from the template,
  listing the evidence files. Write `jobs-to-be-done.md`.
- **Journeys:** for each primary persona, a journey map in `journeys/` (stages, actions,
  thoughts, emotions, pain points, opportunities).

Never invent interview data. If there are no interviews yet, produce proto-personas clearly
marked `status: draft` and `type: proto-persona (assumption-based)`.
