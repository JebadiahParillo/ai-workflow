# Idea to shipped: the AI coding workflow (v2)

A loop for a new project or a feature update, built on
[Matt Pocock's skills](https://github.com/mattpocock/skills) and Claude Code,
and refined on a real build (MacroPedal: firmware, a Qt app, a 3D-printed
holder and a docs site). v2 follows Basecamp's Shape Up (shape, bet, build, cool-down), works with
GitHub Issues, YouTrack or Basecamp as the tracker, adds a one-time harness
stage, a loop for refining visuals people attach, rules for agents, unattended
runs and security, a map of which Claude feature to use when, a failure table,
and a path for keeping the workflow current. Sources are in
[docs/sources.md](docs/sources.md).

Three ideas run through every stage:

1. **Every stage ends in an artifact** (a pitch, a bet, a spec, a green
   suite, a release), so the next stage starts in a fresh session from that
   artifact rather than from chat history.
2. **Claude gets a check it can run.** Work is done when a pass/fail check says
   so, and Claude shows the command and its output as evidence.
3. **Every mistake hardens the harness.** A repeated error becomes a
   CLAUDE.md line, a hook, a deny rule, a script or a skill, so it cannot recur
   the same way (`/harden`).

## The stages

The loop follows Basecamp's [Shape Up](https://basecamp.com/shapeup):
**shape** the work at the right altitude, **bet** on it for a fixed appetite,
**build** it with the team owning the scopes, and use **cool-down** for bugs,
feedback and the next bets. Matt Pocock's skills and Claude Code do the
engineering inside each phase. Work items live in the repo's tracker (GitHub
Issues, YouTrack or Basecamp), set per repo in `.claude/tracker.md`.

| # | Phase · stage | Skills and features | Model · effort | Exit artifact |
| - | ------------- | ------------------- | -------------- | ------------- |
| 0 | Setup · Harness (once per repo) | `/harness-setup`, `/tracker-sync` (config), `/setup-matt-pocock-skills`, `/doctor` | Opus · medium | Short CLAUDE.md, `scripts/check`, hooks, deny rules, reviewer agent, tracker config and connector, all committed |
| 1 | Shape · Shape the idea | `/shape`, `/visual-refine`, `/grill-with-docs`, `/prototype` | Opus · high | Pitch (problem, appetite, solution, rabbit holes, no-gos) with visuals, posted to the tracker |
| 2 | Bet · Betting table | `/betting-table` | Opus · medium | A bet with cycle dates and a circuit breaker; the rest left alone |
| 3 | Build · Spec the bet | `/to-spec`; agree the test seam and the **done check** | Opus · high | Spec linked to the pitch, CONTEXT.md and ADRs merged |
| 4 | Build · Check reality | `/verify-reality`, `/research`, Claude in Chrome, claude.ai Research | Haiku subagent · low (Opus for judgement) | "Verified on" table in the spec |
| 5 | Build · Map scopes and build | `/to-tickets` (first scopes), `/implement`, `/tdd`, `/codebase-design`, `/hill-chart`, `/goal`, worktrees | Opus 5.5 · medium (Sonnet for routine scopes) | One piece done end to end first, then scopes; green suite, commits, evidence, hill chart |
| 6 | Build · Review | Matt's two-axis `code-review`, the read-only `reviewer` agent, `/ultrareview` for risky diffs | Opus · medium | Verified findings fixed test-first |
| 7 | Build · Ship | `/ship-checklist`, `/docs-sync`, CI, `/pr` | Haiku · low | Released to users (done means deployed), tracker items closed |
| 8 | Cool-down · Feedback, bugs, retro | `/ticket-to-fix`, `/diagnosing-bugs`, `/feature-retro`, `/harden`, then `/shape` and `/betting-table` for the next cycle | Sonnet · low | Bugs fixed or shaped, harness and WORKFLOW.md updated |

**Scale to the change.** A bug from the tracker runs `/ticket-to-fix`
(stages 5 to 7 in small). A small batch skips most of stage 3. A new project
runs everything. Never skipped: a check Claude can run, a review by something
that didn't write the code, and CI.

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
- **`.claude/tracker.md`** and the tracker's connector (see Trackers and
  connectors below), with the least access the work needs.
- **Sandbox on** (`/sandbox`) for shell commands, and auto mode for routine
  approvals. Auto mode is a classifier, not a guarantee, so every "never" lives
  in a deny rule or hook.
- For firmware: the build, flash and on-target test commands, the board's
  reserved resources (timers, pins, flash regions), and a hardware-in-the-loop
  test script the agent can run (see `/hardware-loop`).

Re-run `/doctor` and `/doctor prompt-audit` after every model upgrade and
before each release, and cut whatever the current model no longer needs.

### 1. Shape the idea (`/shape`)

