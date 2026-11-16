---
name: docs-sync
description: After a change, find docs (README, guides, docs site) whose numbers, defaults, file names, links or steps no longer match the code, and fix them. Use after /implement when user-facing behaviour, parameters or outputs changed.
---

# Docs sync

1. From the diff, list what changed for users: defaults, option names, file names, steps.
2. Grep the docs for each one. Read only the matching lines with a little context.
3. Fix each mismatch in place. Keep the repo's Markdown as the single source.
4. Run the docs build strictly, if there is one, showing only warnings.
