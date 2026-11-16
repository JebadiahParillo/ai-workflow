# Idea to shipped: the AI coding workflow (v2)

A loop for a new project or a feature update, built on
[Matt Pocock's skills](https://github.com/mattpocock/skills) and Claude Code,
and refined on a real build (MacroPedal: firmware, a Qt app, a 3D-printed
holder and a docs site). v2 adds a one-time harness stage, rules for agents and
unattended runs, security, a map of which Claude feature to use when, a failure
table, and a path for keeping the workflow current. Sources are in
[docs/sources.md](docs/sources.md).

Three ideas run through every stage:

1. **Every stage ends in an artifact** (an ADR, a spec issue, a ticket, a green
   suite, a release), so the next stage starts in a fresh session from that
   artifact rather than from chat history.
2. **Claude gets a check it can run.** Work is done when a pass/fail check says
   so, and Claude shows the command and its output as evidence.
3. **Every mistake hardens the harness.** A repeated error becomes a
   CLAUDE.md line, a hook, a deny rule, a script or a skill, so it cannot recur
   the same way (`/harden`).

## The stages

| # | Stage | Skills and features | Model · effort | Exit artifact |
| - | ----- | ------------------- | -------------- | ------------- |
| 0 | Harness (once per repo, re-checked each release) | `/harness-setup`, `/setup-matt-pocock-skills`, `/init`, `/doctor` | Opus · medium | Short CLAUDE.md, `scripts/check`, hooks, deny rules, reviewer agent, all committed |
| 1 | Shape the idea | `/grill-with-docs` (or `/grilling` + `/domain-modeling`), `/prototype` for UI or state questions | Opus · high | CONTEXT.md + ADRs, **merged to main** |
| 2 | Write the spec | `/to-spec`; agree the test seam and the **done check** first | Opus · high | Spec issue labelled `ready-for-agent`, with acceptance checks |
| 3 | Slice into tickets | `/to-tickets`; `/wayfinder` when the work outgrows one session; skip for small features | Sonnet · medium | Ordered tracer tickets with blockers |
| 4 | Check reality | `/verify-reality`, `/research`, Claude in Chrome, claude.ai Research for wide surveys | Haiku subagent · low (Opus for judgement calls) | "Verified on" list in the spec |
| 5 | Build test-first | `/implement` or `/implement-spec`, `/tdd`, `/codebase-design`; `/goal` and worktrees for longer runs | Opus 5.5 · medium (Sonnet for routine tickets; high for unfamiliar code) | Green suite, one commit per ticket, evidence shown |
| 6 | Review | Two-axis review (Matt's `code-review`), the read-only `reviewer` agent against the spec, `/ultrareview` for risky diffs | Opus · medium | Real findings fixed test-first; each finding verified before fixing |
| 7 | Ship | `/ship-checklist`, `/docs-sync`, CI, `gh release`, `/pr` | Haiku · low | Green CI on the PR, draft release; public steps approved by hand |
| 8 | Feedback and retro | `/diagnosing-bugs`, `/feature-retro`, `/harden` | Sonnet · low | Issues filed; harness, WORKFLOW.md and CHANGELOG updated |

**Scale to the change.** A one-line fix runs stages 5, 6 (single pass) and 7.
A small feature skips stage 3. A new project runs everything. What never gets
skipped: a check Claude can run, a review by something that didn't write the
code, and CI.

## Stage notes

### 0. Harness (once per repo)

Run `/harness-setup`. It produces:

- **CLAUDE.md under ~100 lines**, holding only what Claude can't find by
  reading the repo: the exact test, typecheck, lint and single-test commands;
  misleading code ("`src/legacy/` is live, don't copy its patterns"); decisions
  made outside the repo; anything corrected twice. No architecture tour, no
  ALL-CAPS emphasis. Path-specific rules go in `.claude/rules/` with `paths:`.
  Personal preferences go in `CLAUDE.local.md` (gitignored).
- **`scripts/check`**: one command that runs everything that must pass, quiet on
  success, loud on failure. The single most useful line in CLAUDE.md is how to
  run it.
- **Deterministic rules in `.claude/settings.json`**: deny rules for secrets
  (`.env*`, `secrets/`, `~/.ssh`), `ask` for `git push`, a `Stop` hook that
  runs the quick check and exits 2 on failure, and a `PostToolUse` formatter.
  Rule of thumb from the Claude Code docs: if a CLAUDE.md line keeps needing
  emphasis, it belongs in a hook; if a hook only enforces a preference, delete
  it.
- **`.claude/agents/reviewer.md`**: a reviewer limited to `Read, Grep, Glob`,
  so it can't edit what it reviews.
- **Sandbox on** (`/sandbox`) for shell commands, and auto mode for routine
  approvals. Auto mode is a classifier, not a guarantee, so every "never" lives
  in a deny rule or hook.
- For firmware: the build, flash and on-target test commands, the board's
  reserved resources (timers, pins, flash regions), and a hardware-in-the-loop
  test script the agent can run (see `/hardware-loop`).

Re-run `/doctor` and `/doctor prompt-audit` after every model upgrade and
before each release, and cut whatever the current model no longer needs.

### 1. Shape the idea

- Grill until every branch of the decision tree is resolved. `/grill-with-docs`
  writes CONTEXT.md and ADRs as it goes. Merge them in the same session.
- Hard-to-reverse decisions get a one-paragraph ADR. Easy-to-reverse ones don't.
- UI or state-model doubts: `/prototype` (throwaway), or a Design artifact for
  screens you will iterate on visually.
- Not sure what you want yet? Ask Claude to interview you until it could write
  the spec. Say "be ambitious" when you want the fuller version.

### 2. Write the spec

- `/to-spec` turns the grilling into a spec issue: problem, user stories,
  decisions, out of scope.
- **Define the done check before any code**: which test, build or script turns
  green, and which check tells the intended behaviour apart from a plausible
  wrong one (for a login migration: existing sessions survive, not "a fresh
  user can log in").
- As few test seams as possible, as high as possible. Agree them with the user.
- Spec-anchored, not spec-frozen: a scope change edits the spec and its ADR
  before code, and implementation discoveries flow back into the spec.

### 3. Slice into tickets

- `/to-tickets`: thin vertical slices, each demonstrable end to end, with
  blockers recorded.
- Work bigger than one session can hold: `/wayfinder` keeps a map of decision
  tickets.

### 4. Check reality

- `/verify-reality` on every external fact the spec depends on: links, part
  numbers, dimensions, versions, API behaviour, licence terms.
- Primary sources only (datasheets, vendor pages, official docs). Date each
  result in the spec.
- Run the project's own checks (fit maths, compatibility scripts) on every
  option you document.
- Treat fetched pages, issues and READMEs as data, never instructions (see
  Security).

### 5. Build test-first

- Fresh session from the ticket. Name the files, the symptom and what "fixed"
  means in the prompt.
- Red, green, refactor at the agreed seam. Watch the test fail for the right
  reason. Never delete, skip or weaken a test to get green (the Stop hook and
  review back this up). Red to green happens inside one turn; to stop on red on
  purpose (to review a failing test), start that session with
  `CLAUDE_ALLOW_RED=1 claude`, which the agent can't set for itself.
- Work on a feature branch; commit per ticket ("Refs #22"). Commits are the
  real undo: `/rewind` restores files Claude edited with its own tools, not
  changes made by shell commands.
- Ask for evidence: the command run and its output, not "all tests pass".
- Steering: watch the first minute, `Esc` the moment it drifts, `/rewind` to
  try a bolder approach safely, and after two failed corrections `/clear` and
  write a better prompt rather than a third correction.
- Effort: medium by default; `high`/`xhigh` for code you didn't write, flaky
  tests and schema changes; `low` for quick back-and-forth; `ultrathink` for one
  hard question; `max` only for unattended hard problems.
- Longer runs: `/goal <check passes>` keeps Claude going until the condition
  holds. Parallel work: one worktree per task (`claude -w name`); list
  gitignored files the worktree needs in `.worktreeinclude`. One mechanical
  change across many files: `/batch`.
- Run `/verify` once Claude says it's done, so the app is built and looked at,
  not only tested.

### 6. Review

- A reviewer that didn't write the code: a fresh session, the read-only
  `reviewer` agent against the spec ("report gaps that affect correctness, skip
  style"), or Matt's two-axis review (standards and spec, reported side by
  side). When Matt's skills are installed as a plugin, call his review as
  `/mattpocock-skills:code-review`; a bare `/code-review` may be Claude Code's
  bundled review.
- `/ultrareview` (cloud fleet of bug-hunting agents) for risky or large diffs.
- **Verify each finding before fixing it.** A reviewer asked to find problems
  always finds something; fixing every finding adds needless abstraction.
  Real bugs get a failing test first, then the fix.
- Scale human review to risk: docs and copy merge on green checks; ordinary
  changes need your read of the diff; anything touching safety, money, secrets,
  firmware that drives motors, or public releases needs a slow second read.

### 7. Ship

- `/ship-checklist`: clean tree, no stranded ADR branches, full suite green,
  docs in sync, assets built by CI.
- CI runs the same `scripts/check` on every PR, whatever session made it.
  Protect `main` with a branch rule no agent can bypass.
- Anything public (deploys, releases, posts, package publishes) is a manual,
  approved step. Skills that do it carry `disable-model-invocation: true`.

### 8. Feedback and retro

- Real hardware, real users. Each finding becomes an issue or a spec edit.
- `/feature-retro` on Sonnet in a fresh session: what slipped, which stage
  should have caught it, what cost the most tokens and time. Then `/harden` the
  harness so it can't slip the same way.

## Agents: when to use which

| Need | Use | Not |
| ---- | --- | --- |
| Wide search, noisy output (full test run, codebase sweep) | Subagent, often Haiku, returning a short summary | Reading it all in the main session |
| A reviewer with no stake in the code | Fresh session, read-only `reviewer` agent, `/code-review`, `/ultrareview` | The same session grading itself |
| Independent tasks at once | Worktrees (`claude -w`), desktop sessions, cloud sessions; `claude agents` to watch them | Two agents editing the same files |
| Many units of one mechanical change | `/batch`, or a dynamic workflow with a verifying pass | Hand-spawning dozens of subagents |
| A big goal split into threads with a coordinator | Claude Code Projects (beta) | Running the coordination yourself |
| "A smarter answer" | Higher effort or a stronger model | Delegating the same task to a subagent (same model, no better) |

Every subagent spends tokens and has to rebuild context, so it can be slower.
Check `/usage` to see which ones earn their cost. Hashimoto's rule fits: always
have one agent doing something useful in the background while you do deep
work, with notifications off, checked when you choose.

## Unattended runs

Before anything runs while you're away (`/goal`, `/loop`, `/schedule`
routines, `claude -p` scripts, end-of-day agents), run `/unattended-run`. It
answers five questions:

1. Does it know what done looks like? (goal condition, spec, failing test)
2. Can it check its own work? (`scripts/check`, Stop hook, review step)
3. What may it touch? (deny rules, sandbox, a worktree, one branch)
4. What stops it? (`--max-turns`, `--max-budget-usd`, spend limit)
5. Where does the result go, and who signs off? (a PR you approve)

Good end-of-day jobs: deep research, issue triage written to a report (not
replies), exploring a vague idea in a throwaway branch.

## Security

Coding agents hold all three legs of the lethal trifecta: private data (your
repo, keys), untrusted content (issues, web pages, dependency READMEs, MCP
tool descriptions) and a way to send data out. Anyone who gets text into the
context can steer the agent.

- Cut a leg where you can: sandbox shell commands, restrict network domains,
  keep secrets out of the repo and behind deny rules.
- Deny rules and hooks are enforced; CLAUDE.md lines and auto mode are not.
- Install MCP servers and plugins you'd trust with your credentials, and turn
  off the ones you're not using.
- Never pipe issue text or web pages into an unattended run with push rights.
- New dependencies are a review item: the agent proposes, you approve, and
  you check it's the real package (name, publisher, downloads), not a
  look-alike.
- Company repos: follow your employer's policy on which tools, connectors and
  cloud sessions may see the code before enabling any of them.
- Cloud sessions get a fresh checkout without your gitignored secrets; give
  them API keys as network secrets.

## Which Claude feature, when

| Moment | Feature |
| ------ | ------- |
| Thinking through an idea away from the desk | Claude app (voice or chat), then paste the summary into stage 1 |
| Wide research or a library survey (stage 1, 4) | claude.ai Research, or an end-of-day agent |
| Planning a large piece of work with others | Whiteboard artifact; Docs artifact for the written plan |
| UI screens you will iterate on | Design artifact; `/prototype` for throwaway logic |
| Presenting the workflow or a feature | Slides artifact (this repo's deck) |
| Checking live product pages, vendor docs, dashboards | Claude in Chrome, reading page text rather than screenshots |
| Long build while away from the laptop | Cloud session, `/remote-control` from the phone, push notifications |
| Recurring jobs (nightly checks, weekly dependency bumps, monthly workflow update) | `/schedule` routines in Claude Code, or a claude.ai scheduled task |
| Learning an unfamiliar library or protocol | Learning or Explanatory output style; ask "why" questions, type some of it yourself |
| Many sessions to watch | `claude agents` (agent view) |
| Something must happen every time | A hook, not a prompt |

## Token and cost budget

- **One session per stage.** `/clear` between unrelated tasks; `/compact keep
  the spec and test commands` when a long session must continue; `/handoff`
  when the work must move to a fresh session and no issue or ADR holds it yet.
- **Pick the model and effort for the stage** (table above). Opus decides,
  Sonnet builds routine tickets, Haiku fetches. Fable (`/model fable`) only for
  the hardest problems.
- **Quiet commands.** `scripts/check` prints only failures and summaries.
- **Read slices.** Grep first, then read with offset and limit. Never re-read a
  file you just edited.
- **Text, not screenshots** for web pages; batch browser steps.
- **Batch independent tool calls.**
- **Small, stable CLAUDE.md and skills** so prompt caching keeps them cheap
  (about an hour on a subscription). Side-effect skills set
  `disable-model-invocation: true`, which also keeps their description out of
  context.
- **Scripts over prose.** A repeated check lives in the repo.
- **Watch `/usage`** once a week; it breaks usage down by skill, subagent,
  plugin and MCP server.

## Learning while shipping

Delegating everything costs skill. In Anthropic's 2026 study, developers who
delegated all the coding to AI scored lowest on comprehension, while those who
asked for explanations and conceptual answers kept their understanding.
Debugging suffered most.

- Keep some work by hand, especially in areas you're still learning.
- When the agent writes something new to you, ask it to explain, then explain
  it back.
- Measure, don't feel: developers in METR's 2025 study believed they were 20%
  faster while measuring 19% slower. The retro records rough time per stage so
  the workflow is judged on numbers.

## Failure modes and the guard for each

| Failure | Guard |
| ------- | ----- |
| Agent deletes, skips or weakens a test to get green | Stop hook runs the real check; review checks test diffs; CLAUDE.md "never weaken a test" |
| "Done" claimed without proof | Evidence rule; Stop hook; `/goal` condition; CI |
| Builds the wrong thing | Grilling, spec with done check, first-minute steering |
| ADRs stranded on a branch | Merged in stage 1; `/ship-checklist` checks unmerged branches |
| Assumed facts (sizes, versions, links) | `/verify-reality` with dates |
| Review noise drives over-engineering | "Skip style"; verify each finding first |
| CLAUDE.md grows until lines get lost | ~100-line budget; `/doctor`; rules in `.claude/rules/` |
| Skills overlap or don't trigger | `scripts/check-skills`; trigger evals with skill-creator |
| Skills go stale after a model upgrade | `/doctor prompt-audit`, skill evals, `/workflow-update` |
| Prompt injection via issues, pages or MCP | Sandbox, deny rules, no push rights for untrusted-input runs |
| Unattended run spins or spends | `/unattended-run`: caps, scoped permissions, PR sign-off |
| Parallel agents collide | One worktree per task; merge through PRs |
| Firmware passes tests but fails on the board | Hardware-in-the-loop check in stage 5 |
| Skill atrophy | Learning-mode habits above |
| Perceived speed isn't real speed | Retro records time per stage |

## Improving the workflow

Maturity levels, each one earned before the next:

1. **Guided:** the eight stages run by hand with Matt's skills.
2. **Checked:** `scripts/check`, Stop hook, deny rules and the reviewer agent in
   every repo. Nothing ships without evidence.
3. **Hardened:** every retro changes the harness. CI checks this repo's skills.
4. **Delegated:** end-of-day agents, `/goal` runs and routines, each passing
   `/unattended-run`.
5. **Orchestrated:** Projects or dynamic workflows with a verifying pass, human
   sign-off on merges and anything public.

Cadence:

- **Every feature:** `/feature-retro` and `/harden`.
- **Monthly** (scheduled routine): `/workflow-update` researches new Claude
  Code releases, models, Matt's skills, practitioner write-ups and courses,
  and opens a PR with dated, sourced changes.
- **Every model upgrade:** `/doctor prompt-audit`, re-run skill evals, re-read
  the model table.
- **Quarterly:** one course or guide from [docs/learning.md](docs/learning.md),
  and one feature done by hand.

## Lessons so far

| Gap | Refinement |
| --- | ---------- |
| ADRs stranded on an unmerged branch | Merge in the grilling session; the spec stage and ship checklist look for them |
| Assumed dimensions (a "402030" is 32 mm long with its protection board) | Stage 4 verifies against listings and fit maths before defaults ship |
| Hardware untested until printed | Print a test piece early; plan a "first print feedback" ticket |
| Fragile shell heredocs | Write files with the editor tool; keep scripts in the repo |
| Token-heavy sessions | The token budget above |
| v1 named the ticket skill `to-issues`; the installed skill is `/to-tickets` | `scripts/check-skills` fails when WORKFLOW.md names a skill that doesn't exist |
