# Changelog

## v2 (2026-11-16)

From a research pass over Anthropic's Claude Code docs and talks, practitioner
write-ups (Hashimoto, Willison, Beck, Osmani, Cherny, Huntley, Böckeler) and
recent studies. Sources in docs/sources.md.

- New stage 0, the harness: short CLAUDE.md, `scripts/check`, deny rules, a Stop hook that exits 2, a formatter hook, a read-only reviewer agent, sandbox.
- Every stage now names its done check and asks for evidence. Spec stage defines the check before code.
- Review: a reviewer that didn't write the code, "skip style", verify each finding before fixing, human review scaled to risk, `/ultrareview` for risky diffs.
- New sections: agents (when to use which), unattended runs, security (lethal trifecta), which Claude feature when, learning while shipping, failure modes and guards, improvement path with maturity levels and cadence.
- Model table updated for Opus 5.5 at medium effort by default, with effort levels per situation.
- Fixed: the ticket skill is `/to-tickets`, not `/to-issues`.
- New skills: harness-setup, harden, unattended-run, workflow-update. Rewrote verify-reality, feature-retro, ship-checklist, hardware-loop (adds firmware and HIL) and docs-sync.
- Repo installs as a Claude Code plugin. `scripts/check` lints skills and commands; CI runs it.
- New docs: learning path and sources.

## v1 (2026-11-16)

- First version, from the MacroPedal build: eight stages (Matt Pocock's flow plus "check reality" and "feedback and retro").
- Model and effort per stage, and a token budget.
- Draft skills: verify-reality, feature-retro, ship-checklist, hardware-loop, docs-sync.
