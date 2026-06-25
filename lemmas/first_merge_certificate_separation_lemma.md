# First-Merge Certificate Separation Lemma

Date: 2026-06-17.

Status:

```text
general proved / boundary clarification for branch closure
```

## Setup

Fix a target `b`. Let two directed branches in `H_b` first merge at `z`.
Write their last edges as:

```text
p*x=b, p*b=z,
q*y=b, q*b=z,
```

where the merge is first, so:

```text
x!=y.
```

By two-step source reconstruction:

```text
p!=q.
```

Define the last-edge certificate labels:

```text
H_x=z*p=pred_b(x),
H_y=z*q=pred_b(y),
U=p*z,
W=q*z,
K=U*p=W*q=pred_z(b).
```

The common terminal value is:

```text
z*K=b.
```

## Separation

At a first merge, the following equalities are impossible:

```text
H_x=H_y,
U=W.
```

Equivalently:

```text
z*p != z*q,
p*z != q*z.
```

## Proof

If:

```text
H_x=H_y,
```

then:

```text
b*H_x=x,
b*H_y=y.
```

Hence:

```text
x=y,
```

contradicting first merge.

If:

```text
U=W,
```

then rows `p` and `q` contain the same ordered two-step interval:

```text
b -> z -> U.
```

Indeed:

```text
p*b=z, p*z=U,
q*b=z, q*z=U.
```

The two-step source reconstruction lemma gives:

```text
p=q.
```

Then:

```text
p*x=b,
p*y=b,
```

and left injectivity of row `p` gives:

```text
x=y,
```

again contradicting first merge.

## Consequence

The common terminal bridge:

```text
K=pred_z(b)
```

is real but weak. It does not imply equality of the adjacent last-certificate
labels:

```text
z*p, z*q, p*z, q*z.
```

Thus a branch-closure proof cannot simply propagate equality backward from
`K_z` by identifying neighboring labels. It must use a stronger relation
involving the full crossed equality:

```text
(p*z)*p=(q*z)*q=K.
```

This is the exact remaining local pressure at a first merge.
