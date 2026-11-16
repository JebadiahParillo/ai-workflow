---
name: docs-sync
description: After a change, find docs (README, guides, docs site, CLAUDE.md) whose numbers, defaults, option names, file names, links or steps no longer match the code, and fix them. Use after /implement when user-facing behaviour, parameters or outputs changed, and from /ship-checklist.
---

# Docs sync

1. From the diff, list what changed for users: defaults, option names, file
   names, commands, steps, outputs.
2. Grep the docs and CLAUDE.md for each one. Read only the matching lines with
   a little context.
3. Fix each mismatch in place. The repo's Markdown is the single source; never
   edit generated output.
4. If a command in CLAUDE.md changed, run the new one to confirm it works.
5. Run the docs build strictly, if there is one, showing only warnings, and
   check links if the build doesn't.
