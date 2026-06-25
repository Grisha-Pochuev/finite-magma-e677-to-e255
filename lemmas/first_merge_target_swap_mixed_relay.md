# First-Merge Target-Swap Mixed Relay

Date: 2026-06-17.

Status:

```text
general proved / conditional relay step for branch closure
```

## Setup

Fix a target `b`. Suppose two directed branches in `H_b` first merge at `z`.
Their last edges are:

```text
p*x=b, p*b=z,
q*y=b, q*b=z,
```

with:

```text
x!=y.
```

Assume moreover that the cyclic core has an outgoing edge from `z` carried
by a row `t` not among the two last source rows:

```text
t*z=b,
t*b=m,
t notin {p,q}.
```

This is exactly the case where the merge vertex immediately continues by a
new outgoing core incidence.

Define:

```text
U=p*z,
W=q*z,
K=U*p=W*q=pred_z(b),
theta=z*(b*t).
```

By the first-merge certificate separation lemma:

```text
U!=W.
```

## Statement

After changing the target from `b` to `z`, the same rows `p,q,t` form an
outgoing-majority mixed `2+1` junction at the vertex `b` in `H_z`:

```text
p*b=z, p*z=U,
q*b=z, q*z=W,
t*theta=z, t*z=b.
```

Graphically, in `H_z`:

```text
b -> U
b -> W
theta -> b.
```

Thus a first merge in `H_b`, together with a fresh outgoing continuation from
the merge vertex, relays to the same mixed-junction type with the target pair
swapped:

```text
(target b, merge z)
  =>
(target z, split b).
```

## Proof

For the two merging edges, the target in `H_z` is `z`. Since:

```text
p*b=z,
q*b=z,
```

the two rows have the common source vertex `b` in `H_z`. Their tips are:

```text
p*z=U,
q*z=W.
```

The first-merge separation lemma gives `U!=W`, so these are two distinct
outgoing incidences at `b` in `H_z`.

For the outgoing continuation in `H_b`:

```text
t*z=b,
t*b=m,
```

apply the target-swap fan duality lemma to the edge `z -> m` of `H_b`.
It gives:

```text
theta=z*(b*t),
t*theta=z.
```

Therefore in `H_z`, row `t` carries:

```text
theta -> b,
```

because:

```text
t*theta=z,
t*z=b.
```

Since `t` is distinct from `p,q`, the three displayed incidences form a mixed
`2+1` junction.

## Consequence

The first merge is not an endpoint of the pressure process. In the generic
non-loop continuation case it becomes the next mixed junction after swapping
the target pair:

```text
H_b: two branches merge at z and continue outward
H_z: two branches split at b with one incoming counter-edge.
```

This is the precise relay form needed for the No-Free-Tail argument.

## Boundary

This lemma intentionally excludes the degenerate continuation cases:

```text
t=p,
t=q,
or an outgoing loop at z using one of the last source rows.
```

Those cases require a separate short analysis. They must not be hidden inside
the generic mixed relay.
