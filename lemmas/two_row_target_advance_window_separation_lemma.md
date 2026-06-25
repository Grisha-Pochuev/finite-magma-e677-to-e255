# Two-Row Target-Advance Window Separation Lemma

Date: 2026-06-20.

Status:

```text
proved / local window separation for the period >= 3 residual
```

## Statement

Let two distinct source rows `p,q` share one target-advance step:

```text
p*b=z,
q*b=z,
p!=q.
```

Write the predecessor and successor windows:

```text
a=pred_p(b),  so p*a=b, p*b=z, p*z=U;
c=pred_q(b),  so q*c=b, q*b=z, q*z=W.
```

Then:

```text
a!=c,
U!=W.
```

Equivalently, the two full ported windows around the shared step:

```text
(b,a,z), (z,b,U)
(b,c,z), (z,b,W)
```

are separated on both sides.

## Proof

If:

```text
a=c,
```

then rows `p` and `q` contain the same full ported interval:

```text
p*a=b, p*b=z,
q*a=b, q*b=z.
```

By two-step source reconstruction:

```text
p=q,
```

contradicting the assumption.

If:

```text
U=W,
```

then rows `p` and `q` contain the same full ported interval after target
advance:

```text
p*b=z, p*z=U,
q*b=z, q*z=U.
```

Again two-step source reconstruction gives:

```text
p=q,
```

contradiction.

Thus both neighboring ports are distinct.

## Relation To First-Merge Separation

The right-side separation:

```text
U!=W
```

is the `p*z != q*z` part of:

```text
first_merge_certificate_separation_lemma.md
```

The present lemma records the symmetric left-side separation:

```text
pred_p(b) != pred_q(b)
```

in the same full-ported-interval language used by the G12 residual.

## Period >= 3 Residual

If the active same-source target-advance components have period at least `3`
as in:

```text
target_advance_same_row_period_lemma.md
```

then, for each row separately, the three consecutive orbit vertices:

```text
a,b,z
```

and:

```text
b,z,U
```

do not collapse to a fixed point or swap loop.

So the remaining G12 step has the exact local shape:

```text
two distinct rows share the middle step b -> z,
but their left ports and right ports are both separated.
```

## Consequence For G12

In a minimal G12 loop with no independent full ported-interval collision,
two active branch rows can share a target-advance step only in this separated
window form.

Therefore the next obstruction is not local equality of neighboring ports.
It is global:

```text
can a finite relay loop be made only from separated period >= 3 two-row
windows, with no independent full interval collision and no strict clean
theta?
```
