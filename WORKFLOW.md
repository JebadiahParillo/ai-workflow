# Idea to shipped: the AI coding workflow (v1)

An eight-stage loop for a new project or a feature update. It builds on
[Matt Pocock's skills](https://github.com/mattpocock/skills) and was refined on
a real build (a Bluetooth foot pedal with firmware, a Qt app, a 3D-printed
holder and a docs site). Each stage ends in an artifact, so the next stage can
start in a **fresh session** from that artifact rather than from chat history.

| # | Stage | Skills | Model · effort | Exit artifact |
| - | ----- | ------ | -------------- | ------------- |
| 1 | Shape the idea | `/grilling`, `/domain-modeling` | Opus · high | CONTEXT.md + ADRs, **merged** |
| 2 | Write the spec | `/to-spec` (agree the test seam first) | Opus · high | Spec issue, `ready-for-agent` |
| 3 | Slice into tickets | `/to-issues`, `/wayfinder` (skip for small features) | Sonnet · medium | Ordered tracer tickets |
| 4 | Check reality | `/research`, `/verify-reality`, browser | Haiku subagent · low | Verified facts in the spec |
| 5 | Build test-first | `/implement`, `/tdd`, `/codebase-design` | Sonnet · medium (Opus for design-heavy seams) | Green suite + commit per ticket |
| 6 | Review on two axes | `/code-review` | Sonnet; two subagents only for diffs over ~300 lines | Fixes, test-first, committed |
| 7 | Ship | `/ship-checklist`, CI, `gh release` | Haiku · low | Draft release, green CI; public steps gated by hand |
| 8 | Feedback and retro | `/diagnosing-bugs`, `/feature-retro` | Sonnet · low | Issues filed; this file and its CHANGELOG updated |

## Every-feature checklist

1. Grill the idea; update CONTEXT.md; merge ADRs in the same session.
2. `/to-spec` with an agreed seam; any later scope change edits the spec and its ADR before code.
3. Slice into tickets, unless the feature is small.
4. Verify every external fact (links, sizes, versions) and run the project's own checks on each option.
5. `/implement` with `/tdd` at the seam; commit per ticket.
6. `/code-review`; fix real bugs test-first.
7. Ship through CI; anything public is a manual, gated step.
8. Real-world feedback, then `/feature-retro`.

## Token budget

- **One session per stage.** The handoff is the issue or ADR, not a long transcript.
- **Pick the model for the stage** (table above). Opus decides, Sonnet builds, Haiku fetches.
- **Quiet commands.** Pipe test and build output through `grep`/`tail` so only failures and summaries come back.
- **Read slices.** Grep first, then read with offset and limit. Never re-read a file you just edited.
- **Text, not screenshots.** Read pages with text extraction or a small JS query; batch browser steps.
- **Batch independent tool calls** into one message.
- **Subagents only for wide sweeps,** on a cheap model, returning a conclusion rather than file dumps.
- **Small, stable CLAUDE.md and skills,** so prompt caching keeps them cheap; put long references in files the skill reads only when needed.
- **Scripts over prose.** A repeated check lives in the repo and runs in one call.
- **Scale review to the diff.** A single pass for small changes; two parallel axes for big ones.

## Lessons so far

| Gap | Refinement |
| --- | ---------- |
| ADRs stranded on an unmerged branch | Merge in the grilling session; the spec stage checks for them |
| Assumed dimensions (a "402030" is 32 mm long with its protection board) | Stage 4 verifies against listings and fit maths before defaults ship |
| Hardware untested until printed | Print a test piece early; plan a "first print feedback" ticket |
| Fragile shell heredocs | Write files with the editor tool; keep scripts in the repo |
| Token-heavy sessions | The token budget above |
