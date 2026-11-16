---
name: ship-checklist
description: Pre-push and pre-release gate. Checks branch hygiene, unmerged ADR or decision branches, CI status, release drafts, docs in sync, and that public steps (deploys, publishing, posting) stay manual. Use before pushing a feature or tagging a release.
---

# Ship checklist

Run on Haiku. Every check is a command whose output is limited to failures.

- [ ] The working tree is clean, and the commits reference the spec issue.
- [ ] No unmerged branch holds ADRs or docs this work depends on (`git branch --no-merged` plus a grep for `docs/adr`).
- [ ] The full test suite passes locally, with only the summary lines shown.
- [ ] Docs match the change (run `/docs-sync` if user-facing behaviour changed).
- [ ] Release assets come from CI, not a local build.
- [ ] Public steps (deploys, releases, posts) are listed for the user to approve. Never run them without that approval.
