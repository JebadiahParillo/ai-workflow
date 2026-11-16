# Learning path

Formal courses first, then the practitioner writing this workflow draws on.
`/workflow-update` re-checks this list monthly; dates show when an entry was
last confirmed.

## 1. Courses (free)

| Course | Where | Why | Checked |
| ------ | ----- | --- | ------- |
| Claude Code 101, then Claude Code in Action | [Claude Academy](https://academy.claude.com) (formerly Anthropic Academy) | Official foundations: workflows, context, hooks, subagents | 2026-11 |
| Agent Skills | Claude Academy | Writing skills that trigger and stay small | 2026-11 |
| Model Context Protocol courses | Claude Academy | Building and judging MCP servers | 2026-11 |
| AI Skills for Real Engineers (27 lessons) | [AI Hero, Matt Pocock](https://www.aihero.dev/skills-catalog) | The skills this workflow is built on, lesson by lesson | 2026-11 |

Claude Academy courses end in a completion badge. Anthropic's proctored
certifications are separate and paid (about $99 to $175 per attempt), so a
badge is not a certification.

## 2. Official guidance (re-read after big releases)

- [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices): checks, hooks vs CLAUDE.md, unattended runs, what to stop doing.
- [Extend Claude Code](https://code.claude.com/docs/en/features-overview): when to use CLAUDE.md, rules, skills, subagents, hooks, MCP, plugins.
- [Skills reference](https://code.claude.com/docs/en/skills) and [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices).
- [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).
- [Claude Code changelog](https://code.claude.com/docs/en/changelog) and [What's new](https://code.claude.com/docs/en/whats-new).

## 3. Practitioners

- Ryan Singer, [Shape Up](https://basecamp.com/shapeup) (free online book from Basecamp): the process this workflow's stages follow. Read Part 1 (shaping) and the hill charts chapter first.

- Simon Willison, [Agentic Engineering Patterns](https://simonwillison.net/guides/agentic-engineering-patterns/): red/green TDD, "first run the tests", anti-patterns, code is cheap but good code isn't.
- Mitchell Hashimoto, [My AI Adoption Journey](https://mitchellh.com/writing/my-ai-adoption-journey): reproduce your own work, end-of-day agents, harness engineering.
- Kent Beck, [Augmented Coding: Beyond the Vibes](https://www.kentbeck.com/summaries/augmented-coding-beyond-the-vibes/): TDD as the guardrail; watch for disabled tests and unasked-for complexity.
- Addy Osmani, [My LLM coding workflow going into 2026](https://addyosmani.com/blog/ai-coding-workflow/) and the book [Beyond Vibe Coding](https://beyond.addy.ie/).
- Lydia Hallie (Anthropic), [Rethinking Claude Code Best Practices](https://ai.engineer/talks/vlfCjWuv4es-rethinking-claude-code-best-practices): hooks that exit 2, deny rules, sandbox, review scaled to risk.
- Birgitta Böckeler, [Understanding Spec-Driven Development](https://www.martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html): spec-first vs spec-anchored vs spec-as-source.
- [Software Mansion Agentic Engineering Guide](https://agentic-engineering.swmansion.com/): a maintained handbook, including security.
- [The Ralph Playbook](https://claytonfarr.github.io/ralph-playbook): loop engineering from Geoffrey Huntley's technique; fresh context each iteration, state on disk.

## 4. Evidence (read before believing a speed claim)

- Anthropic, [How AI assistance impacts the formation of coding skills](https://www.anthropic.com/research/AI-assistance-coding-skills) (Jan 2026).
- METR, [We are changing our developer productivity experiment design](https://metr.org/blog/2026-02-24-uplift-update/) (Feb 2026), the follow-up to the 2025 study.

## 5. Embedded and hardware

- [Exploring LLMs for embedded system development and debugging](https://arxiv.org/abs/2307.03817): hardware-in-the-loop verification of generated firmware.
- Vendor documentation MCP servers (Espressif, IAR and others) are worth checking for your toolchain before writing your own.
