# General V3 Bridge Descent Boundary

Date: 2026-06-20.

Status:

```text
boundary / exact descent obligation for the first-extra clean bridge
```

## Purpose

This refines the remaining clean branch from:

```text
clean_first_extra_matching_bridge_alignment.md
```

The clean first-extra matching is not a new same-row recurrence.  After target
advance it is a general V3-type same-input two-target bridge.  This file
records the exact descent/admissibility obligation left by that bridge.

## Setup

Rows `p,q` share a target-advance step:

```text
p*b=z,
q*b=z,
p!=q.
```

Their row cycles meet again for the first time at:

```text
w=x_i=y_j,
i,j > 1.
```

The first-extra matching in `H_w` is clean-disjoint:

```text
x_{i-1} -> x_{i+1}   carried by row p,
y_{j-1} -> y_{j+1}   carried by row q.
```

Target advance gives the V3-type bridge:

```text
H_{x_{i+1}}:  w -> x_{i+2}   carried by row p,
H_{y_{j+1}}:  w -> y_{j+2}   carried by row q.
```

The common input is the first extra intersection `w`.

## Immediate Hit Roles

The V3 bridge is not clean if any of the following happens:

```text
1. x_{i+1}=y_{j+1}
   -> same-output fan at the first extra intersection in H_w;

2. x_{i+2}=y_{j+2}
   -> same-output fan after target advance;

3. x_{i+1}=y_{j+2} or y_{j+1}=x_{i+2}
   -> directed path/cross-hit after target advance;

4. the full interval repeats in two active branch roles
   -> source reconstruction collision;

5. w, x_{i+1}, y_{j+1}, x_{i+2}, or y_{j+2}
   hits the old visible/core footprint
   -> ordinary relay/core attachment.
```

These roles are already routed by:

```text
same_target_pair_collision_trichotomy_lemma.md
same_input_lift_target_advance_lemma.md
minimal_g12_loop_normal_form_boundary.md
```

## Clean Residual

If none of the immediate hit roles occurs, the exact remaining object is:

```text
a clean same-input two-target bridge
with common input equal to the first extra row-orbit intersection.
```

It is clean in the following sense:

```text
x_{i+1} != y_{j+1},
x_{i+2} != y_{j+2},
x_{i+1} != y_{j+2},
y_{j+1} != x_{i+2},
```

and none of its displayed vertices is a watched old/core vertex.

## Descent Measure Needed

The current global measure:

```text
M0-M4 in relay_minimality_measure_candidate.md
```

does not yet name this object explicitly.

The natural extension is:

```text
M5. first-extra offset:
    the first position i>1 at which the two active same-row target-advance
    cycles meet again after their shared step;

M6. clean V3 bridge rank:
    the first clean same-input two-target bridge born at that first extra
    intersection.
```

The desired descent sentence is:

```text
In a minimal G12 loop, a clean V3 bridge born at the first extra intersection
is admissible as a smaller measured relay object unless it creates an
immediate hit role listed above.
```

Equivalently, if the bridge cannot be measured as smaller, then the first
extra intersection must already produce the M496-like same-output fan pattern:

```text
x_{i+1}=y_{j+1}.
```

## Current Boundary

This file does not prove the desired descent sentence.

It isolates the remaining proof obligation:

```text
clean first-extra matching
-> general V3 bridge at the first extra intersection
-> prove smaller measured relay, or force same-output fan / collision / core hit.
```

## Anchored-M7 Update

The anchored-M7 clean self-repeat residual now also reduces to clean V3
admissibility:

```text
anchored_m7_reduces_to_general_v3_admissibility.md
```

There the V3 bridge is not born at a first-extra intersection.  It is born
inside the first anchored right-`h` self-repeat cycle:

```text
H_{r_i}:     h -> A_i,
H_{r_{i+1}}: h -> A_{i+1}.
```

So the remaining global target should be stated in the unified form:

```text
Clean same-input two-target bridge admissibility:
any clean V3 bridge born before the current terminal event is either locally
routed or admissible as a smaller measured relay object.
```

This unified statement would cover both the first-extra V3 bridge and the
anchored-M7 V3 necklace.
