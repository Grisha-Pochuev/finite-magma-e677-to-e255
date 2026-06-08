# Double Interval Pressure Lemma

Date: 2026-06-05.

Status:

```text
candidate / next main frontier
```

Purpose:

```text
Record the sharpened form of the pressure-diamond obstruction.
```

## Setup

Assume the main no-free-tail contradiction setup:

```text
t=r_2=b_2*0
t!=0
s=b_3
s*t=b_4.
```

The edge-triangle expansion of the origin edge gives:

```text
u_2=0*(t*b_2)
b_2*u_2=0
b_2*0=t
```

So row `b_2` contains the two-sided segment:

```text
u_2 -> 0 -> t.
```

The edge-triangle expansion of the offset edge gives:

```text
c_{-1}=t*(b_4*b_3)
b_3*c_{-1}=t
b_3*t=b_4
```

So row `b_3` contains the two-sided segment:

```text
c_{-1} -> t -> b_4.
```

## Main Observation

The nonzero value `t=r_2` is not a free tail point.  It is the common pivot of
two forced adjacent intervals:

```text
row b_2:  u_2     -> 0 -> t
row b_3:  c_{-1} -> t -> b_4
```

Together with row-`t` pressure:

```text
z_t=(b_2*t)*b_2
t*z_t=0
t*(b_4*b_3)=c_{-1}
```

and row-`b_4` pressure:

```text
p=(b_3*b_4)*b_3
b_4*p=t
b_4*r_3=b_5
```

this is stronger than the earlier one-sided or single-row orbit picture.

## Immediate Roles

The origin predecessor cannot be zero:

```text
u_2!=0
```

because row `b_2` sends:

```text
0 -> t
u_2 -> 0
```

and `t!=0`.

If:

```text
u_2=t,
```

then row `b_2` swaps:

```text
0 <-> t.
```

This is the origin self-swap role.

If:

```text
c_{-1}=0,
```

then row `t` has two zero outputs, so:

```text
b_4*b_3=z_t.
```

This is the backward-zero trap.

If:

```text
c_{-1}=b_4,
```

then row `b_3` swaps:

```text
t <-> b_4.
```

This is the offset self-swap role.

If:

```text
p=r_3,
```

then exactly:

```text
t=b_5.
```

So outside the special bridge offset `r_2=b_5`, row `b_4` has two distinct
occupied columns.

## Candidate Lemma

Proposed next main lemma:

```text
In a finite E677 magma, the double interval

  row b_2:  u_2     -> 0 -> t
  row b_3:  c_{-1} -> t -> b_4

cannot be extended with both predecessors staying completely fresh, while also
avoiding the row-t zero pressure and the row-b_4 occupied-column pressure.
```

If this is proved, the no-free-tail route becomes:

```text
t!=0
=> pressure diamond
=> double interval pressure
=> zero trap / self-swap / row collision / bad-cycle descent
=> contradiction
=> r_2=0
=> E255 for 0.
```

## Next Work

Do not start a broad finite search from this file.

The next useful step is symbolic:

```text
Classify the occupied roles of u_2:
  u_2=t      -> origin self-swap;
  u_2=b_j    -> row-b_j pressure/descent;
  u_2 fresh  -> a second fresh interval must be tracked together with c_{-1}.
```

Progress:

```text
occupied_u2_lift_lemma.md
```

If:

```text
u_2=b_j,
```

then:

```text
t*b_2=b_{j+1}.
```

So the occupied `u_2` case lifts immediately into row `t`, where it combines
with:

```text
t*z_t=0
t*(b_4*b_3)=c_{-1}
t*r_{k-1}=b_{k+1}    when t=b_k.
```

Therefore the hard branch is not all occupied `u_2`; it is specifically the
case where this row-`t` lift avoids zero collision, predecessor coupling, and
bad-cycle descent.

## Cross-Source Progress 2026-06-07

The file:

```text
two_step_source_reconstruction_lemma.md
```

proves that an ordered interval:

```text
a -> b -> c
```

uniquely determines its source row.

Applied to the paired predecessor cycles, this gives:

```text
paired_chain_aligned_overlap_lemma.md
```

The row-`b_2` and row-`b_3` cycles cannot share two aligned consecutive edges.
At the initial common pivot `t`, the roles:

