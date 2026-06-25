# Same-Input Lift Target-Advance Lemma

Date: 2026-06-18.

Status:

```text
general proved / lifted same-input pair advances back to two-target split
```

## Purpose

This records the transport behind U4 and also explains why U3's same-target
pair is not an independent new layer.

The same-input target lift:

```text
p*z=s,
q*z=r
```

creates a same-target pair in `H_z`.  Target advance of that pair returns to
the original two-target split at the common input `z`, with one more forward
value in each source row.

## General Statement

Assume:

```text
p*z=s,
q*z=r,
s!=r.
```

Define:

```text
P_z=z*(s*p),
Q_z=z*(r*q).
```

Then:

```text
p*P_z=z,
q*Q_z=z.
```

So in `H_z`:

```text
P_z -> s     carried by row p,
Q_z -> r     carried by row q.
```

Target-advance these two intervals.  Row `p` gives:

```text
(z, P_z, s)
  -> (s, z, p*s).
```

Row `q` gives:

```text
(z, Q_z, r)
  -> (r, z, q*r).
```

Thus the lifted same-target pair advances back to:

```text
target s: z -> p*s,
target r: z -> q*r.
```

Both advanced intervals share the input `z`.

## Consequence

If the lifted pair in `H_z` is locally clean under:

```text
same_target_pair_collision_trichotomy_lemma.md
```

then it is not an independent same-target matching.  Its target advance is a
two-target same-input bridge:

```text
H_s: z -> p*s,
H_r: z -> q*r.
```

The next work must use that two-target bridge or compare the forward values
`p*s` and `q*r`.

## U4 Application

For the shifted-repeat split:

```text
row Z_i^{r-1}: T -> Z_i^r,
row Z_i^{s-1}: T -> Z_i^s,
```

the lift gives a pair in `H_T`.

If that lifted pair is clean-disjoint, target advance returns to:

```text
H_{Z_i^r}: T -> Z_i^{r-1}*Z_i^r,
H_{Z_i^s}: T -> Z_i^{s-1}*Z_i^s.
```

So U4 is also a two-target bridge with common input `T`, not a free
same-target matching.

## U3 Application

For:

```text
Beta_i=A_j,
```

this general lemma specializes to:

```text
beta_coupled_same_target_pair_advance_lemma.md
```

where:

```text
z=A_j,
s=A_i,
r=b.
```
