---
name: feature-retro
description: Short retrospective after a feature merges. Records what slipped and what worked, then updates WORKFLOW.md (lessons, checklist, token budget) and CHANGELOG.md in the ai-workflow repo. Use at the end of every feature.
---

# Feature retro

Run it on Sonnet at low effort, in a fresh session, with only the spec issue and its commits as input.

1. Read the spec issue, its review findings and `git log` for the feature. Don't read the code.
2. Answer in five lines or fewer: what slipped, its cause, which stage should have caught it, what worked, and what cost the most tokens.
3. Make one concrete change to WORKFLOW.md (a lesson, a checklist line, or a token rule). Add a CHANGELOG entry.
4. If the same gap has appeared twice, propose a skill or a script for it.
