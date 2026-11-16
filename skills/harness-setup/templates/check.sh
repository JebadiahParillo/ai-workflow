#!/usr/bin/env bash
# One command for everything that must pass. Quiet on success, loud on failure.
# Usage: scripts/check          full suite (what CI runs)
#        scripts/check --quick  fast subset (the Stop hook runs this)
set -uo pipefail
cd "$(dirname "$0")/.."

# Fill these in for the repo. Each entry is one shell command.
QUICK=(
  # "npx tsc --noEmit"
  # "npm run lint --silent"
  # "pytest -q -x tests/unit"
)
FULL=(
  "${QUICK[@]}"
  # "pytest -q"
  # "pio test -e native"
)

steps=("${FULL[@]}")
[[ "${1:-}" == "--quick" ]] && steps=("${QUICK[@]}")

if [[ ${#steps[@]} -eq 0 ]]; then
  echo "scripts/check: no steps configured" >&2
  exit 1
fi

# A user-only escape hatch for stopping on red on purpose: launch the session
# with CLAUDE_ALLOW_RED=1. Failures still print; the Stop hook won't block.
allow_red=0
[[ "${1:-}" == "--quick" && "${CLAUDE_ALLOW_RED:-0}" == "1" ]] && allow_red=1

failed=0
for cmd in "${steps[@]}"; do
  out=$(bash -c "$cmd" 2>&1)
  if [[ $? -ne 0 ]]; then
    echo "FAIL: $cmd"
    echo "$out" | tail -n 40
    failed=1
  fi
done

[[ $failed -eq 0 ]] && echo "check: ok (${#steps[@]} steps)"
[[ $allow_red -eq 1 ]] && exit 0
exit $failed
