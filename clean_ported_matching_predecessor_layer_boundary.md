# Clean Ported-Matching Predecessor-Layer Boundary

Date: 2026-06-18.

Status:

```text
proved normal form / remaining boundary after H_b footprint trichotomy
```

## Purpose

After the generated `H_b` footprint trichotomy, the hardest residual is the
case where the ported-transition cycle produces no internal `H_b`
concatenation and no generated outgoing fan.

This file records the exact normal form of that residual, including the
row-`b` predecessor layer.

References:

```text
ported_cycle_hb_footprint_trichotomy_lemma.md
bad_target_right_b_orbit_predecessor_recursion_lemma.md
```

## Setup

Fix a bad target `b`.  Let:

```text
x_{i+1}=x_i*b,
A_i=pred_{x_i}(b),
H_i=x_{i+1}*x_i=pred_b(A_i).
```

Thus:

```text
x_i*A_i=b,
x_i*b=x_{i+1},
b*H_i=A_i.
```

The generated `H_b` edge is:

```text
A_i -> x_{i+1}.
```

## Clean Ported-Matching Assumption

After routing visible hits and applying the footprint trichotomy, the clean
ported-matching residual assumes:

```text
1. the orbit labels x_i on the chosen cycle are pairwise distinct;
2. the inputs A_i are pairwise distinct;
3. no A_i equals any orbit label x_j;
4. no A_i, x_i, or x_{i+1} lies in the visible crossed-fan footprint;
5. local repeat roles A_i=x_{i+1}, A_i=x_i, x_{i+1}=x_i are routed out.
```

Then the generated `H_b` footprint is exactly a matching:

```text
A_i -> x_{i+1}.
```

It has:

```text
no generated H_b path concatenation,
no generated outgoing fan,
and no visible-footprint hit.
```

## Predecessor Layer

The same data also creates row-`b` predecessor arrows:

```text
H_i -> A_i
```

meaning:

```text
b*H_i=A_i.
```

Because row `b` is a function and a permutation:

```text
H_i=H_j  <=>  A_i=A_j.
```

Indeed:

```text
H_i=H_j => b*H_i=b*H_j => A_i=A_j,
```

and conversely, if `A_i=A_j`, then both `H_i,H_j` are the unique row-`b`
predecessor of the same element.

Therefore, in the clean ported-matching residual where the `A_i` are pairwise
distinct, the `H_i` are pairwise distinct too.

## Remaining Hit Types

After this normal form, the next nonfresh event in the predecessor layer is
one of:

```text
H_i in {x_j}       -> row-b predecessor layer hits an orbit/output label;
H_i in {A_j}       -> row-b predecessor layer links two generated H_b inputs;
H_i in visible     -> visible bridge/predecessor hit;
H_i=A_i            -> row-b fixed point boundary;
H_i fresh          -> two-layer matching extends one step backward.
```

The local case:

```text
H_i=A_i
```

is already listed in:

```text
right_b_orbit_local_repeat_roles.md
```

as the row-`b` fixed point boundary.

## Consequence

The remaining hard branch is not merely:

```text
a closed right-b orbit.
```

It is the sharper two-layer object:

```text
H_i --row b--> A_i --H_b edge/source x_i--> x_{i+1},
```

where the second layer is a clean matching and the first layer is also fresh
unless it hits:

```text
the orbit labels,
the generated H_b inputs,
the visible crossed-fan footprint,
or a row-b fixed point.
```

The next useful proof should classify the first nonfresh hit of the
predecessor layer.  If no such hit occurs immediately, iterate the predecessor
layer backward in row `b`; finiteness then forces a row-`b` cycle boundary,
not an immediate contradiction.
