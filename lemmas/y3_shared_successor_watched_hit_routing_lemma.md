# Y3 Shared-Successor Watched-Hit Routing Lemma

Date: 2026-06-19.

Status:

```text
proved routing / watched hits of U=p*S and V=S*A_j are not new residuals
```

## Purpose

This treats case 1 from:

```text
y3_shared_successor_square_boundary.md
```

The Z3 square has:

```text
p*A_j=S,
U=p*S,
V=S*A_j,
S*(U*p)=A_j.
```

This file records what happens if `U` or `V` hits the local watched shell:

```text
A_j, P, S, Beta_j, b, x_{j+1}, H_j, D_j.
```

## Hits Of V=S*A_j

The value `V` is the output of row `S` at the common input `A_j`.

### V=b

Rows `S` and `x_j` share:

```text
A_j -> b.
```

If their next outputs at `b` also agree, the full ported interval forces:

```text
S=x_j.
```

Otherwise this is a common-edge divergence / outgoing fan at the generated
input `A_j`, routed by the same machinery as the base row-b/generated bridge.

### V=D_j

Rows `S` and `b` share:

```text
A_j -> D_j.
```

Again, equal continuation gives source-row collision; unequal continuation is
a common-edge divergence attached to the row-b/generated bridge.

### V=S

This is a right-`A_j` fixed point for the source row `S`:

```text
S*A_j=S.
```

It is a fixed-target source recurrence boundary.

### V=p or V=x_j

The source-successor orbit from `p` has hit one of the source rows already in
the Z3 shell.  This is routed by:

```text
fixed_target_source_orbit_first_merge_boundary.md
```

as a source hit in `H_{A_j}`.

### V=A_j, P, Beta_j, H_j, or x_{j+1}

These are watched generated/left-cycle hits.  They route by the corresponding
first-hit role:

```text
same-input split,
same-target pair,
directed H-path,
or same-row recurrence.
```

No such hit is a new clean Z3 residual.

## Hits Of U=p*S

The value `U` is the next point on the left row-`p` cycle:

```text
A_j -> S -> U.
```

### U=A_j

Row `p` has a two-cycle:

```text
A_j -> S -> A_j.
```

This is a same-row recurrence boundary for row `p`.

### U=P

The row-`p` cycle returns to the predecessor of `A_j`:

```text
P -> A_j -> S -> ... -> P -> A_j.
```

This is the expected finite row-`p` return and belongs to the same-row
recurrence side of Z1 unless it cross-hits another watched layer earlier.

### U=b or U=D_j

The left row-`p` cycle hits the generated source orbit:

```text
x_j -> b -> D_j -> ...
```

This is a cross-hit between the left row-`p` cycle and the generated
source-successor orbit, hence routed by:

```text
y3_three_cycle_first_intersection_boundary.md
fixed_target_source_orbit_first_merge_boundary.md
```

### U=S

Row `p` has:

```text
p*A_j=S,
p*S=S.
```

This is a row-`p` fixed-output recurrence boundary attached to the Z3 shell.

### U=Beta_j, H_j, or x_{j+1}

These are generated predecessor/successor layer hits.  They route by the
existing beta/H/X first-hit maps and do not create a new square residual.

## Clean Square Residual

After this routing, the genuinely clean shared-successor square may assume:

```text
U,V are fresh relative to
{A_j, P, S, Beta_j, b, x_{j+1}, H_j, D_j},
```

except for the separately handled convergence branch:

```text
U=V,
```

which is routed by:

```text
y3_commuting_second_step_reduction_lemma.md
```
