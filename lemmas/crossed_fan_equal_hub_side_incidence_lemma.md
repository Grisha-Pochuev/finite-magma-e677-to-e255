# Crossed-Fan Equal-Hub Bridge-Edge Lemma

Date: 2026-06-18.

Status:

```text
general proved / bridge-edge routing lemma
```

## Setup

Use the crossed-fan notation:

```text
p*a=b,  q*a=b,
p*b=c,  q*b=d,

r*b=a,  s*b=a,
r*a=u,  s*a=v.
```

Let the common hubs be:

```text
h=c*p=d*q=pred_b(a),   b*h=a,
k=u*r=v*s=pred_a(b),   a*k=b.
```

Assume the equal-hub case:

```text
h=k.
```

Then:

```text
b*h=a,
a*h=b.
```

## Statement For A Bad Target

If `b` is a bad target, so no row right-fixes `b`, then:

```text
h != b.
```

Moreover, row `a` gives an additional `H_b` edge with input `h`:

```text
a*h=b,
a*b=t,
```

where:

```text
t != b.
```

Thus, in `H_b`, row `a` realizes:

```text
h -> t.
```

There are two cases:

```text
1. h != a:
   this is a bridge-edge incidence based at h, away from the crossed split a;

2. h = a:
   row a itself belongs to the outgoing fiber F(a,b).  If a is not already one
   of the selected source rows p,q, this upgrades the outgoing fan at a to a
   triple fan.
```

## Proof

Since `h=k`, the defining bridge equations give:

```text
b*h=a,
a*h=b.
```

If `h=b`, then:

```text
a*b=b,
```

which is impossible for a bad target `b`, because badness says `x*b!=b` for
every row `x`.

Therefore:

```text
h!=b.
```

Now row `a` has:

```text
a*h=b.
```

By definition of `H_b`, this means `A_b(a)=h`.  Its output is:

```text
R_b(a)=a*b=t.
```

Again, badness of `b` gives:

```text
t!=b.
```

So row `a` is a genuine graph edge:

```text
h -> t
```

in `H_b`.

If `h!=a`, this edge is based away from the original crossed vertex `a`.  If
`h=a`, then row `a` satisfies `a*a=b`, so row `a` is itself a source in the
outgoing fiber `F(a,b)`.

Important boundary:

```text
h -> t
```

is not automatically a side attachment to the old crossed-fan component.  It
becomes a side attachment only if `h` is already known to lie in the active
`H_b` corridor/core.  Otherwise it is an external bridge edge that must be
tracked by the two-target relay state.

## Use In The Proper Bad-Target Crossed-Fan Frontier

Together with:

```text
crossed_fan_cross_tip_hub_separation_lemma.md
bad_target_crossed_fan_row_a_edge_lemma.md
```

the equal-hub branch now has strong routing information:

```text
h=k
=> cross tips are disjoint
=> row a creates either a bridge edge based at h or a larger outgoing fan at a.
```

So the equal-hub branch should be handled by bridge-edge / enlarged-fan relay
machinery, not by searching for a direct short right-fixer.
