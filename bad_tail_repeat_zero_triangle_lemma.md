# Bad-Tail Repeat Zero-Triangle Lemma

Date: 2026-06-07.

Status:

```text
proved equivalence and zero-triangle normal form / candidate next trap
```

Purpose:

```text
Replace the collision r_4=r_2 by an explicit zero-hit triangle in the
row-b_3 source orbit.
```

## Setup

Let:

```text
t=r_2
s=b_3
s*t=b_4.
```

Define:

```text
u=s*b_4
p=u*s=(s*b_4)*s.
```

The offset zipper gives:

```text
b_4*p=t.
```

## Exact Equivalence

Since:

```text
r_4=b_4*0,
```

we have:

```text
r_4=t
<=>
b_4*0=t.
```

But:

```text
b_4*p=t.
```

Row `b_4` is injective, so:

```text
b_4*0=t
<=>
p=0.
```

Therefore:

```text
r_4=r_2
<=>
p=0
<=>
(b_3*b_4)*b_3=0.
```

Equivalently, with `u=b_3*b_4`:

```text
r_4=r_2
<=>
u*b_3=0.
```

## Common-Edge Fan At 0 -> t

The same repeat equality also says:

```text
b_2*0=t
b_4*0=t.
```

By:

```text
common_edge_fan_lemma.md
```

the next tips:

```text
alpha=b_2*t
delta=b_4*t
```

are distinct and satisfy:

```text
alpha*b_2=delta*b_4=pred_t(0).
```

Thus the bad-tail repeat simultaneously creates:

```text
the zero triangle u*b_3=0;
and a two-source common-edge fan over 0 -> t.
```

Thus the bad-tail repeat is exactly a zero-hit tooth in the row-`b_3` source
orbit:

```text
t -> b_4 -> u
```

with:

```text
u*b_3=0.
```

## Zero-Triangle Consequences

Assume the equivalent conditions above and define:

```text
r=u*0.
```

Apply the inverse edge chain to:

```text
u*b_3=0.
```

Since the predecessor of `b_3` in row `0` is `b_4`, we get:

```text
r*u=b_4.
```

More explicitly, the edge predecessor triangle for `u*b_3=0` gives:

```text
u*(b_3*(0*u))=b_3
0*((u*0)*u)=b_3.
```

Because:

```text
0*b_4=b_3,
```

row-`0` injectivity yields:

```text
(u*0)*u=b_4,
```

which is:

```text
r*u=b_4.
```

So the full normal form is:

```text
s*t=b_4
s*b_4=u
u*s=0
r=u*0
r*u=b_4.
```

## Additional Zipper Edge

Let:

```text
q=s*u
d=q*s.
```

The source-orbit zipper for:

```text
b_4 -> u -> q
```

gives:

```text
u*d=b_4.
```

Thus row `u` has:

```text
u*s=0
u*d=b_4.
```

Since `b_4!=0`, row-`u` injectivity gives:

```text
d!=s.
```

The repeat branch therefore creates a second pressure pair:

```text
row u:
  s -> 0
  d -> b_4
```

and the return edge:

```text
r*u=b_4.
```

## Role Split

The new value:

```text
r=u*0
```

is the natural next classifier.

Immediate cases:

```text
r=s:
  r*u=b_4 and s*t=b_4
  => u=t by row-s injectivity;
  then row s swaps t and b_4 if s*b_4=t.

r=d:
  r*u=b_4 and u*d=b_4
  is a common-output coupling in different rows, not an immediate collision.

r=b_j:
  row b_j gets the new edge b_j*u=b_4
  in addition to b_j*r_{j-1}=b_{j+1};
  this is bad-cycle row pressure.

r fresh:
  the zero triangle produces a new active row r with r*u=b_4.
```

## Session Result

The Bad-Tail Repeat branch is not yet contradicted, but it is fully normalized:

```text
r_4=r_2
```

is exactly:

```text
(b_3*b_4)*b_3=0,
```

and forces the reusable zero triangle:

```text
b_3*b_4=u
u*b_3=0
(u*0)*u=b_4.
```

This is a stronger and more useful statement than the original tail equality.

## Next Single Frontier

Classify:

```text
r=u*0
```

by the four roles above.  In particular, test whether:

```text
r=b_j
```

always produces descent in row `b_j`, and whether the fresh-`r` branch can be
folded back into the double-interval pressure mechanism.
