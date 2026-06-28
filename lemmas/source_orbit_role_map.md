# Source-Orbit Role Map

Date: 2026-05-31.

Status:

```text
candidate role map for source_orbit_ladder_lemma.md
```

Scope:

```text
case45
7*0=5
6*5=5
6*6=8
q=6*8
```

Transfer check:

```text
The same zero-hit mechanism also appears in the neighboring special-branch
layers 6*6=2, 6*6=3, and 6*6=4.
```

## Dependency

The source-orbit ladder is not a bare syntactic consequence of one E677
substitution. It uses the established finite E677 fact that every left row is
a permutation, equivalently the inverse edge chain:

```text
a*z=c  ==>  z = c*((a*c)*a)
```

Thus if:

```text
a*z0=z1
a*z1=z2
```

then:

```text
z0 = z1*(z2*a)
```

In the current layer, with source row `6`:

```text
6*z0=z1
6*z1=z2
=> z1*(z2*6)=z0
```

## Confirmed Roles

### Immediate zero-hit

Role:

```text
8 -> q -> 0
```

Then:

```text
6*q=0
6*0=t
0*(t*6)=q
t*6=pred0(q)
```

Confirmed representatives:

```text
q=2:
  pred0(2)=1
  r=6*0 in {1,3,4,7}
  r*6=1 closes all r
  audit 2026-05-31: this holds without the extra condition h=2*6=2

q=4:
  pred0(4)=3
  t=6*0 in {1,2,3,7}
  t*6=3 closes all t

q=7:
  pred0(7)=6
  t=6*0 in {1,2,3,4}
  t*6=6 closes all t
```

### Immediate zero-hit plus one

Role:

```text
8 -> q -> 0 -> 1
```

Confirmed representative:

```text
q=3:
  6*3=0
  6*0=1
  1*6=2
  next source rung u=6*1 in {4,6,7}
  all u closed
```

### Eventual zero-hit

Role:

```text
8 -> q -> s -> 0
```

or, more generally:

```text
8 -> q -> s -> ... -> p -> 0
```

Confirmed representatives:

```text
q=4
s=6*4=1
6*1=0
```

Then:

```text
6*0=r
0*(r*6)=1
r*6=pred0(1)=0
```

Diagnostic:

```text
r=6*0 in {2,3,7}
```

Targeted checks:

```text
r=2 -> closed
r=3 -> closed
r=7 -> closed
```

Second representative:

```text
q=4
s=6*4=2
6*2=0
```

Then:

```text
6*0=r
0*(r*6)=2
r*6=pred0(2)=1
```

Diagnostic:

```text
r=6*0 in {1,3,7}
```

Targeted checks:

```text
r=1 -> closed
r=3 -> closed
r=7 -> closed
```

Longer representative from a different `q`:

```text
q=7
6*7=1
6*1=2
6*2=0
```

This is:

```text
8 -> 7 -> 1 -> 2 -> 0
```

Then:

```text
6*0=r
0*(r*6)=2
r*6=pred0(2)=1
```

Admissible `r` values:

```text
r in {3,4}
```

Targeted checks:

```text
r=3 -> closed
r=4 -> closed
```

Structural reading:

```text
The useful object is the source row-6 orbit itself, not the active q-row.
If the orbit eventually hits 0 after one or more source steps, row 0 converts
the next return edge into an explicit predecessor condition.
```

## Current Status

This is now a genuine candidate mechanism, but not a complete proof of the
whole `6*6=8` layer.

Known:

```text
immediate zero-hit is confirmed for q=2,4,7
zero-hit-plus-one is confirmed for q=3
eventual zero-hit is confirmed for three zero-avoiding representatives:
  q=4,s=1
  q=4,s=2
  q=7,s=1,p=2
```

Audit detail:

```text
q=2, 6*2=0 was rechecked without requiring h=2*6=2.
The diagnostic gives r=6*0 in {1,3,4,7}, and the predicted r*6=1 closes
all four values.
```

Still open:

```text
remaining zero-avoiding source roles for q in {2,4,7}
whether the self-loop layer 6*6=6 has a different no-tail role
```

