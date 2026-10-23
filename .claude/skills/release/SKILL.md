---
name: release
description: Prepare a Sada release (verify CI and approved stories, write CHANGELOG and release notes for customers, tag the version, deployment checklist).
argument-hint: "<version>"
---

# Release

1. Confirm the target branch is green in CI and list merged PRs since the last tag (`git log <last-tag>..HEAD`).
2. Update `CHANGELOG.md` (Keep a Changelog format) grouped by Added / Changed / Fixed, citing `US-###`.
3. Write customer-facing release notes in brand voice in `content/website/releases/<version>.md`.
4. Walk through `infra/runbooks/deploy.md` (create it on first release): migrations, env vars,
   rollback plan, smoke tests.
5. Only after the user confirms: tag `v<version>`, push the tag, and create the GitHub release.
