---
name: harness-setup
description: One-time setup of a repo for agentic work (stage 0). Writes a short CLAUDE.md, a single scripts/check command, deny rules, a Stop hook that blocks on a failing check, a formatter hook and a read-only reviewer agent. Use when starting a new project, adopting the workflow in an existing repo, or re-checking the harness before a release.
disable-model-invocation: true
---

# Harness setup

Templates are in `${CLAUDE_SKILL_DIR}/templates/`. Copy, then fill in for this
repo; never overwrite an existing file without showing the diff first.

1. **Baseline.** Find how this repo builds, tests, lints and typechecks (CI
   config, package scripts, Makefile, PlatformIO, CMake). Run the full test
   suite once. If it is red, stop and report: a Stop hook on a red baseline
   blocks every turn.
2. **`scripts/check`.** From `templates/check.sh`. Fill `QUICK` with the fast
   steps (typecheck, lint, unit tests for touched code) and `FULL` with
   everything CI runs. Quiet on success, failures only. Make it executable and
   run it both ways. On repos used from Windows, add a `.gitattributes` with
   `* text=auto eol=lf` so scripts keep LF endings and run in bash and WSL.
3. **CLAUDE.md.** Start from `templates/CLAUDE.md`, or prune the existing one
   (`/init` can draft it). Keep only what Claude can't find by reading the
   repo: commands, misleading code, decisions made elsewhere, anything already
   corrected twice. Aim for under 100 lines. Rules for one directory go in
   `.claude/rules/<name>.md` with a `paths:` list.
4. **`.claude/settings.json`.** Merge `templates/settings.json`: deny rules for
   secrets, `ask` for push, the Stop hook. Add a `PostToolUse` formatter hook
   for the repo's formatter (matcher `Edit|Write`, reading the file path from
   the hook input with `jq -r '.tool_input.file_path'`). Add a `PreToolUse`
   hook only for a rule with zero exceptions (generated code, migrations).
5. **Reviewer.** Copy `templates/reviewer.md` to `.claude/agents/reviewer.md`.
6. **Firmware repos.** Add to CLAUDE.md the build, flash and on-target test
   commands and the board's reserved resources. Wire a hardware-in-the-loop
   test into `scripts/check --full` if a board is attached (see
   `/hardware-loop`). Put flashing behind `ask` if the board drives anything
   that moves.
7. **Worktrees.** List small gitignored files a fresh checkout needs in
   `.worktreeinclude`; put the install command in CLAUDE.md.
8. **Matt's skills and the tracker.** Run `/setup-matt-pocock-skills` if not
   done. Run `/tracker-sync` to write `.claude/tracker.md` (GitHub Issues,
   YouTrack or Basecamp) and confirm the connector can read one item. Give
   it the least access the work needs; tokens stay in the connector or CLI.
9. **Prove it.** Ask for a change that breaks the check and confirm the Stop
   hook sends Claude back. Ask Claude to read `.env` and confirm it is denied.
   Run `/doctor`.
10. Commit on a branch as "Harness: …" and list what was added.

Re-run steps 3, 4 and 9 after a model upgrade and before each release.