Next work should classify source-orbit roles, not enumerate arbitrary `h/s`
tails.

## Transfer Check: Neighboring Layer `6*6=2`

Date: 2026-05-31.

Neighboring layer:

```text
case45
7*0=5
6*5=5
6*6=2
```

The source row starts:

```text
6 -> 2
```

The zero-hit representative:

```text
6*2=0
```

then gives:

```text
6*0=r
0*(r*6)=2
r*6=pred0(2)=1
```

Diagnostic:

```text
r=6*0 in {1,3,4,7,8}
```

Targeted checks:

```text
r=1 -> closed
r=3 -> closed
r=4 -> closed
r=7 -> closed
r=8 -> closed
```

Interpretation:

```text
The eventual-zero mechanism transfers outside the original 6*6=8 layer.
This supports treating source-orbit ladder as a cross-layer role principle,
not merely a local q=6*8 trick.
```

### Eventual zero-hit representative in `6*6=2`

Date: 2026-05-31.

To test whether only the immediate zero-hit role transfers, the first
zero-avoiding source step was checked:

```text
case45
7*0=5
6*5=5
6*6=2
6*2=1
6*1=0
```

The ladder gives:

```text
6*0=r
0*(r*6)=1
r*6=pred0(1)=0
```

Diagnostic gave:

```text
r in {3,4,6,7,8}
```

Targeted checks:

```text
r=3 -> closed
r=4 -> closed
r=6 -> closed
r=7 -> closed
r=8 -> closed
```

Interpretation:

```text
Eventual zero-hit transfers to a neighboring layer as well.  The next unknown
is not this role, but the truly zero-avoiding successor 6*1 != 0.
```

Second eventual-zero transfer in `6*6=2`:

```text
6*6=2
6*2=1
6*1=3
6*3=0
```

The ladder gives:

```text
6*0=r
0*(r*6)=3
r*6=pred0(3)=2
```

Diagnostic:

```text
r in {4,6,7,8}
```

Targeted checks:

```text
r=4 -> closed
r=6 -> closed
r=7 -> closed
r=8 -> closed
```

Interpretation:

```text
The transferred eventual-zero role survives one more source step.  This
supports formulating the role by the final edge into 0, not by the initial
layer 6*6=k.
```

Closed zero-avoiding prefix in `6*6=2`:

```text
6*6=2
6*2=1
6*1=3
```

Diagnostic:

```text
6*3 in {0,4,6,7,8}
```

Results:

```text
6*3=0 -> eventual zero-hit, all r closed
6*3=4 -> closes after 6*4 in {0,6,7,8}
6*3=6 -> closed
6*3=7 -> closed
6*3=8 -> closed
```

In detail, under `6*3=4`:

```text
6*4=0 -> eventual zero-hit, r in {7,8} closed
6*4=6 -> source cycle 6 -> 2 -> 1 -> 3 -> 4 -> 6 closed
6*4=7 -> closed
6*4=8 -> closed
```

Conclusion:

```text
case45, 7*0=5, 6*5=5, 6*6=2, 6*2=1, 6*1=3
status: closed
```

This is the first closed genuinely zero-avoiding prefix in a neighboring
special-branch layer.

Sibling prefix:

```text
6*6=2
6*2=1
6*1=4
```

The zero-hit exit closes:

```text
6*4=0
6*0=r
r*6=pred0(4)=3
r in {3,6,7,8}
```

The remaining exits also close:

```text
6*4=3 -> closed
6*4=6 -> closed
6*4=7 -> closed
6*4=8 -> closed
```

The final direct successors:

```text
6*1=6 -> closed
6*1=7 -> closed
6*1=8 -> closed
```

Therefore:

```text
case45, 7*0=5, 6*5=5, 6*6=2, 6*2=1
status: closed
```

Interpretation:

```text
The first nonzero source successor after 6*6=2 is fully killed by the same
role split: eventual zero-hit plus compact zero-avoiding prefix collapse.
```

Second nonzero source value:

```text
6*6=2
6*2=3
```

Zero-hit exit:

```text
6*3=0
6*0=r
r*6=pred0(3)=2
r in {1,4,6,7,8}
```