```text
c_{-1}=0
b_2*t=b_4
```

cannot occur together.

This does not yet prove the candidate lemma, but it replaces the vague need for
"some coupling" with an exact forbidden overlap.  The remaining task is to
force that overlap, or an unequal-neighbor pressure role, from the row-`t` and
row-`b_4` fans.

## Fan-Spine Upgrade 2026-06-08

The strongest bad-tail occupied role now produces:

```text
self_containing_fan_spine_lemma.md
```

When the pressure network forces:

```text
P*0=P,
```

the common-edge fan above `0 -> P` creates a row-`P` spine:

```text
e -> h -> 0 -> P -> C,
```

and every additional fan tip returns to the same backward hub `h`.

Thus the double-interval candidate has acquired a concrete multi-row
termination object:

```text
one five-point active interval;
several pairwise distinct return tips;
one common hub.
```

The next general target is to prove that this fan spine cannot close inside a
finite bad-cycle block without an aligned overlap, row-`0` shared-edge descent,
or zero-column fixed point.

The common-edge object is now two-sided:

```text
two_sided_common_edge_fan_lemma.md
```

For every source `q*0=P`, row `q` contains:

```text
alpha_q -> 0 -> P -> T_q,
```

where all backward feet `alpha_q` are distinct and all forward tips `T_q` are
distinct.

The shortest row-`P` closure:

```text
e=C
```

is no longer open. It is a row-`0` shared-edge descent and creates a bad
four-cycle at `P`. After choosing a minimal bad element with cycle length
greater than four, this closure is impossible.

The aligned occupied-tip role is also closed:

```text
C=b_j
T_q=b_{j-2}
=>
q=r_{j-3}.
```

Therefore the double-interval frontier has narrowed to non-aligned occupied
tips, zero-tooth continuation after a tip-source collision, and longer
row-`P` cycle closure.

For the zero-tooth continuation, the aligned occupied return is now closed:

```text
v*q=0
q=b_k
v*0=q
=>
v=r_{k-1}.
```

Only fresh returns and returns to a different bad-cycle index remain.

The longer row-`P` closure is also no longer an undifferentiated cycle event.
For the fourth and fifth predecessors:

```text
f=L_P^{-4}(P)
g=L_P^{-5}(P),
```

the exact split is:

```text
f*f=g <=> h*P=P <=> E255 at P;
f*f!=g <=> P is bad.
```

Under minimal bad-cycle selection, every shorter closure must take the first
role.

For exact closure length five, even that first role is impossible:

```text
fan_spine_length_five_badness_lemma.md
```

The forced good-P equations collide in row `h`. Thus the first unresolved
good shorter closure is length six.

The fan recursion itself has now been made explicit:

```text
fan_tip_bridge_expansion_lemma.md
```

Every original source `q` produces:

```text
row q:   0 -> P -> T_q
row T_q: q -> h and w_q -> P,
```

where:

```text
w_q=(q*T_q)*q.
```

A bridge collision creates a second-generation common-edge fan; otherwise all
bridges are distinct. This is the concrete recursive pressure process whose
finite termination is still required.

The fan is anchored back to the original bad tail by:

```text
terminal_source_anchored_fan_lemma.md
```

The universal source:

```text
A=0*0=b_{m-1}
```

has:

```text
A*r_{m-2}=0
A*0=P.
```

So the self source and terminal source provide:

```text
row P: h       -> 0 -> P
row A: r_{m-2} -> 0 -> P.
```

A third source adds a third distinct backward foot. This is the direct return
from bridge expansion to double-interval pressure.

Further progress:

```text
double_interval_backward_extension_lemma.md
```

If `u_2` and `c_{-1}` are fresh, the double interval still cannot stay static.
The edge-triangle rule extends both intervals one step backward:

```text
e_2=u_2*b_1
b_2*e_2=u_2

e_3=c_{-1}*(t*b_3)
b_3*e_3=c_{-1}.
```

So the fresh branch contains:

```text
row b_2:
  e_2 -> u_2 -> 0 -> t

row b_3:
  e_3 -> c_{-1} -> t -> b_4
```

The hard branch is therefore a growing double predecessor chain, not a fixed
local configuration.

The first computational check, if needed later, should test only a fixed role,
not the full open search.