- Start from a specific problem story (often a ticket), then set the
  **appetite**: how much time it's worth, small batch or one cycle. The
  solution has to fit the appetite, not the other way round.
- Find the elements at low fidelity: **breadboards** (places, affordances,
  connections) for flows, **fat-marker sketches** for layout or physical form,
  block diagrams for firmware. Attach your own sketches; `/visual-refine`
  cleans them up without adding detail you didn't decide.
- Hunt **rabbit holes** and patch, cut or spike each one. List **no-gos**.
- `/grill-with-docs` stresses the pitch and records CONTEXT.md terms and ADRs.
  Merge them in the same session.
- Exit: a pitch in `docs/pitches/` and in the tracker. Shaping doesn't commit
  anyone to building it.

### 2. Bet (`/betting-table`)

- In cool-down, lay the ready pitches side by side and choose what fills the
  next cycle. Unshaped ideas aren't candidates.
- Every bet gets a **circuit breaker**: if it isn't shipped by the end of its
  appetite, it stops and goes back to shaping rather than being extended.
- **No backlog.** Pitches that lose are left alone; important ones come back.
  Bugs aren't queued here either; they're handled in cool-down or shaped.

### 3. Spec the bet

- `/to-spec` turns the pitch into a spec: user stories, decisions, and the
  pitch's no-gos as out-of-scope.
