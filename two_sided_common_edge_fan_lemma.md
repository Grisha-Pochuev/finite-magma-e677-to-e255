# Two-Sided Common-Edge Fan Lemma

Date: 2026-06-08.

Status:

```text
general proved
```

Purpose:

```text
Upgrade a common-edge fan from distinct forward tips to distinct
two-sided intervals.
```

## Statement

Fix `a,b` with:

```text
a!=b.
```

Let:

```text
F(a,b)={p : p*a=b}.
```

For every `p in F(a,b)`, define:

```text
c_p=p*b
d_p=a*(b*p).
```

Then row `p` contains:

```text
d_p -> a -> b -> c_p.
```

Moreover:

```text
p -> d_p
```

and:

```text
p -> c_p
```

are both injective on `F(a,b)`.

The forward tips also have the common return:

```text
c_p*p=pred_b(a).
```

## Proof

The common-edge fan lemma already gives:

```text
p*a=b
p*b=c_p
c_p*p=pred_b(a),
```

and proves that the values `c_p` are pairwise distinct.

Apply the edge-predecessor triangle to:

```text
p*a=b.
```

It gives:

```text
p*(a*(b*p))=a.
```

By definition:

```text
d_p=a*(b*p),
```

so:

```text
p*d_p=a.
```

Therefore row `p` contains:

```text
d_p -> a -> b -> c_p.
```

Suppose:

```text
d_p=d_q=d.
```

Then rows `p` and `q` contain the same ordered two-step interval:

```text
d -> a -> b.
```

The two-step source reconstruction lemma gives:

```text
p=q.
```

Thus the backward feet `d_p` are pairwise distinct.

## Self-Containing Form

Assume:

```text
P*0=P.
```

For every source:

```text
q*0=P,
```

define:

```text
T_q=q*P
alpha_q=0*(P*q).
```

Then:

```text
q*alpha_q=0
q*0=P
q*P=T_q
T_q*q=pred_P(0).
```

So every source row contains:

```text
alpha_q -> 0 -> P -> T_q.
```

Both sets:

```text
{alpha_q : q*0=P}
{T_q : q*0=P}
```

have the same cardinality as the source fiber.

Also:

```text
alpha_q!=0
T_q!=P.
```

Indeed, either equality would make row `q` send the same column to two
different outputs.

## Significance

A common edge is not only a forward fan:

```text
a -> b -> c_p.
```

It is a family of pairwise distinguished two-sided intervals:

```text
d_p -> a -> b -> c_p.
```

For the No-Free-Tail problem this gives, in every source row over `0 -> P`,
one distinct zero predecessor and one distinct forward tip.

