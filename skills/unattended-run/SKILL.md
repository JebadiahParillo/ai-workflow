---
name: unattended-run
description: Pre-flight checklist before work runs without someone watching (a /goal run, /loop, a /schedule routine, a claude -p script, an end-of-day agent or a cloud session). Confirms a done condition, a self-check, scoped permissions, a turn or spend cap and a human sign-off. Use before starting any long or overnight run.
---

# Unattended run

Answer each question with the concrete value. Any blank answer: fix it or
don't start.

1. **Done:** the condition, phrased as something checkable (a `/goal`
   condition, a failing test that must turn green, a spec's acceptance list).
2. **Self-check:** the command it runs (`scripts/check`), and whether a Stop
   hook enforces it.
3. **Scope:** the branch or worktree it works in; deny rules and sandbox on;
   no push to `main` (branch protection, not just a prompt line). Network limited
   to what the task needs.
4. **Untrusted input:** does it read issues, web pages, emails or third-party
   docs? If so it gets no push rights and no secrets; its output is a report
   or a draft PR only.
5. **Stop:** `--max-turns` and `--max-budget-usd` for `claude -p`; a plan
   spend limit for routines; a time box for `/loop`.
6. **Result and sign-off:** where it lands (PR, report file, issue comment)
   and who approves it. Nothing public or irreversible runs without that
   approval.

Then:

- Try it on a small slice first (three files, one ticket) and read the result
  before scaling up.
- Watch the first few runs of any new routine.
- Note the run in the retro: time, cost (`/usage`), and whether its output
  was usable.
