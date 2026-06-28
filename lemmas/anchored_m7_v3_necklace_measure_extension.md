# Anchored-M7 V3 Necklace Measure Extension

Date: 2026-06-25.

Status:

```text
measure extension candidate / exact admissibility gap for coupled zipper bridge
```

## Purpose

This file is now the anchored specialization of the target-independent
measure boundary:

```text
fixed_target_zipper_reduces_to_v3_admissibility.md
```

It extends:

```text
relay_minimality_measure_candidate.md
anchored_x3_rank_measure_candidate.md
general_v3_bridge_descent_boundary.md
```

to the current residual:

```text
anchored_m7_clean_v3_necklace_obstruction.md
anchored_m7_coupled_zipper_bridge_residual.md
```

The existing V3 measure `M5/M6` was designed for a clean V3 bridge born at a
first extra intersection of two row cycles.  The current V3 necklace is
different: it is born inside the first self-repeat cycle of one anchored
right-`h` source orbit.

## Current Measure Components

Already named:

```text
M5. first-extra offset;
M6. clean V3 bridge rank at that first-extra intersection;
M7. anchored-X3 source-orbit first-event rank.
```

The live anchored branch has:

```text
M7 = n,
```

where:

```text
r_0*h=r_1,
...
r_{n-1}*h=r_0
```

is the first clean same-orbit self-repeat.

## New Subrank

Add:

```text
M8. anchored V3 necklace bridge rank:
    the first position i<n at which the M7 self-repeat cycle produces a
    clean adjacent V3 bridge

        H_{r_i}:     h -> A_i,
        H_{r_{i+1}}: h -> A_{i+1},

    with A_i=r_{i-1}*r_i and A_{i+1}=r_i*r_{i+1}.
```

If any adjacent bridge is not clean, it routes by:

```text
anchored_m7_zipper_first_collision_target.md
anchored_m7_zipper_target_advance_lemma.md
same_input_lift_target_advance_lemma.md
general_v3_bridge_descent_boundary.md
```

So `M8` is only needed for the fully clean necklace.

## Why It Should Be Smaller

The original terminal event is the return:

```text
r_n=r_0.
```

Every adjacent V3 bridge in the necklace is born at a position:

```text
i<n.
```

Therefore, if an adjacent V3 bridge is admissible as a relay object of the
same global kind, it should be smaller than the terminal M7 self-repeat:

```text
M8 < M7.
```

This is the expected descent:

```text
anchored false branch
  -> clean M7 self-repeat at rank n
  -> adjacent clean V3 bridge at rank i<n
  -> smaller measured relay object.
```

## Exact Admissibility Gap

The proof still needs one sentence:

```text
An adjacent clean V3 bridge born inside the anchored M7 self-repeat cycle is
admissible as a relay object under the same global minimality measure.
```

This is not automatic from `general_v3_bridge_descent_boundary.md`, because
that file treats V3 bridges born at first-extra intersections, not V3 bridges
born inside one anchored self-repeat cycle.

In the unified language, this is the target-independent sentence:

```text
A zipper-born clean adjacent V3 bridge is admissible under the same global
minimality measure as first-extra V3 bridges.
```

## If Admissibility Fails

If the bridge is not admissible, the exact obstruction is:

```text
a closed clean V3 necklace at one common input h,
whose every adjacent bridge is locally clean,
but which cannot be inserted into the global relay measure as a smaller
object.
```

This obstruction is recorded in:

```text
anchored_m7_clean_v3_necklace_obstruction.md
```

## Next Proof Target

Prove the admissibility sentence above, or identify the missing hypothesis.

The likely missing hypothesis is one of:

```text
1. the bridge must attach to old/core data;
2. the bridge must repeat a full ported interval in an independent role;
3. the bridge must regenerate a standard anchored-X3 triple, not just a V3
   pair;
4. the fully clean necklace itself creates strict clean theta.
```
