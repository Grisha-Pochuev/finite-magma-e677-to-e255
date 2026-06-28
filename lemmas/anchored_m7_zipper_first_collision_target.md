# Anchored-M7 Zipper First-Collision Target

Date: 2026-06-25.

Status:

```text
target / next exact split after cycle zipper lemma
```

## Starting Point

Use:

```text
anchored_m7_cycle_zipper_lemma.md
```

The clean self-repeat is now a cyclic zipper:

```text
r_i*h=r_{i+1},
I_i=h*(r_{i+1}*r_i)=(r_{i-1}*r_i)*r_{i-1},
I_i -> r_{i+1} in H_h.
```

The chosen cycle is first clean self-repeat, so the source rows:

```text
r_0,r_1,...,r_{n-1}
```

are distinct before returning to `r_0`.

## Immediate Routed Collisions

For two different positions `i!=j`, compare the two `H_h` edges:

```text
I_i -> r_{i+1},
I_j -> r_{j+1}.
```

If:

```text
I_i=I_j,
```

then outputs are distinct by first self-repeat minimality, so `H_h` has an
outgoing fan.

If:

```text
r_{i+1}=r_{j+1},
```

then the source cycle has an earlier repeat, impossible in the clean first
self-repeat segment unless it is the chosen return.

If:

```text
I_i=r_{j+1}
or
I_j=r_{i+1},
```

then the two `H_h` edges concatenate into an actual directed path in `H_h`.

Thus all input repeats, output repeats, and input-output hits are routed by:

```text
same_target_pair_collision_trichotomy_lemma.md
anchored_m7_first_event_routing_lemma.md
```

## Clean Residual

The live clean zipper residual has:

```text
all source rows r_i distinct,
all outputs r_{i+1} distinct,
all inputs I_i distinct,
no input-output hit between any I_i and any r_j,
no watched/core hit.
```

So the `H_h` edges:

```text
I_i -> r_{i+1}
```

form a clean matching around the right-`h` source cycle.

## Next Proof Target

Prove that this clean matching plus the zipper equations:

```text
I_i=h*(r_{i+1}*r_i)=(r_{i-1}*r_i)*r_{i-1}
```

creates strict clean theta in `H_h`, or regenerates anchored-X3 with a smaller
M7 rank.

Equivalently, rule out a fully clean cyclic zipper matching.

## Do Not Repeat

Do not test only local endpoint equalities such as:

```text
im1=r1,
i0=rm1,
i0=im1.
```

The bounded diagnostic already found no such short collapse:

```text
anchored_m7_cycle_end_saturation_diagnostic.md
```