closed for all admissible `r`.

The first nonzero sibling:

```text
6*3=1
```

has:

```text
6*1 in {0,4,6,7,8}
```

and closes completely:

```text
6*1=0 -> eventual zero-hit, all r closed
6*1=4 -> closed
6*1=6 -> closed
6*1=7 -> closed
6*1=8 -> closed
```

The remaining direct exits:

```text
6*3=6 -> closed
6*3=7 -> closed
6*3=8 -> closed
```

Therefore:

```text
case45, 7*0=5, 6*5=5, 6*6=2, 6*2=3
status: closed
```

Third nonzero source value:

```text
6*6=2
6*2=4
```

Zero-hit exit:

```text
6*4=0
6*0=r
r*6=pred0(4)=3
r in {1,3,6,7,8}
```

closed for all admissible `r`.

The first nonzero sibling:

```text
6*4=1
```

has:

```text
6*1 in {0,3,6,7,8}
```

and closes completely:

```text
6*1=0 -> eventual zero-hit, all r closed
6*1=3 -> closed
6*1=6 -> closed
6*1=7 -> closed
6*1=8 -> closed
```

The remaining direct exits:

```text
6*4=3 -> closed
6*4=6 -> closed
6*4=7 -> closed
6*4=8 -> closed
```

Therefore:

```text
case45, 7*0=5, 6*5=5, 6*6=2, 6*2=4
status: closed
```

Current layer status:

```text
6*6=2:
  6*2=0 closed by immediate zero-hit
  6*2=1 closed by prefix-collapse
  6*2=3 closed by prefix-collapse
  6*2=4 closed by prefix-collapse
  6*2=6 closed directly
  6*2=7 closed by zero-hit plus direct exits
  6*2=8 closed by zero-hit plus direct exits
  status: closed
```

Details for the last values:

```text
6*2=6 -> closed directly

6*2=7:
  6*7=0, 6*0=r, r*6=pred0(7)=6 -> all r closed
  6*7 in {1,3,4,6,8} -> closed

6*2=8:
  6*8=0, 6*0=r, r*6=pred0(8)=7 -> all r closed
  6*8 in {1,3,4,6,7} -> closed
```

Conclusion:

```text
case45, 7*0=5, 6*5=5, 6*6=2
status: closed
```

## Transfer Check: Neighboring Layer `6*6=3`

Date: 2026-05-31.

Neighboring layer:

```text
case45
7*0=5
6*5=5
6*6=3
```

The source row starts:

```text
6 -> 3
```

The zero-hit representative:

```text
6*3=0
```

then gives:

```text
6*0=r
0*(r*6)=3
r*6=pred0(3)=2
```

Diagnostic:

```text
r=6*0 in {1,2,4,7,8}
```

Targeted checks:

```text
r=1 -> closed
r=2 -> closed
r=4 -> closed
r=7 -> closed
r=8 -> closed
```

Interpretation:

```text
The zero-hit role transfers to a second neighboring layer.  The candidate is
now a cross-layer source-orbit principle for the special branch, not just a
local repair of the 6*6=8 layer.
```

First nonzero prefix-collapse representative:

```text
6*6=3
6*3=1
```

The direct check timed out at 60s, but the source split closed it.

Zero-hit exit:

```text
6*1=0
6*0=r
r*6=pred0(1)=0
r in {2,4,6,7,8}
```

closed for all admissible `r`.

The remaining exits:

```text
6*1=2 -> closed
6*1=4 -> closed
6*1=6 -> closed
6*1=7 -> closed
6*1=8 -> closed
```

Therefore:

```text
case45, 7*0=5, 6*5=5, 6*6=3, 6*3=1
status: closed
```

Interpretation:

```text
The prefix-collapse role transfers from the fully closed 6*6=2 layer into
6*6=3.
```

Pause point:

```text
6*6=3
6*3=2
direct check -> timeout at 60s
```

Next:

```text
diagnose row 6 and split by the next source edge, likely 6*2.
Do not count the timeout as evidence of openness; it only says direct search
is again the wrong shape.
```

Resolution:

```text
6*6=3
6*3=2
```

Diagnostic:

