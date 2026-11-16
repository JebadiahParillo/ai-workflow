# Sources for v2

What each change in v2 rests on, checked 2026-11-16. `/workflow-update` adds a
dated section here each month.

| Change | Source |
| ------ | ------ |
| Stage 0 harness; CLAUDE.md only for what Claude can't discover; under ~200 lines; `/doctor prompt-audit` | [Claude Code best practices](https://code.claude.com/docs/en/best-practices) |
| Hook vs CLAUDE.md rule ("emphasis means it belongs in a hook"); Stop hook exit 2; `PostToolUse` formatter; deny rules hold in every mode; sandbox | Claude Code best practices; Lydia Hallie, [Rethinking Claude Code Best Practices](https://ai.engineer/talks/vlfCjWuv4es-rethinking-claude-code-best-practices) |
| Auto mode is a classifier (blocked 89% of dangerous commands in one study) | Hallie talk |
| Define the done check before work; evidence over claims | Hallie talk; best practices |
| Read-only reviewer agent; "skip style"; verify findings | Best practices; Hallie talk |
| Effort levels; Opus 5.5 default at medium; Haiku for simple subagents; subagents don't give smarter answers | Best practices ("Change the model and effort", "Know what subagents cost") |
| `/goal`, `/loop`, `/schedule` routines, worktrees, `/batch`, agent view, five questions before unattended runs | Best practices; [changelog](https://code.claude.com/docs/en/changelog) |
| Projects beta (coordinator and threads) | Anthropic, "Projects redesigned", 2026-09-17 |
| Skill frontmatter (`disable-model-invocation`, `context: fork`, 500-line body, 1,536-character description cap); testing skills with and without | [Skills reference](https://code.claude.com/docs/en/skills) |
| Skill evals and trigger optimisation | Anthropic, [Improving skill-creator](https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills) |
| Harness engineering; end-of-day agents; always one agent running | [Mitchell Hashimoto](https://mitchellh.com/writing/my-ai-adoption-journey) |
| Every mistake into CLAUDE.md; verification loops | Boris Cherny, as reported by VentureBeat and others |
| Red/green TDD; first run the tests; don't ship unreviewed code | [Simon Willison](https://simonwillison.net/guides/agentic-engineering-patterns/) |
| TDD as guardrail against disabled tests and extra complexity | [Kent Beck](https://www.kentbeck.com/summaries/augmented-coding-beyond-the-vibes/) |
| Lethal trifecta; sandboxes over detection | Simon Willison, "Living dangerously with Claude" |
| Spec-anchored over spec-frozen | Birgitta Böckeler on martinfowler.com |
| Learning-while-shipping habits | Anthropic skill-formation RCT, Jan 2026 |
| Measure time, don't trust the feeling | METR 2025 study and its Feb 2026 update |
| Hardware-in-the-loop as the firmware check | arXiv 2307.03817; Agentic HIL and IAR write-ups |
