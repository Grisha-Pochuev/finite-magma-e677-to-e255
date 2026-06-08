# Agent Instructions

This repository studies the finite-magma problem

```text
E677: x = y * (x * ((y * x) * y))
E255: x = ((x*x)*x)*x.
```

The goal is to determine whether `E677` implies `E255` in all finite magmas.

## Working principles

Use mathematical reasoning first.  Computation should support structural
understanding, not replace it.

Preferred workflow:

1. read `docs/CURRENT_FRONTIER.md`;
2. read `docs/LEMMA_STATUS.md`;
3. work on one current frontier only;
4. formulate one structural question before computing;
5. run only bounded, interpretable checks;
6. immediately translate computational results into a lemma, caveat, or status
   update.

## Computation discipline

Do not run or request broad brute-force searches merely to see what happens.

A useful computation should have a clear interpretation before it starts, such
as:

```text
this rejects a fixed structural role
this confirms a listed finite split
this checks a proposed forced cell
this reproduces a recorded closure
```

For user-side computation, prefer short scripts with clear stop rules.

## Public writing style

All public repository files should be in English.

When recording a result, distinguish:

```text
proved
recorded closed
reproducible checkpoint
candidate
diagnostic only
```

Do not claim the full theorem is proved unless the proof is actually complete.

## Current continuation point

Start from:

```text
docs/CURRENT_FRONTIER.md
docs/RESEARCH_UPDATE_2026-06-08.md
lemmas/fan_tip_bridge_expansion_lemma.md
lemmas/fan_bridge_zipper_extension_lemma.md
lemmas/terminal_source_anchored_fan_lemma.md
lemmas/three_source_good_six_pressure_candidate.md
```

The No-Free-Tail Lemma remains unproved.  Do not start another broad search.
The next task is a symbolic classification of the first intersection among
the three bridge paths.
