# Pivot Ladder Fan Lemma

Date: 2026-06-07.

Status:

```text
proved pressure combination / bounded collision split
```

Purpose:

```text
Combine the four-output pivot return fan with the bad-cycle ladder edge in the
same row t=r_2.
```

## Setup

Let:

```text
t=r_2=b_k.
```

From the pivot return fan, row `t` has:

```text
t*z=0
t*h=c
t*g_alpha=w
t*g_v=p,
```

where:

```text
z=(b_2*t)*b_2
h=b_4*b_3
c=c_{-1}

alpha=b_2*t
w=(b_2*alpha)*b_2
g_alpha=(alpha*t)*alpha

v=b_4
p=(b_3*b_4)*b_3
g_v=(b_4*t)*b_4.
```

The bad-cycle ladder independently gives:

```text
t*r_{k-1}=b_{k+1}.
```

Thus row `t` has a five-spoke fan:

```text
z         -> 0
h         -> c
g_alpha   -> w
g_v       -> p
r_{k-1}   -> b_{k+1}.
```

## Ladder-Collision Equivalences

By injectivity of row `t`:

```text
b_{k+1}=0
<=>
r_{k-1}=z;

b_{k+1}=c
<=>
r_{k-1}=h;

b_{k+1}=w
<=>
r_{k-1}=g_alpha;

b_{k+1}=p
<=>
r_{k-1}=g_v.
```

So every collision with the ladder output forces the old tail parameter
`r_{k-1}` to equal one of the four explicit pivot-fan columns.

The already known collision:

```text
c=0
```

is equivalent to:

```text
h=z,
```

the backward-zero trap.

All other pairwise output collisions among:

```text
0,c,w,p
```

are likewise equivalent to pairwise column collisions among:

```text
z,h,g_alpha,g_v.
```

## Five-Distinct Branch

If none of the collision roles occurs, then:

```text
0, c, w, p, b_{k+1}
```

are five distinct forced outputs in row `t`, with five distinct columns:

```text
z, h, g_alpha, g_v, r_{k-1}.
```

This does not by itself contradict finiteness, but it is now a sharply bounded
branch.  Any further pressure in row `t` must avoid these five occupied outputs
and columns.

## Next Target

Apply the edge-triangle predecessor step to these five row-`t` edges:

```text
t*q=y
=> t*(q*(y*t))=q.
```

The next layer either:

```text
hits one of the five occupied columns/outputs and forces a collision;
or extends five explicit predecessor segments in the single row t.
```

The key question is whether the five-distinct branch can close as permutation
cycles without one segment meeting another or returning to the bad-cycle
ladder column `r_{k-1}`.
