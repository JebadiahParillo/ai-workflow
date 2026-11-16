---
name: visual-refine
description: Turn a visual a person attaches (a fat-marker sketch, whiteboard photo, breadboard, wiring sketch, marked-up screenshot, photo of a part or a print, a bug screenshot) into a clean, editable version at the right fidelity, then loop on their markup. Use whenever the user attaches or pastes an image, sketch or diagram to shape, specify, build or report something.
---

# Visual refine

The person draws; Claude reads, restates, cleans up and asks. The person's
markup on each round is the authority.

1. **Read it back.** Describe what you see in plain words: each element, label,
   arrow and number, and anything you can't read. Ask about the unreadable or
   ambiguous parts before redrawing. Never invent a value the sketch didn't
   give; mark it `?`.
2. **Pick the fidelity for the stage.**
   - Shaping: stay rough. Breadboard as text or a simple diagram; layout as a
     fat-marker style SVG (thick strokes, no styling, no real copy). Don't add
     detail the sketch didn't decide.
   - Spec and build: exact where it matters (dimensions, pin numbers, states),
     still no decoration.
   - Bug report: annotate the screenshot (what's wrong, what's expected).
3. **Pick the form.**
   - A diagram that lives with the code (flows, state machines, wiring, block
     diagrams): SVG or Mermaid in `docs/` next to the pitch or spec.
   - Boxes and arrows to rearrange with others: a Whiteboard artifact.
   - Screens to iterate on visually: a Design artifact.
   - Parts and dimensions: a dimensioned sketch plus the parameters it feeds.
4. **Keep the original.** Save the attachment beside the refined version
   (`<name>.orig.jpg` next to `<name>.svg`) so changes can be checked against
   it.
5. **Loop.** Send the refined version and ask the person to mark it up (draw
   on it, or list changes). Apply only what they marked. Stop when they say
   it matches.
6. **Attach** the final version and the original to the pitch, spec or ticket
   with `/tracker-sync`, and reference it from the docs.
7. Check the result renders: for SVG, render it to PNG (`rsvg-convert`) and
   look at it before sending.
