# Side-Attachment Mixed Certificate Lemma

Date: 2026-06-17.

Status:

```text
general proved / specialized certificate for earliest side attachment
```

## Purpose

This lemma specializes the mixed `2+1` junction to the situation produced by
the binary-sink escape:

```text
an extra core incidence attaches to an internal vertex of an active branch path.
```

It records which row is the old incoming path edge, which row is the old
outgoing path edge, and what the target swap does to these three rows.

## Common Path Data

Fix a target `b`.  Let an active branch path pass through an internal vertex
`v`:

```text
x -> v -> y
```

in `H_b`.  Write the two path rows as:

```text
p*x=b, p*b=v,      path enters v
q*v=b, q*b=y.      path leaves v
```

Thus the active path already gives one incoming and one outgoing incidence at
`v`.

## Case A: Extra Incoming Side Incidence

Suppose the side incidence also enters `v`:

```text
r*a=b,
r*b=v.
```

Define:

```text
U=p*v,
V=r*v,
K=U*p=V*r=pred_v(b),
h=y*q=pred_b(v),
theta=v*(b*q).
```

Then:

```text
v*K=b,
b*h=v.
```

After target swap `b -> v`, the three rows become:

```text
p*b=v,       p*v=U,
r*b=v,       r*v=V,
q*theta=v,   q*v=b.
```

Graphically in `H_v`:

```text
b -> U,
b -> V,
theta -> b.
```

The two new outgoing tips are distinct:

```text
U!=V.
```

Indeed, if `U=V`, rows `p` and `r` contain the same ordered two-step interval:

```text
b -> v -> U,
```

so two-step source reconstruction gives `p=r`, and row injectivity gives
`x=a`, contradicting distinct incoming incidences.

If the two arrivals are genuine branch arrivals, `x!=v` and `a!=v`, then:

```text
U!=b,
V!=b.
```

So the extra incoming side incidence relays, after target swap, to an
outgoing-majority mixed `2+1` junction at `b` in `H_v`, with the possible loop
degeneracy of the third incidence handled by the existing junction dichotomy.

## Case B: Extra Outgoing Side Incidence

Suppose the side incidence leaves `v`:

```text
r*v=b,
r*b=c.
```

Define:

```text
h=y*q=c*r=pred_b(v),
S=p*v,
J=S*p=pred_v(b),
alpha=v*(b*q),
gamma=v*(b*r).
```

Then:

```text
b*h=v,
v*J=b.
```

After target swap `b -> v`, the three rows become:

```text
q*alpha=v,   q*v=b,
r*gamma=v,   r*v=b,
p*b=v,       p*v=S.
```

Graphically in `H_v`:

```text
alpha -> b,
gamma -> b,
b     -> S.
```

The two new incoming feet are distinct:

```text
alpha!=gamma.
```

This is the target-swap form of the common outgoing fan at `v`; equivalently,
if they were equal, the two rows would fail the two-sided common-edge
separation.

If the arrival along the active path is genuine, `x!=v`, then:

```text
S!=b.
```

So the extra outgoing side incidence relays, after target swap, to an
incoming-majority mixed `2+1` junction at `b` in `H_v`.

## Two-Target Bridge Square

Both side-attachment orientations expose the same pair of target bridges:

```text
pred_b(v)  with  b*pred_b(v)=v,
pred_v(b)  with  v*pred_v(b)=b.
```

The difference is which pair of rows shares which bridge.

Incoming-side case:

```text
U*p=V*r=pred_v(b),
y*q=pred_b(v).
```

Outgoing-side case:

```text
y*q=c*r=pred_b(v),
(p*v)*p=pred_v(b).
```

Thus an earliest side attachment should be compared through the full
three-row certificate, not by trying to identify the two bridge labels.

## Consequence

The first side attachment before a binary sink is now in the same algebraic
format as the original mixed `2+1` frontier, but with extra branch-path
information:

```text
one row is the old incoming branch edge;
one row is the old outgoing branch edge;
one row is the side-core edge.
```

This makes the next No-Free-Tail step more constrained than a generic mixed
junction: any relayed first merge must respect this inherited path ordering.
