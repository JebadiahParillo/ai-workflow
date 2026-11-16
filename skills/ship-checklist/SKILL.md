---
name: ship-checklist
description: Pre-push and pre-release gate. Checks branch hygiene, unmerged ADR or decision branches, the full check, CI status, docs in sync, release assets built by CI, secrets, and that public steps (deploys, publishing, posting) stay manual. Use before pushing a feature, opening a PR or tagging a release.
---

# Ship checklist

Run on Haiku. Every check is a command whose output is limited to failures.
Report a table of pass/fail; stop at the first failure that blocks shipping.

- [ ] Working tree clean; commits reference the spec issue.
- [ ] No unmerged branch holds ADRs or docs this work depends on
      (`git branch --no-merged main`, then grep those branches for `docs/adr`).
- [ ] `scripts/check` (full) passes; show its summary line.
- [ ] No secrets in the diff (`git diff main...HEAD` grepped for keys, tokens,
      `.env` contents); no new file matching a deny rule.
- [ ] No test deleted, skipped or weakened in the diff without a reason in the
      PR.
- [ ] Docs match the change (`/docs-sync` if user-facing behaviour changed).
- [ ] CI is green on the PR (`gh pr checks`); `main` has branch protection.
- [ ] Release assets come from CI, not a local build.
- [ ] Tracker items for this work are linked to the PR or release; they close
      only after merge (`/tracker-sync`).
- [ ] Public steps (deploys, releases, posts, package publishes) are listed
      for the user to approve. Never run them without that approval.
