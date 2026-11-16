# ai-workflow (v2)

My AI coding workflow for Claude Code: a one-time harness stage plus an
eight-stage loop from idea to shipped, built on
[Matt Pocock's skills](https://github.com/mattpocock/skills), with rules for
agents, unattended runs and security, and a monthly update so it stays current.

- [WORKFLOW.md](WORKFLOW.md): the stages, agents, unattended runs, security, which Claude feature to use when, the failure table, and the improvement path.
- [skills/](skills/): the skills that fill the gaps (below).
- [docs/learning.md](docs/learning.md): courses and reading, in order.
- [docs/sources.md](docs/sources.md): what each rule rests on, with dates.
- [CHANGELOG.md](CHANGELOG.md): how the workflow has changed.

## Skills

| Skill | Stage | What it does |
| ----- | ----- | ------------ |
| `/harness-setup` | 0 | CLAUDE.md, `scripts/check`, deny rules, Stop hook, reviewer agent |
| `/verify-reality` | 4 | Checks every external fact in a spec against primary sources |
| `/hardware-loop` | 4–8 | Printed parts and firmware, with a hardware-in-the-loop check |
| `/unattended-run` | 5+ | Pre-flight before `/goal`, routines, loops or overnight runs |
| `/docs-sync` | 5–7 | Fixes docs that no longer match the code |
| `/ship-checklist` | 7 | Pre-push and pre-release gate |
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
3. In each project, run `/harness-setup` once.
4. Schedule `/workflow-update` monthly as a routine (`/schedule`) on this repo.

## Check

`scripts/check` lints the skills: frontmatter, sizes, duplicate names, every
slash command the docs mention, and the templates. CI runs it on every push and
PR.

Licence: MIT.
