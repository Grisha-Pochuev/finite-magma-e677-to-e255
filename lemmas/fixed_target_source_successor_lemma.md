# Fixed-Target Source-Successor Lemma

Date: 2026-06-19.

Status:

```text
general proved / every H_T edge forces a successor-source edge in the same H_T
```

## Purpose

This records the fixed-target version of the triangle pressure used in:

```text
x3_advanced_edge_triangle_pressure_lemma.md
```

It is useful for the current Y3 residual because the three-edge matching in
`H_{A_j}` does not merely target-advance away from `A_j`.  It also generates a
new layer inside the same target graph `H_{A_j}`.

## Statement

Fix a target `T`.  Suppose row `r` gives an edge in `H_T`:

```text
r*I=T,
r*T=O.
```

Let:

```text
U=r*O.
```

Then row `O` also gives an edge in the same graph `H_T`:

```text
O*(U*r)=T,
O*T=O*T.
```

So the source row changes by right multiplication with `T`:

```text
r -> r*T=O.
```

and the new `H_T` edge is:

```text
(U*r) -> O*T
```

carried by row `O`.

## Proof

Apply E677 to:

```text
x=O,
y=r.
```

Since:

```text
r*T=O,
r*O=U,
```

E677 gives:

```text
O = r*(O*((r*O)*r)) = r*(O*(U*r)).
```

But `r*T=O`, and row `r` is a permutation, so left cancellation in row `r`
gives:

```text
O*(U*r)=T.
```

Thus row `O` has predecessor `U*r` of `T`, hence it contributes an edge in
`H_T`.

## Y3 Application

For the clean Y3 matching in `H_{A_j}`:

```text
row p:   P      -> S,
row x_j: Beta_j -> b,
row b:   H_j    -> D_j,
```

the fixed-target source-successor map sends:

```text
p   -> S,
x_j -> b,
b   -> D_j.
```

The next forced layer in the same target `A_j` is:

```text
row S:   (p*S)*p       -> S*A_j,
row b:   x_{j+1}*x_j   -> b*A_j = D_j,
row D_j: (b*D_j)*b     -> D_j*A_j.
```

Since:

```text
x_{j+1}*x_j=H_j,
```

the middle edge is exactly the already tracked row-`b` edge:

```text
H_j -> D_j.
```

So the X3/Y3 triangle layer is not an unrelated new matching.  It is the
right-`A_j` source-successor layer of the same fixed target graph `H_{A_j}`.

## Consequence

The next Y3 split can be stated in terms of source-row orbits under right
multiplication by `A_j`:

```text
r_{n+1}=r_n*A_j.
```

A hit between the source-successor orbit of `p` and the generated orbit
through:

```text
x_j -> b -> D_j -> ...
```

repeats a source row in `H_{A_j}` and therefore repeats the corresponding full
ported interval.  If no such source hit occurs before a repeat inside one
orbit, the remaining object is a clean fixed-target source-orbit residual.
