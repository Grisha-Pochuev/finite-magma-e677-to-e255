# Generated-Input Three-Source Bridge Expansion Lemma

Date: 2026-06-18.

Status:

```text
proved expansion / W3 becomes a three-source same-target configuration
```

## Purpose

This sharpens W3:

```text
clean same-input two-target bridge at a generated input A_j.
```

At a generated input `A_j`, a two-row bridge is never alone.  The generated
row `x_j` and row `b` are always present, so any extra row through `A_j`
creates a three-source configuration in the same target graph `H_{A_j}`.

## Setup

Use the generated right-`b` data:

```text
x_j*A_j=b,
x_j*b=x_{j+1},
Beta_j=pred_{x_j}(A_j),
H_j=pred_b(A_j),
D_j=b*A_j.
```

So:

```text
x_j*Beta_j=A_j,
x_j*A_j=b,

b*H_j=A_j,
b*A_j=D_j.
```

Now suppose W3 gives an extra source row `p` distinct from the two already
present rows:

```text
p*A_j=S,
S!=b.
p notin {x_j,b}.
```

Define:

```text
P=A_j*(S*p)=pred_p(A_j).
```

Then:

```text
p*P=A_j.
```

## Same-Target Expansion

In the single target graph `H_{A_j}`, the three rows give:

```text
P      -> S       carried by row p,
Beta_j -> b       carried by row x_j,
H_j    -> D_j     carried by row b.
```

Thus this non-row-`b` W3 case is not just a two-edge bridge.  It expands to a
three-edge same-target configuration at `A_j`.

If `p=b`, then the first edge is exactly the row-`b` partner:

```text
H_j -> D_j.
```

That is the two-source V4-folded bridge, not a three-source expansion.

## Local Collision Routing

If any two of the three edges have:

```text
same input,
same output,
same full ported interval,
or input-output cross hit,
```

then:

```text
same_target_pair_collision_trichotomy_lemma.md
```

routes the pair to a fan, source collision, or path concatenation.

So the clean residual is a three-edge matching in `H_{A_j}`:

```text
inputs  P, Beta_j, H_j     pairwise disjoint,
outputs S, b, D_j          pairwise disjoint,
no input-output cross hit among the three edges.
```

## Target Advance

If the three-edge same-target configuration is clean, target advance gives
three intervals sharing the original input `A_j`:

```text
H_S:     A_j -> p*S,
H_b:     A_j -> x_{j+1},
H_{D_j}: A_j -> b*D_j.
```

So the clean W3 residual becomes a three-target same-input bridge at the
generated input `A_j`.

## Consequence

The exact remaining non-row-`b` W3 obstruction is:

```text
a clean three-source matching in H_{A_j},
equivalently a clean three-target same-input bridge after target advance.
```

This is much sharper than a two-row bridge.  The next useful step is to compare
the three target outputs:

```text
p*S,
x_{j+1},
b*D_j.
```

or to show that a clean three-source matching at every generated input forces
a fan/path hit elsewhere in the right-`b` generated layer.
