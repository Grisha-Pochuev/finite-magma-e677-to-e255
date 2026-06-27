# Y3 Three-Cycle First-Intersection Boundary

Date: 2026-06-19.

Status:

```text
boundary / early intersections in Y3 are routed; only clean disjoint cycle shell remains
```

## Purpose

This continues:

```text
clean_external_bridge_seventh_stage_reduction_lemma.md
source_successor_eventual_predecessor_hit_lemma.md
```

The Y3 residual is no longer an open three-edge matching.  It is a comparison
of three finite source-row cycles through the same generated input `A_j`.

This file records the exact first-intersection split.  It prevents the next
run from reopening X3 from scratch.

## Y3 Cycle Notation

Use the clean X3/Y3 normal form:

```text
row p:   P      -> A_j -> S,
row x_j: Beta_j -> A_j -> b,
row b:   H_j    -> A_j -> D_j,
```

where:

```text
p notin {x_j,b},
D_j=b*A_j.
```

Define forward cycles from the common input `A_j`:

```text
C_p^0=A_j,   C_p^1=S,   C_p^{m+1}=p*C_p^m,
C_x^0=A_j,   C_x^1=b,   C_x^2=x_{j+1},   C_x^{m+1}=x_j*C_x^m,
C_b^0=A_j,   C_b^1=D_j, C_b^{m+1}=b*C_b^m.
```

By the predecessor-hit lemma, each cycle returns through its named predecessor:

```text
C_p^{L_p-1}=P,       C_p^{L_p}=A_j,
C_x^{L_x-1}=Beta_j,  C_x^{L_x}=A_j,
C_b^{L_b-1}=H_j,     C_b^{L_b}=A_j.
```

## First Event

Scan the three cycles after the local Y3 data:

```text
P -> A_j -> S,
Beta_j -> A_j -> b -> x_{j+1},
H_j -> A_j -> D_j.
```

The first nonlocal event is one of:

```text
1. a cycle vertex hits the visible crossed-fan/core footprint;
2. a cycle vertex hits a generated A/X/H/Beta layer outside its own local role;
3. two different source cycles meet at the same vertex;
4. one cycle returns to its own predecessor before any cross-hit;
5. all three cycles remain pairwise disjoint until their own predecessor returns.
```

Cases 1 and 2 are routed by the existing visible/generated hit maps.

Case 4 is a same-row recurrence boundary for the corresponding row.  For row
`b`, the return is already controlled by:

```text
row_b_successor_eventual_h_hit_lemma.md
row_b_successor_h_hit_role_lemma.md
```

## Cross-Hit Routing

Suppose two different Y3 cycles first meet at a fresh vertex `z`:

```text
C_r^m=z=C_s^n,
r!=s,
```

where `r,s` are chosen from:

```text
p, x_j, b.
```

Then both rows are defined at the same input `z`:

```text
r*z=C_r^{m+1},
s*z=C_s^{n+1}.
```

If the two outputs are different, this is a same-input split:

```text
r*z != s*z.
```

It is routed by:

```text
same_input_lift_target_advance_lemma.md
```

which lifts the split to a same-target pair in `H_z` and then advances it
back to a two-target common-input bridge.

If the two outputs are equal, the target-lift to `H_z` gives two same-target
edges with the same output.  Then:

```text
same_target_pair_collision_trichotomy_lemma.md
```

routes the pair as:

```text
same full ported interval -> source-row collision;
same output               -> incoming fan in H_z;
input-output cross hit     -> directed H_z path;
otherwise                 -> clean same-target pair already covered by the
                             U/V/W/X reductions.
```

Thus a fresh cross-hit between two Y3 cycles is not a new residual.

## Remaining Clean Shell

After routing first hits, the only genuinely new Y3 remainder is:

```text
Z3. clean disjoint three-cycle shell at A_j.
```

It consists of three finite simple row cycles through the common vertex `A_j`:

```text
A_j -> S -> ... -> P -> A_j          under row p,
A_j -> b -> x_{j+1} -> ... -> Beta_j -> A_j  under row x_j,
A_j -> D_j -> ... -> H_j -> A_j      under row b,
```

with no cross-hit between the three cycles before the three predecessor
returns and no hit to the watched generated/visible footprint except for the
named local vertices.

This is now the exact Y3 residual.  The next useful target is not another
local collision split.  It is to compare the three predecessor-return steps:

```text
P      -> A_j,
Beta_j -> A_j,
H_j    -> A_j,
```

or the three first successor steps:

```text
A_j -> S,
A_j -> b,
A_j -> D_j,
```

as one clean three-cycle shell.
