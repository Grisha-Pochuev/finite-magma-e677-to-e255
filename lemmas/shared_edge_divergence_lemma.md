# Shared-Edge Divergence Lemma

Date: 2026-06-07.

Status:

```text
general proved
```

Purpose:

```text
Describe exactly what happens when two distinct source rows share one directed
edge but cannot share the full next interval.
```

## Setup

Assume:

```text
p*a=b
q*a=b
p!=q.
```

Define the next outputs:

```text
c=p*b
d=q*b.
```

## Forced Divergence

If:

```text
c=d,
```

then rows `p` and `q` contain the same interval:

```text
a -> b -> c.
```

The two-step source reconstruction lemma would give:

```text
p=q.
```

Therefore:

```text
c!=d.
```

## Forced Return Coupling

The source-orbit ladder applied to:

```text
p*a=b
p*b=c
```

gives:

```text
b*(c*p)=a.
```

The same ladder applied to row `q` gives:

```text
b*(d*q)=a.
```

Row `b` is injective, so:

```text
c*p=d*q.
```

Define:

```text
h=c*p=d*q.
```

Then the full shared-edge divergence diamond is:

```text
p*a=b
q*a=b

p*b=c
q*b=d
c!=d

c*p=h
d*q=h

b*h=a.
```

Thus a common directed edge cannot continue as a common second edge.  Instead,
it creates:

```text
distinct next outputs c,d
and a common return value h.
```

## Application At The Initial Pivot

Use:

```text
P=b_2
Q=b_3
t=r_2
B=b_4
c_-=c_{-1}
alpha=P*t.
```

The two source rows have:

```text
P*0=t
Q*c_-=t

P*t=alpha
Q*t=B.
```

### Common incoming edge

If:

```text
c_-=0,
```

then rows `P` and `Q` share:

```text
0 -> t.
```

Therefore:

```text
alpha!=B
alpha*P=B*Q
t*(alpha*P)=0.
```

This is exactly the backward-zero pivot coupling, now interpreted as a general
shared-edge divergence diamond.

### Common outgoing edge

If:

```text
alpha=B,
```

then rows `P` and `Q` share:

```text
t -> B.
```

Define:

```text
beta=P*B
u=Q*B.
```

Then:

```text
beta!=u
beta*P=u*Q
B*(beta*P)=t.
```

Thus the outgoing-edge coincidence also produces a forced cross-column
coupling rather than a harmless overlap.

### Both sides cannot align

The cases:

```text
c_-=0
alpha=B
```

cannot occur together, because that would make rows `P` and `Q` share the full
interval:

```text
0 -> t -> B.
```

## Application To Any Paired-Chain Cross-Hit

At:

```text
A_i=B_m=x,
```

if the predecessors agree, the two rows share the incoming edge into `x`, so
their successors must differ and create a return coupling.

If the successors agree, the two rows share the outgoing edge from `x`, so
their following successors must differ and create the next return coupling.

Therefore every one-edge overlap of the paired cycles propagates into an
explicit divergence diamond.  The only branch without such a diamond is the
one where both neighboring points already differ at the first cross-hit.

## Main Remaining Question

The No-Free-Tail gap can now be stated as:

```text
Can the unequal-neighbor cross-hit branch avoid all divergence diamonds,
bad-cycle hits, zero traps, and occupied-row collisions until both source
cycles close?
```

Any future computation should target that exact branch, not merely test
whether the cycles intersect.

## Multi-Source Form

The arbitrary-fiber version is recorded in:

```text
common_edge_fan_lemma.md
```

All source rows sharing `a -> b` have pairwise distinct forward tips, and all
tips return to the common hub `pred_b(a)`.
