---
name: hardware-loop
description: Workflow for physical and embedded work. Covers parametric CAD parts (measure first, fit check every option, test piece first, print-feedback ticket) and firmware (build, flash and an on-target hardware-in-the-loop test as the done check, reserved resources recorded, flashing gated). Use when a feature has a printed or fabricated part, or firmware that runs on a board.
---

# Hardware loop

## Printed and fabricated parts

1. Measure the real parts and record the source of each number (datasheet,
   listing, calipers). Real boards may have rounded corners where the drawing
   shows chamfers, so design stops and fits that don't depend on corner shape.
2. Every dimension is a parameter with a sensible default. Defaults follow the
   parts actually linked.
3. Run the fit and clearance check for every option you document, in one
   script call.
4. Print the smallest test piece first (threads, snap fits) before the full
   part.
5. Plan a "first print feedback" ticket. Turn each piece of feedback into a
   parameter or a test, then regenerate.
6. Smoke-test the generated files headless, printing only failures.

## Firmware

1. CLAUDE.md lists the build, flash and test commands, the target, and the
   board's reserved resources (timers, pins, DMA channels, flash regions) that
   generated code must not touch.
2. Host-side unit tests for logic that doesn't need the board; they run in
   `scripts/check --quick`.
3. A hardware-in-the-loop test is the done check for anything that touches the
   board: build, flash, drive the inputs (serial, USB HID, GPIO), read back
   what the board did, compare. It prints only failures. It runs in
   `scripts/check` (full) when a board is attached.
4. Flashing is an `ask` permission when the board drives motors, heaters or
   anything that moves. Hardware with safety functions is never flashed by an
   unattended run.
5. Paste compiler and fault output verbatim; for a hard fault, capture
   registers and the stack before guessing.
6. Record every board-only bug as a test (host or HIL) before fixing it.
