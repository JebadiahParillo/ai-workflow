---
name: hill-chart
description: Show build progress as a Shape Up hill chart. Places each scope uphill (still figuring it out) or downhill (executing), renders an SVG, compares with the last snapshot to flag stuck or backsliding scopes, and posts it to the tracker. Use during a cycle when someone asks where a bet stands, at each scope milestone, or weekly.
---

# Hill chart

Progress is how solved each scope is, not how many tasks are left.

1. Read the bet's scopes from `docs/bets/<bet>/scopes.json` (create it from the
   tracker's scope list if missing).
2. For each scope, propose a position from 0 to 100 with one line of
   evidence: unknowns still open put it uphill (under 50); "approach known,
   all work visible" is the top (50); downhill is execution, and 100 is done
   and merged. A scope is past the top only if the unknown part was proven by
   building or a spike, not by reasoning.
3. **The person doing the work sets the final positions.** Show the proposal
   and let them move dots; on Basecamp they drag the dots in the hill chart
   themselves.
4. Save the old file as `scopes-<date>.json`, write the new one, and render:
   `python3 ${CLAUDE_SKILL_DIR}/scripts/hill_chart.py scopes.json hill.svg --previous scopes-<last>.json`
5. Act on its warnings: STUCK means ask what's unknown or spike it; BACKSLID
   means split or re-shape the scope; MIXED means split it so parts move
   independently.
6. Push the riskiest uphill scopes first. If uphill scopes remain past the
   middle of the appetite, raise scope hammering or the circuit breaker now,
   not at the end.
7. Post the SVG (or PNG via `rsvg-convert`) and one line per moved scope to the
   bet's tracker item through `/tracker-sync`.
