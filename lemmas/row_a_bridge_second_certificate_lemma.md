# Row-a Bridge Second-Certificate Lemma

Date: 2026-06-18.

Status:

```text
general proved / second-layer certificate / instance of bad_target_self_labeled_edge_recursion_lemma.md
```

## Setup

Fix a bad target `b` and the row-a bridge edge:

```text
a*k=b,
a*b=t.
```

In `H_b`, this is the edge:

```text
k -> t
```

carried by source row `a`.

This is the `x=a` instance of:

```text
bad_target_self_labeled_edge_recursion_lemma.md
```

Define:

```text
ell=t*a,
m=a*t,
w=m*a=(a*t)*a,
beta=k*(b*a).
```

## Statement

The full double-interval certificate for the row-a bridge edge is:

```text
row a:
  beta -> k -> b -> t

row t:
  a -> ell
  w -> b

row b:
  ell -> k.
```

Equivalently:

```text
ell=pred_b(k),
w=A_b(t).
```

So the bridge edge immediately generates the next target-`b` bridge:

```text
b*ell=k.
```

## Proof

Apply the general double-interval edge certificate to the `H_b` edge:

```text
source row q=a,
input k,
target b,
output t.
```

The general certificate says:

```text
h_edge=t*a,
u_edge=a*t,
w_edge=(a*t)*a,
beta_edge=k*(b*a),
```

and forces:

```text
t*a=h_edge,
b*h_edge=k,
t*w_edge=b,
a*beta_edge=k.
```

With the notation above:

```text
h_edge=ell,
w_edge=w,
beta_edge=beta.
```

This gives all displayed cells.

## Clean Residual Consequence

In the clean external-bridge residual:

```text
k!=a.
```

Therefore:

```text
ell!=h=pred_b(a).
```

Indeed, if `ell=h`, then:

```text
b*ell=k,
b*h=a,
```

and row `b` injectivity gives:

```text
k=a,
```

contradicting the clean residual.

Thus the clean residual also has:

```text
t*a != pred_b(a).
```

## Boundary

The equality `ell=a` is not a contradiction by itself.  It says:

```text
t*a=a,
```

so `t=a*b` right-fixes `a`.  Since `a` is not known to be a bad target, this
belongs to the two-target relay analysis, not to the bad-target contradiction
for `b`.
