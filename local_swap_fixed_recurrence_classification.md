# Local Swap/Fixed Recurrence Classification

Date: 2026-06-19.

Status:

```text
boundary / classifies R-a, R-b1, R-b2, R-b3 local recurrence cases
```

## Purpose

This treats the small local recurrence cases left in:

```text
same_row_recurrence_inventory.md
```

after R-b4/R-b5/R-x/R-Z were absorbed:

```text
R-a, R-b1, R-b2, R-b3.
```

These cases are not fresh bridge layers.  They are local swap/fixed
recurrences attached to visible or generated vertices.

## General Swap Form

Assume one row `r` swaps a target `T` with a vertex `u`:

```text
r*u=T,
r*T=u.
```

Then in `H_T`, row `r` gives a loop:

```text
u -> u.
```

Target advance gives the two-state same-row recurrence:

```text
(T,u,u) -> (u,T,T) -> (T,u,u).
```

So a swap recurrence is exactly a target-swap loop, not a fresh external
bridge.

## R-a

R-a has:

```text
a*k=b,
a*b=k.
```

Thus row `a` swaps:

```text
b <-> k.
```

The vertex `k` is visible:

```text
k=pred_a(b)
```

from the original crossed-fan data.  Therefore R-a is a visible target-swap
loop:

```text
(b,k,k) <-> (k,b,b).
```

It is not an independent clean residual.

## R-b1

R-b1 has:

```text
A_i=x_{i+1},
x_i*A_i=b,
x_i*b=x_{i+1}.
```

Therefore row `x_i` swaps:

```text
b <-> x_{i+1}.
```

The swapped vertex `x_{i+1}` is in the generated X-layer.  So R-b1 is the
generated analogue of R-a:

```text
(b,x_{i+1},x_{i+1})
  <-> (x_{i+1},b,b).
```

It is a generated target-swap loop, not a fresh clean external bridge.

## R-b2

R-b2 has:

```text
x_i*b=x_i,
x_i!=b.
```

This is a fixed point of right multiplication by `b`, not a right fixer of
the bad target `b`.

However it is attached to the generated ported interval:

```text
x_i*A_i=b,
x_i*b=x_i.
```

So in `H_b` row `x_i` gives:

```text
A_i -> x_i.
```

This is an A-X hit in the generated `H_b` footprint, hence belongs to:

```text
ported_cycle_hb_footprint_trichotomy_lemma.md
```

It is routed as generated path/fan attachment, not as an independent
recurrence.

## R-b3

R-b3 has:

```text
H_i=A_i,
b*A_i=A_i.
```

This is a row-`b` fixed point at a generated input `A_i`.

It is not a right fixer for `b`, but it is attached to the unavoidable
row-b/generated bridge:

```text
row b:   A_i -> A_i,
row x_i: A_i -> b.
```

So R-b3 is the fixed-point branch of the base bridge at `A_i`.

The bad-target no-predecessor-output lemma also gives:

```text
A_i*b != A_i,
```

so the fixed point is one-sided: row `b` fixes `A_i`, but right multiplication
by `b` does not fix `A_i`.

Thus R-b3 should be treated as a base-bridge fixed-point boundary, not as a
new external bridge.

## Consequence

The local recurrence cases reduce as follows:

```text
R-a  -> visible target-swap loop;
R-b1 -> generated target-swap loop / A-X footprint hit;
R-b2 -> generated A-X footprint hit;
R-b3 -> base row-b/generated bridge fixed-point boundary.
```

None of these is an independent fresh residual.  The remaining obstruction is
the global same-row recurrence/minimal relay descent, where target-swap loops
must either hit the visible core, repeat a full ported interval in an
independent role, or fit into the global relay-cycle minimality measure.