```text
6*2 in {0,1,4,6,7,8}
```

Zero-hit exit:

```text
6*2=0
6*0=r
r*6=pred0(2)=1
```

closed for all admissible `r`.  The remaining exits:

```text
6*2=1 -> closed
6*2=4 -> closed
6*2=6 -> closed
6*2=7 -> closed
6*2=8 -> closed
```

Therefore:

```text
case45, 7*0=5, 6*5=5, 6*6=3, 6*3=2
status: closed
```

Next successor:

```text
6*6=3
6*3=4
```

Direct check timed out, then source split closed it.

Diagnostic:

```text
6*4 in {0,1,2,6,7,8}
```

Zero-hit exit:

```text
6*4=0
6*0=r
r*6=pred0(4)=3
```

closed for all admissible `r`.  The remaining exits:

```text
6*4=1 -> closed
6*4=2 -> closed
6*4=6 -> closed
6*4=7 -> closed
6*4=8 -> closed
```

Therefore:

```text
case45, 7*0=5, 6*5=5, 6*6=3, 6*3=4
status: closed
```

Current status:

```text
6*6=3:
  6*3=0 closed by immediate zero-hit
  6*3=1 closed by prefix-collapse
  6*3=2 closed by prefix-collapse
  6*3=4 closed by prefix-collapse
  6*3=6 closed directly
  6*3=7 closed by zero-hit plus direct exits
  6*3=8 closed by zero-hit plus direct exits
  status: closed
```

Details for the last values:

```text
6*3=6 -> closed directly

6*3=7:
  6*7=0, 6*0=r, r*6=pred0(7)=6 -> all r closed
  6*7 in {1,2,4,6,8} -> closed

6*3=8:
  6*8=0, 6*0=r, r*6=pred0(8)=7 -> all r closed
  6*8 in {1,2,4,6,7} -> closed
```

Conclusion:

```text
case45, 7*0=5, 6*5=5, 6*6=3
status: closed
```

## Transfer Check: Neighboring Layer `6*6=4`

Date: 2026-05-31.

Neighboring layer:

```text
case45
7*0=5
6*5=5
6*6=4
```

Zero-hit representative:

```text
6*4=0
```

then gives:

```text
6*0=r
0*(r*6)=4
r*6=pred0(4)=3
```

Diagnostic:

```text
r=6*0 in {1,2,3,7,8}
```

Targeted checks:

```text
r=1 -> closed
r=2 -> closed
r=3 -> closed
r=7 -> closed
r=8 -> closed
```

Interpretation:

```text
The zero-hit role now transfers across 6*6 in {2,3,4}.  This suggests the
role is controlled by the source row-6 orbit and the fixed row-0 cycle, rather
than by the particular target layer 6*6=8.
```

## Boundary Check: Self-Loop Layer `6*6=6`

Date: 2026-05-31.

Self-loop layer:

```text
case45
7*0=5
6*5=5
6*6=6
```

Here the source orbit starts with:

```text
6 -> 6
```

so the earlier root zero-hit route from `6 -> k -> 0` does not apply directly.

A non-root zero-hit representative was tested:

```text
6*8=0
```

It gives:

```text
6*0=r
0*(r*6)=8
r*6=pred0(8)=7
```

Diagnostic:

```text
r=6*0 in {2,3,4,7}
```

Results:

```text
r=7 -> closed
r=2 -> timeout at 60s
r=3 -> timeout at 60s
```

For `r=2`, active diagnostics show row `6` remains the compact row:

```text
row 6 domain 92
```

Interpretation:

```text
The self-loop layer is a boundary for the current zero-hit mechanism.
Do not only raise limits.  The next invariant should treat 6*6=6 as a
self-loop/no-tail role, not as another ordinary eventual-zero case.
```

Resolution:

```text
double_fixed_self_loop_lemma.md
```

The boundary is resolved by the double-fixed exit:

```text
6*5=5
6*6=6
u=5*6
=> 5*u=5
```

All possible values:

```text
u in {1,2,3,7,8}
```

closed.  Thus:

```text
case45, 7*0=5, 6*5=5, 6*6=6
status: closed
```
