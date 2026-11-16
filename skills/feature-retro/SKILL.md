---
name: feature-retro
description: Short retrospective after a bet ships or its circuit breaker fires. Records what slipped, which stage should have caught it, time and cost per stage, then hardens the harness and updates WORKFLOW.md and CHANGELOG.md in the ai-workflow repo. Use at the end of every feature or release.
---

# Feature retro

Run on Sonnet at low effort, in a fresh session. Inputs: the pitch and spec, review findings,
the hill chart snapshots, `git log` for the bet, bugs filed against it in the
tracker, and `/usage` for the period. Don't
read the code.

1. Answer in at most seven lines:
   - What slipped, and its cause.
   - Which stage should have caught it.
   - What worked and is worth keeping.
   - Rough time per stage against the appetite, and what cost the most tokens.
   - Did the bet ship inside its appetite? If the circuit breaker fired, why.
   - Any unattended run: was its output usable?
   - Anything you did by hand that you'd now delegate, or the reverse.
2. For each slip, run `/harden` so it can't recur the same way.
3. Make one concrete change to WORKFLOW.md (a lesson, a checklist line, a
   token rule) and add a CHANGELOG entry. If nothing needs changing, say so;
   don't invent a change.
4. If the same gap has appeared twice across retros, propose a skill or
   script for it.
5. If WORKFLOW.md's stages, skills or checklist changed, list the slides of the
   "Idea to Shipped" deck that need the same change.
