# Beta-Anchor Row-b Partner Reduction Lemma

Date: 2026-06-18.

Status:

```text
proved reduction / V4 beta anchor always has row-b same-target partner
```

## Purpose

This sharpens V4:

```text
beta-anchored reversible square.
```

The beta-anchored edge:

```text
Beta_j -> b in H_{A_j}
```

is never isolated.  Row `b` always contributes another edge in the same target
graph `H_{A_j}`.

## Setup

Use:

```text
x_j*A_j=b,
x_j*b=x_{j+1},
Beta_j=pred_{x_j}(A_j),
H_j=pred_b(A_j).
```

So:

```text
x_j*Beta_j=A_j,
x_j*A_j=b,
b*H_j=A_j.
```

Define:

```text
D_j=b*A_j.
```

## Same-Target Partner

The beta anchor gives in `H_{A_j}`:

```text
Beta_j -> b       carried by row x_j.
```

Row `b` gives in the same target `H_{A_j}`:

```text
H_j -> D_j        carried by row b.
```

Equivalently:

```text
x_j*Beta_j=A_j,
x_j*A_j=b,

b*H_j=A_j,
b*A_j=D_j.
```

Thus every V4 beta anchor contains the same-target pair:

```text
H_{A_j}:  Beta_j -> b,
          H_j    -> D_j.
```

## Collision Routing

Apply:

```text
same_target_pair_collision_trichotomy_lemma.md
```

to the pair:

```text
Beta_j -> b,
H_j    -> D_j.
```

The useful local roles are:

```text
Beta_j=H_j      -> outgoing fan in H_{A_j}
                   and the shared-edge divergence branch;

D_j=b           -> incoming fan in H_{A_j}
                   unless the full interval also repeats;

Beta_j=D_j      -> path concatenation H_j -> D_j=Beta_j -> b;

H_j=b           -> path concatenation Beta_j -> b=H_j -> D_j.
```

If both input and output coincide:

```text
Beta_j=H_j and D_j=b,
```

then rows `x_j` and `b` realize the same full ported interval:

```text
(A_j,H_j,b),
```

so:

```text
x_j=b,
```

by ported interval reconstruction.  This is excluded in the clean bad-target
right-`b` orbit.

## Clean-Disjoint Advance

If the pair is clean-disjoint, target advance gives:

```text
(A_j, Beta_j, b)
  -> (b, A_j, x_{j+1}),
```

the generated `H_b` edge:

```text
A_j -> x_{j+1}.
```

The row-`b` partner advances to:

```text
(A_j, H_j, D_j)
  -> (D_j, A_j, b*D_j).
```

So the clean V4 residual becomes a same-input two-target bridge:

```text
H_b:     A_j -> x_{j+1}       carried by row x_j,
H_{D_j}: A_j -> b*D_j         carried by row b.
```

It shares the input `A_j` with the generated matching edge.

## Consequence

V4 is not an independent square residual.  It either routes locally by the
same-target collision trichotomy or becomes a clean same-input two-target
bridge involving the generated `H_b` edge at `A_j`.

Thus V4 folds into the V3-type two-target bridge frontier.
