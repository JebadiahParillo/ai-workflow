---
name: hardware-loop
description: Workflow for physical parts made by parametric CAD scripts (3D-printed enclosures, holders, mounts). Covers measuring before modelling, a fit check for every option, printing a test piece first, a planned print-feedback ticket, and turning feedback into parameters. Use when a feature has a printed or fabricated part.
---

# Hardware loop

1. Measure the real parts and record the source of each number (datasheet, listing, calipers). Real boards may have rounded corners where the drawing shows chamfers, so design stops and fits that don't depend on corner shape.
2. Keep every dimension a parameter with a sensible default. Defaults follow the parts actually linked.
3. Run the fit and clearance check for every option you document, in one script call.
4. Print the smallest test piece first (threads, snap fits) before the full part.
5. Plan a "first print feedback" ticket. Turn each piece of feedback into a parameter or a test, then regenerate.
6. Smoke-test the generated files headless, printing only failures.
