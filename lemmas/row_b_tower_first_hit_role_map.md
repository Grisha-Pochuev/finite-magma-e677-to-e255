# Row-b Tower First-Hit Role Map

Date: 2026-06-18.

Status:

```text
proved role map / routing target, not contradiction
```

## Purpose

This file classifies what the first nonfresh hit of the row-`b` predecessor
tower means in the clean ported-matching residual.

It continues:

```text
clean_ported_matching_predecessor_layer_boundary.md
row_b_predecessor_tower_dichotomy_boundary.md
```

## Setup

Use the clean ported-matching residual:

```text
x_{i+1}=x_i*b,
A_i=pred_{x_i}(b),
H_i=pred_b(A_i)=x_{i+1}*x_i.
```

So:

```text
x_i*A_i=b,
x_i*b=x_{i+1},
b*H_i=A_i.
```

The generated `H_b` footprint is a matching:

```text
A_i -> x_{i+1}.
```

The row-`b` predecessor layer is:

```text
H_i -> A_i.
```

Assume visible hits, generated `A`-repeats, generated `X`-repeats, and
generated `A-X` hits have already been routed.

## Hit Type 1: `H_i=A_j`

If:

```text
H_i=A_j,
```

then row `b` contains:

```text
b*A_j=A_i.
```

But for the generated edge indexed by `j`, row `b` also contains:

```text
b*H_j=A_j.
```

Therefore the first hit into the generated `A`-layer creates a genuine
two-step row-`b` chain:

```text
H_j -> A_j -> A_i
```

inside the predecessor tower.

This is not a contradiction by itself.  It means that the tower of `A_i` has
hit another generated input `A_j`.  In the tower notation:

```text
B_i^1=A_j.
```

So this role is exactly an unequal-depth tower collision:

```text
the predecessor tower of A_i enters the generated input A_j.
```

It should be routed as a row-`b` tower cross-hit, not as an `H_b` path.

## Hit Type 2: `H_i=x_j`

If:

```text
H_i=x_j,
```

then row `b` contains:

```text
b*x_j=A_i.
```

At the same orbit label, row `x_j` contains the ported interval:

```text
x_j*A_j=b,
x_j*b=x_{j+1}.
```

Thus the row-`b` predecessor tower has hit a source/orbit label, not a
generated `H_b` input.

The hit creates a two-row local configuration:

```text
row b:   x_j -> A_i
row x_j: A_j -> b -> x_{j+1}
```

This is also not a contradiction by itself.  It is a target-changing
configuration: row `b` now carries a full ported interval for target `A_i`:

```text
(A_i, x_j, b*A_i).
```

The next route should compare this target-`A_i` interval with the old
target-`b` interval carried by row `x_j`:

```text
(b,A_j,x_{j+1}).
```

So this role belongs to a two-target bridge/target-swap analysis.

## Hit Type 3: `H_i` In Visible Footprint

If:

```text
H_i in {a,b,c,d,u,v,h,k,t,ell}
```

or in any explicitly retained core/corridor footprint, then the row-`b`
predecessor tower attaches to the visible crossed-fan skeleton.

This is the desired core-attachment kind of event.  It should be routed by the
specific visible vertex hit, using the existing row-a bridge and crossed-fan
case files.

## Hit Type 4: `H_i=A_i`

This is the row-`b` fixed point boundary:

```text
b*A_i=A_i.
```

It is already listed in:

```text
right_b_orbit_local_repeat_roles.md
```

It is not a right fixer of the bad target `b`; it is a fixed point of row
`b` away from `b`.

## Clean Continuation

If none of these hit types occurs, then the row-`b` predecessor tower extends
one step backward:

```text
B_i^2=pred_b(H_i),
b*B_i^2=H_i.
```

The first later hit is classified by the same role map with `B_i^m` in place
of `H_i`.

## Consequence

The first-hit problem is now split into:

```text
1. A-layer hit: row-b tower cross-hit H_j -> A_j -> A_i;
2. X-layer hit: two-target bridge involving rows b and x_j;
3. visible hit: core attachment;
4. fixed point: row-b cycle boundary;
5. no hit: extend the row-b predecessor tower.
```

The next useful proof target is to route Type 1 and Type 2.  They are the
only first-hit roles that are neither immediate visible attachment nor pure
row-`b` cycle boundary.
