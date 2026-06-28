# Two-Sided Offset Orbit Lemma

Date: 2026-06-04.

Status:

```text
proved consequence / candidate no-free-tail framework
```

Purpose:

```text
Use the edge-predecessor triangle on the first offset edge to make the
row-b_3 orbit two-sided.
```

This refines:

```text
offset_source_orbit_first_return_lemma.md
source_orbit_zipper_lemma.md
edge_predecessor_triangle_lemma.md
```

## Setup

Let:

```text
s=b_3
t=r_2=b_t
```

The offset edge is:

```text
s*t=b_4.
```

The forward row-`s` orbit was:

```text
c_0=t
c_1=b_4
c_{i+1}=s*c_i.
```

## Backward Step From The Offset Edge

Apply the edge predecessor triangle to:

```text
s*t=b_4.
```

It gives:

```text
s*(t*(b_4*s))=t.
```

Therefore the predecessor of `t` in row `s` is explicit:

```text
c_{-1}=t*(b_4*s).
```

So:

```text
s*c_{-1}=c_0.
```

The offset orbit is not just a forward tail:

```text
c_0 -> c_1 -> c_2 -> ...
```

It is a two-sided row-`s` orbit segment:

```text
c_{-1} -> c_0 -> c_1 -> c_2 -> ...
```

where:

```text
c_{-1}=c_0*(c_1*s).
```

## General Two-Sided Formula

For any source-orbit edge:

```text
s*c_i=c_{i+1},
```

the predecessor is:

```text
c_{i-1}=c_i*(c_{i+1}*s).
```

This is the same zipper formula, read as a backward orbit construction.

Thus the source row `s` orbit can be extended in both directions:

```text
... -> c_{-2} -> c_{-1} -> c_0 -> c_1 -> c_2 -> ...
```

with:

```text
c_{i-1}=c_i*(c_{i+1}*s).
```

Because row `s` is a finite permutation, this two-sided orbit is a finite
cycle.

## New First-Return Target

The no-free-tail target should therefore use a two-sided first return:

```text
starting from the occupied edge c_0=t -> c_1=b_4,
look both forward and backward in the row-s cycle.
```

The first return to the occupied bad-cycle block can occur:

```text
forward:  c_k in occupied block, k>=2;
backward: c_{-k} in occupied block, k>=1.
```

Either direction creates row pressure by the same zipper/triangle formulas.

## Immediate Backward Roles

The first backward point is:

```text
c_{-1}=t*(b_4*s).
```

Possible roles:

```text
c_{-1}=t:
  impossible unless b_4=t, because row s would send t to both t and b_4.

c_{-1}=b_4:
  row s swaps t and b_4:
    s*t=b_4
    s*b_4=t.
  This is the general self-swap role.

c_{-1}=0:
  s*0=t, so r_3=t.
  The segment
    0 -> t -> b_4
  in row s triggers the source-row zero trap.

c_{-1}=b_j:
  first-return row pressure applies in row b_j.

c_{-1} fresh:
  the orbit has a fresh backward tail as well as the forward tail.
```

So a free no-bridge tail must keep both directions fresh:

```text
c_2,c_3,...
c_{-1},c_{-2},...
```

and must also keep the zipper/triangle columns fresh.

## Backward Zero Is A Source-Row Zero Trap

If:

```text
c_{-1}=0,
```

then:

```text
s*0=t
s*t=b_4.
```

Let:

```text
g=b_4*s.
```

The source-orbit ladder gives:

```text
t*g=0.
```

This is exactly:

```text
c_{-1}=t*(b_4*s)=0.
```

Now the global source-row zero trap applies:

```text
t*g=0
d=t*0
d*t=pred0(g)
g=t*(g*succ0(t)).
```

So backward zero is not a new case.  It enters the already known zero-trap
machinery.

Additionally:

```text
r_3=s*0=t=r_2.
```

The bad-cycle ladder gives:

```text
b_4*r_3=b_5,
```

so:

```text
b_4*t=b_5.
```

Together with the offset relay:

```text
b_4*p=t
p=(s*b_4)*s,
```

row `b_4` has an occupied pressure pair:

```text
b_4*p=t
b_4*t=b_5.
```

## Backward 2-Cycle Is Self-Swap

If:

```text
c_{-1}=b_4,
```

then:

```text
s*b_4=t
s*t=b_4.
```

So row `s=b_3` swaps the offset pair:

```text
t <-> b_4.
```

The old local self-swap branches are instances of this role.  It should be
treated by the edge-triangle/self-swap pressure mechanism, not as a fresh
tail.

## Stronger Candidate

The current strongest no-free-tail target becomes:

```text
In a no-bridge offset branch, the two-sided row-b_3 orbit through
  r_2 -> b_4
cannot have a maximal fresh arc whose endpoints avoid:
  0;
  bad-cycle elements;
  bridge/self-cycle roles;
  zipper-column collisions;
  edge-triangle pressure collisions.
```

Equivalently:

```text
the finite row-b_3 cycle cannot contain the occupied edge r_2 -> b_4 as part
of a completely fresh two-sided interval.
```

This is still not the full proof, but it removes the misleading picture of a
one-directional free tail.

## Row-`r_2` Pressure

Update 2026-06-04:

```text
r2_row_pressure_lemma.md
```

The offset value:

```text
t=r_2
```

is itself produced by:

```text
b_2*0=t.
```

Applying the edge predecessor triangle to this edge gives:

```text
t*((b_2*t)*b_2)=0.
```

So row `t` already has a forced zero edge.

The backward offset point gives another row-`t` edge:

```text
c_{-1}=t*(b_4*s).
```

Therefore row `t` has:

```text
t*((b_2*t)*b_2)=0
t*(b_4*s)=c_{-1}.
```

If `c_{-1}=0`, these columns collide and the branch is the backward-zero trap.
If `c_{-1}!=0`, row `t` has two distinct occupied outputs.

So a fresh two-sided interval must also avoid collision in row `r_2`, not only
in row `b_3`.