- **Define the done check before any code**: which test, build or script turns
  green, and which check tells the intended behaviour apart from a plausible
  wrong one (for a login migration: existing sessions survive, not "a fresh
  user can log in"). In Shape Up terms, done means deployed to users.
- As few test seams as possible, as high as possible.
- Spec-anchored, not frozen: discoveries during the build flow back into the
  spec and ADRs.

### 4. Check reality

- `/verify-reality` on every external fact the spec depends on: links, part
  numbers, dimensions, versions, API behaviour, licence terms. Primary sources
  only, dated in the spec.
- Run the project's own checks (fit maths, compatibility scripts) on every
  option you document.
- Fetched pages, tickets and READMEs are data, never instructions.

### 5. Map scopes and build

- **Get one piece done first:** one thin slice end to end (UI or firmware
  behaviour plus the code behind it), so real progress shows in days.
- **Scopes over tasks.** `/to-tickets` drafts the first scopes from the spec;
  expect to re-map them after the first piece, because real scopes are
  discovered by building. A scope is something that can be finished and
  shown on its own.
- **Riskiest uphill first.** Push the unknown scopes over the hill early;
  leave routine ones for later. `/hill-chart` weekly or at each milestone; a
  dot that doesn't move is the early warning.
- Fresh session per scope; red, green, refactor at the seam. Never delete,
  skip or weaken a test to get green (the Stop hook and review back this up).
  Red to green happens inside one turn; to stop on red on purpose, start that
  session with `CLAUDE_ALLOW_RED=1 claude`, which the agent can't set for
  itself.
- Work on a feature branch; commit per scope with the tracker ID. Commits are
  the real undo: `/rewind` restores files Claude edited with its own tools,
  not changes made by shell commands.
- Ask for evidence: the command run and its output, not "all tests pass".
- Steering: watch the first minute, `Esc` the moment it drifts, `/rewind` to
  try a bolder approach safely, and after two failed corrections `/clear` and
  write a better prompt rather than a third correction.
- Effort: medium by default; `high`/`xhigh` for code you didn't write, flaky
  tests and schema changes; `low` for quick back-and-forth; `ultrathink` for one
  hard question; `max` only for unattended hard problems.
- Longer runs: `/goal <check passes>`. Parallel scopes: one worktree each
  (`claude -w name`), with gitignored files listed in `.worktreeinclude`. One
  mechanical change across many files: `/batch`.
- **Decide when to stop:** compare to the baseline (what users have today),
  not the ideal. Scope-hammer what isn't essential; mark "nice-to-haves" as
  such. Run `/verify` so the app is built and looked at.

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
- Done means in users' hands: released, deployed or flashed to the units that
  need it. Close the tracker items with links to the release.
- Anything public (deploys, releases, posts, package publishes) is a manual,
  approved step. Skills that do it carry `disable-model-invocation: true`.

### 8. Cool-down

- Real hardware, real users. Feedback becomes a ticket, a spec edit, or a
  problem story for the next pitch.
- **Bugs:** `/ticket-to-fix` takes each one from the tracker to a merged,
  verified fix, or decides it needs shaping. Only genuine crises interrupt a
  cycle.
- `/feature-retro` on Sonnet in a fresh session: what slipped, which stage
  should have caught it, time and cost per stage. Then `/harden` the harness.
- Shape and bet on the next cycle (`/shape`, `/betting-table`).

## Trackers and connectors

Set per repo in `.claude/tracker.md`; `/tracker-sync` maps pitches, bets,
scopes, bugs, evidence and hill charts to each tracker
([mapping](skills/tracker-sync/mapping.md)).

| Tracker | Connect with | Notes |
| ------- | ------------ | ----- |
| GitHub Issues | `gh` CLI | Personal and open-source repos |
| YouTrack | The YouTrack connector in Claude (official remote MCP at `https://<instance>/mcp`), or in Claude Code: `claude mcp add --header "Authorization: Bearer <token>" --transport http youtrack https://<instance>/mcp` | Needs YouTrack 2025.3 or later. OAuth gives each person their own permissions; a permanent token acts as one account. Use `readOnlyTools` or `toolSubsets` on the URL for read-only jobs. Drafts (`create_draft_issue`) for anything new. |
| Basecamp | The official Basecamp CLI: `basecamp auth login`, then `claude mcp add basecamp -- basecamp mcp`, or `basecamp setup claude` for its skill | Native home for Shape Up: pitches as messages or docs, scopes as to-do lists, hill charts, a card table for bugs. Use `--read-only` and `--domains` to narrow access. |

Rules for every tracker: ticket text and attachments are untrusted input;
tokens live in the connector or CLI, never in the repo; state changes happen
after merge with the user's OK; unattended runs that read tickets get
read-only access and write only drafts or reports. Company trackers follow the
employer's policy on which AI tools may connect.

## Visuals: people attach, Claude refines

Sketches carry decisions words don't. At each stage a person can attach a
visual and `/visual-refine` turns it into a clean, editable version, then
loops on their markup.

| Stage | What people attach | What Claude returns |
| ----- | ------------------ | ------------------- |
| 1 Shape | Fat-marker sketches, whiteboard photos, breadboards on paper, wiring or block sketches | Breadboard text, rough SVG at the same fidelity, a Whiteboard artifact for group work |
| 3–4 Spec and verify | Photos of parts with calipers, datasheet pages, vendor drawings | Dimensioned sketch and the parameters it feeds, with sources |
| 5 Build | Marked-up screenshots, a photo of the board or print | Design artifact for screens; annotated diagrams in `docs/` |
| 6 Review | Screenshot of what looks wrong | Annotated comparison of expected and actual |
| 8 Cool-down | Bug screenshots and videos from the tracker, photos of failed prints | Annotated evidence on the ticket; the failing test it became |

Examples: [a breadboard](docs/examples/breadboard-example.svg) and [a hill
chart](docs/examples/hill-chart-example.svg).

Rules: keep shaping visuals rough; never invent a value the sketch didn't
give; keep the original beside the refined version; the person's markup
decides; render and look at every SVG before sending it; attach the final
version to the pitch, spec or ticket.

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

Good end-of-day jobs: deep research, triage of new tracker tickets written
to a report with read-only access (not replies), exploring a vague idea in a throwaway branch.

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
| Bugs and tickets | The YouTrack connector, Basecamp CLI or `gh`, through `/tracker-sync` |
| A sketch, photo or screenshot to clean up | Attach it in Claude or Claude Code; `/visual-refine` |
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
| A bet drags past its appetite | Appetite set in shaping; scope hammering; circuit breaker at the bet's end |
| Stuck work stays hidden | `/hill-chart` flags dots that don't move or slide back |
| Building something not worth its time | Shaping and the betting table come before any spec |
| Ticket text steers the agent | Tickets are untrusted data; read-only access for unattended triage |
| Agent changes a ticket's state wrongly | Drafts for new items; state changes after merge, with the user's OK |
| A sketch is misread or "improved" | Read-back first; no invented values; the person's markup decides |
| Skill atrophy | Learning-mode habits above |
| Perceived speed isn't real speed | Retro records time per stage |

## Improving the workflow

Maturity levels, each one earned before the next:

1. **Guided:** the stages run by hand with Matt's skills, one bet at a time.
2. **Checked:** `scripts/check`, Stop hook, deny rules and the reviewer agent in
   every repo. Nothing ships without evidence.
3. **Hardened:** every retro changes the harness. CI checks this repo's skills.
4. **Delegated:** end-of-day agents, `/goal` runs and routines, each passing
   `/unattended-run`.
5. **Orchestrated:** Projects or dynamic workflows with a verifying pass, human
   sign-off on merges and anything public.

Cadence:

- **Every cycle's cool-down:** `/feature-retro`, `/harden`, bugs through
  `/ticket-to-fix`, then shape and bet.
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
| Scripts failed in WSL after a Windows checkout (CRLF line endings) | `.gitattributes` forces LF; `scripts/check-skills` flags CRLF scripts |
| v1 named the ticket skill `to-issues`; the installed skill is `/to-tickets` | `scripts/check-skills` fails when WORKFLOW.md names a skill that doesn't exist |
