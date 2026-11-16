# ai-workflow (v2)

My AI coding workflow for Claude Code: Basecamp's
[Shape Up](https://basecamp.com/shapeup) (shape, bet, build, cool-down) run
with [Matt Pocock's skills](https://github.com/mattpocock/skills), a one-time
harness stage, GitHub Issues, YouTrack or Basecamp as the tracker, a loop for
refining sketches people attach, rules for agents, unattended runs and
security, and a monthly update so it stays current.

- [WORKFLOW.md](WORKFLOW.md): the stages, agents, unattended runs, security, which Claude feature to use when, the failure table, and the improvement path.
- [skills/](skills/): the skills that fill the gaps (below).
- [docs/learning.md](docs/learning.md): courses and reading, in order.
- [docs/sources.md](docs/sources.md): what each rule rests on, with dates.
- [CHANGELOG.md](CHANGELOG.md): how the workflow has changed.

## Skills

| Skill | Stage | What it does |
| ----- | ----- | ------------ |
| `/harness-setup` | 0 | CLAUDE.md, `scripts/check`, deny rules, Stop hook, reviewer agent, tracker |
| `/tracker-sync` | all | Reads and writes GitHub Issues, YouTrack or Basecamp per `.claude/tracker.md` |
| `/shape` | 1 | Appetite, breadboards, fat-marker sketches, rabbit holes, no-gos, pitch |
| `/visual-refine` | 1–8 | Turns attached sketches, photos and screenshots into clean, editable visuals |
| `/betting-table` | 2 | Lays out ready pitches; records the bet and its circuit breaker |
| `/verify-reality` | 4 | Checks every external fact in a spec against primary sources |
| `/hill-chart` | 5 | Uphill/downhill progress per scope as SVG; flags stuck scopes |
| `/hardware-loop` | 4–8 | Printed parts and firmware, with a hardware-in-the-loop check |
| `/unattended-run` | 5+ | Pre-flight before `/goal`, routines, loops or overnight runs |
| `/docs-sync` | 5–7 | Fixes docs that no longer match the code |
| `/ship-checklist` | 7 | Pre-push and pre-release gate |
| `/ticket-to-fix` | 8 | Bug ticket to reproduced, fixed, verified and reported |
| `/feature-retro` | 8 | Short retro with time and cost per stage |
| `/harden` | any | Turns a mistake into a hook, rule, test or line so it can't recur |
| `/workflow-update` | monthly | Researches what's new and opens a sourced PR |

## Install

1. Install Matt Pocock's skills: `npx skills@latest add mattpocock/skills`,
   then run `/setup-matt-pocock-skills` in each repo.
2. Install this repo as a Claude Code plugin:
   `/plugin marketplace add JebadiahParillo/ai-workflow`, then
   `/plugin install ai-workflow@ai-workflow`. Plugin skills are namespaced, so
   `/harden` is also reachable as `/ai-workflow:harden`. Or copy the folders in
   `skills/` into `~/.claude/skills/`.
3. Connect your tracker: the YouTrack connector in Claude (or
   `claude mcp add` with your instance URL plus /mcp), the Basecamp CLI
   (`basecamp auth login`, then `claude mcp add basecamp -- basecamp mcp`), or
   `gh` for GitHub.
4. In each project, run `/harness-setup` once.
5. Schedule `/workflow-update` monthly as a routine (`/schedule`) on this repo.

## Check

`scripts/check` lints the skills: frontmatter, sizes, duplicate names, every
slash command the docs mention, and the templates. CI runs it on every push and
PR.

Licence: MIT.
