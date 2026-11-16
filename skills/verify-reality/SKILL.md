---
name: verify-reality
description: Check every external fact a spec depends on (links, product listings, sizes, prices, versions, API behaviour) against primary sources, and record the results with a date in the spec. Use after /to-spec and before /implement, or when a spec cites outside facts.
---

# Verify reality

1. List the spec's external facts: each URL, part, dimension, version or API claim.
2. Check each one against its primary source. Use one cheap subagent (Haiku) for the fetching. Read page text or run a small JS extraction, never screenshots, and batch the reads.
3. Run the project's own checks on every option (fit scripts, compatibility tests), in one scripted call.
4. Add a "Verified on <date>" list to the spec issue: what was checked, the result, and anything that changed a default.
5. Report only the mismatches.
