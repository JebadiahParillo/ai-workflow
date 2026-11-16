---
name: harden
description: Turn an agent mistake into a permanent fix so it can't recur the same way. Picks the right home (CLAUDE.md line, path rule, hook, deny rule, script, skill or test) and applies it. Use when Claude repeats an error, ignores an instruction, a review or retro finds a slip, or the user says "don't let this happen again".
---

# Harden

1. State the mistake in one line, with the evidence (the command, diff or
   output). If it happened once and was a misread prompt, fix the prompt
   instead and stop.
2. Pick the home with the first rule that fits:

   | The fix must… | Put it in |
   | --- | --- |
   | Never be broken (secrets, protected paths, force push) | Deny rule, or `PreToolUse` hook that exits 2 |
   | Always run (format, typecheck before finishing) | `PostToolUse` or `Stop` hook |
   | Be checkable pass/fail | A test, or a step in `scripts/check` |
   | Be a fact Claude can't find in the repo | One line in CLAUDE.md |
   | Apply only in one directory or file type | `.claude/rules/<name>.md` with `paths:` |
   | Be a multi-step procedure | A skill, or a step in an existing skill |
   | Be a repeated manual check | A script in the repo, named in CLAUDE.md |

   A CLAUDE.md line that keeps being missed belongs in a hook. A hook that only
   enforces a preference should be deleted.
3. Apply it in the smallest form: one line, one rule, one test.
4. Prove it: reproduce the original mistake and show the new guard catching
   it. For a CLAUDE.md line, start a fresh session with the original prompt.
5. Keep the budget: if CLAUDE.md is past ~100 lines, move or cut something
   before adding.
6. If the fix belongs in the shared workflow, not just this repo, add a line to
   the ai-workflow repo's WORKFLOW.md lessons table and CHANGELOG.
