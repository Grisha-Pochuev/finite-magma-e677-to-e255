# Proper Crossed-Fan Target-Swap Self-Duality Lemma

Date: 2026-06-18.

Status:

```text
general proved / routing lemma
```

## Setup

Fix distinct `a,b`.  Suppose there is a crossed fan:

```text
p*a=b,  q*a=b,
p*b=c,  q*b=d,

r*b=a,  s*b=a,
r*a=u,  s*a=v.
```

Assume the selected rows are proper, meaning no selected row swaps `a` and
`b`:

```text
c!=a, d!=a,
u!=b, v!=b.
```

The fan certificates define:

```text
h=c*p=d*q=pred_b(a),   b*h=a,
k=u*r=v*s=pred_a(b),   a*k=b.
```

## Statement

After swapping the target pair `a <-> b`, the same four rows form the dual
proper crossed fan:

```text
r*b=a,  s*b=a,
r*a=u,  s*a=v,

p*a=b,  q*a=b,
p*b=c,  q*b=d.
```

That is:

```text
outgoing fan F(a,b) with tips c,d
incoming fan F(b,a) with tips u,v
```

becomes:

```text
outgoing fan F(b,a) with tips u,v
incoming fan F(a,b) with tips c,d.
```

The two common hubs are exchanged:

```text
h <-> k.
```

The following properties are invariant under the swap:

```text
properness of the selected rows;
h=k versus h!=k;
existence or nonexistence of cross-tip collisions
{c,d} ∩ {u,v}.
```

## Proof

The displayed equations are symmetric in the unordered pair `{a,b}` once the
two source pairs are exchanged:

```text
(p,q,c,d,h) <-> (r,s,u,v,k).
```

The outgoing common-edge fan:

```text
p*a=b, q*a=b
```

for the target pair `(a,b)` is exactly the incoming common-edge fan after the
target pair is read as `(b,a)`.

Similarly:

```text
r*b=a, s*b=a
```

becomes the outgoing fan for the swapped target pair.

The common-edge fan lemma gives:

```text
c*p=d*q=pred_b(a)=h,
u*r=v*s=pred_a(b)=k.
```

After swapping `a` and `b`, these are precisely the same hub equations with
`h` and `k` interchanged.

Properness is just:

```text
p*b!=a, q*b!=a, r*a!=b, s*a!=b,
```

which is symmetric.  The cross-tip set intersection

```text
{c,d} ∩ {u,v}
```

is also symmetric.

## Use In The Proper Bad-Target Frontier

The remaining proper crossed-fan case should be treated as a two-target object
on the unordered pair `{a,b}`.

The badness assumption is not symmetric:

```text
b is bad
```

does not imply that `a` is bad.  But the proper crossed-fan skeleton itself is
fully target-swap self-dual.  Therefore any final argument for the clean
`h!=k`, no-cross-tip-collision branch should track full ported intervals across
the two-target relay rather than trying to privilege one side of the skeleton.

