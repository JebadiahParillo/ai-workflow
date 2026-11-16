---
name: shape
description: Shape a raw idea or a big bug into a Shape Up pitch before any spec or code. Sets the appetite, finds the elements with breadboards and fat-marker sketches (refining any the user attaches), removes rabbit holes, lists no-gos, and writes the pitch (problem, appetite, solution, rabbit holes, no-gos). Use at the start of any new feature, project or large fix, or when the user says shape, pitch or appetite.
---

# Shape

Work at the right altitude: concrete enough to bet on, rough enough to leave
room for the builder. No wireframes, no task lists.

1. **Problem.** One specific story of what's broken or missing today, from a
   real user or ticket. Not a solution in disguise.
2. **Appetite.** How much time this is worth: a small batch (days to two
   weeks) or a big batch (a full cycle). It is a fixed limit, not an estimate;
   the solution must fit it. Default to the smaller one.
3. **Elements.** Rough out the solution:
   - Flows and interactions: a **breadboard** in text. Places underlined (or
     `## Place`), affordances listed under each, arrows for connections.
   - Layout or physical form: a **fat-marker sketch**. Ask the user to attach a
     photo or sketch, or draw a rough one, then run `/visual-refine` at shaping
     fidelity.
   - Firmware or hardware: a block diagram of parts and signals, at the same
     roughness.
   Explore two or three alternatives before settling.
4. **Rabbit holes.** Walk the solution slowly and list every unknown,
   technical risk or edge case that could blow the appetite. For each: patch
   it with a decision, cut it, or mark it as a spike. Check doubtful technical
   claims now (`/verify-reality`, `/prototype`).
5. **No-gos.** What this deliberately won't do.
6. **Write the pitch** from `${CLAUDE_SKILL_DIR}/templates/pitch.md` to
   `docs/pitches/<slug>.md`, with the refined visuals beside it, and post it
   with `/tracker-sync`.
7. Shaping ends at the pitch. Whether to build it is decided at the betting
   table (`/betting-table`), not here.

Pair with `/grill-with-docs` to stress the pitch and record CONTEXT.md terms
and ADRs as they come up.
