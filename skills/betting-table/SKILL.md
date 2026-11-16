---
name: betting-table
description: Decide which shaped pitches to build in the next cycle, Shape Up style. Compares pitches on problem, appetite and remaining risk, records the bet with its circuit breaker, and leaves the rest alone (no backlog). Use during cool-down, when choosing what to build next, or when the user asks what to work on.
disable-model-invocation: true
---

# Betting table

The user decides. This skill lays out the bet; it never makes it.

1. Gather the candidates: pitches in `docs/pitches/` and the tracker's pitch
   items from the last few cool-downs, plus any bug the user flags as
   critical. Unshaped ideas aren't candidates; they need `/shape` first.
2. For each pitch, one row: the problem in a sentence, appetite, open rabbit
   holes, what it unblocks, and the cost of not doing it this cycle.
3. Flag pitches that aren't ready: no appetite, open rabbit holes, or a
   solution vaguer than a breadboard.
4. Show the table and ask the user to bet. Fill the cycle up to its capacity,
   no further. A small team or one person usually bets on one big batch or a
   few small ones.
5. Record the bet in the tracker (`/tracker-sync`): the pitch, the cycle dates,
   and the **circuit breaker**: if it isn't shipped by the end of its appetite,
   it stops by default and goes back to shaping, not into an extension.
6. Don't queue the pitches that lost. Leave them where they are; good ideas
   come back.
7. Hand off: the bet's pitch is the input to `/to-spec` (stage 3's done check
   and seam) and then the build.
