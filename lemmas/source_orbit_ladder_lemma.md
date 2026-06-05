# Source-Orbit Ladder Lemma

Date: 2026-05-27.

Status:

```text
candidate / repeated structural mechanism
```

Update 2026-05-31:

```text
candidate / role mechanism with explicit dependency on left-row permutations
```

Current role map:

```text
source_orbit_role_map.md
```

This file records the broader mechanism that emerged from the two-sided relay
square.

## General Ladder

In any finite E677 magma, every left row is a permutation and the inverse edge
chain holds:

```text
a*z=c  ==>  z = c*((a*c)*a)
```

Therefore, if a row has consecutive orbit edges:

```text
a*z0=z1
a*z1=z2
```

then:

```text
z1*(z2*a)=z0
```

Therefore a longer source orbit:

```text
a*z0=z1
a*z1=z2
a*z2=z3
a*z3=z4
```

creates a ladder of reverse constraints:

```text
z1*(z2*a)=z0
z2*(z3*a)=z1
z3*(z4*a)=z2
```

In the current work the source row is usually row `6`.

Important correction:

```text
This ladder should not be presented as a bare one-substitution consequence of
E677.  It uses the already established finite E677 permutation/inverse-edge
fact.
```

## Special Zero-Hit Rule In Case45

In case45, row `0` is fixed as the 9-cycle:

```text
0*0=1
0*1=2
0*2=3
0*3=4
0*4=5
0*5=6
0*6=7
0*7=8
0*8=0
```

So if the row-6 orbit has:

```text
6*q=0
6*0=t
```

then the ladder gives:

```text
0*(t*6)=q
```

Because row `0` is known, this forces:

```text
t*6 = pred0(q)
```

where `pred0(q)` is the predecessor of `q` in the row-0 cycle.

Examples:

```text
q=2 -> pred0(q)=1
q=8 -> pred0(q)=7
q=5 -> pred0(q)=4
```

This is a clean structural rule.  It should be used before branching inside
row `q`.

## Current Application

Current layer:

```text
case45
7*0=5
6*5=5
6*6=8
```

Current q-node:

```text
q=6*8=2
s=6*q=0
h=q*6=2
```

This contains:

```text
6*2=0
```

Let:

```text
r=6*0
```

The zero-hit rule gives:

```text
r*6=pred0(2)=1
```

Targeted check:

```text
r=1 -> closed
r=3 -> closed
r=4 -> closed
r=7 -> closed
```

Therefore:

```text
q=2
s=0
h=2
status: closed
```

Audit update 2026-05-31:

```text
The immediate zero-hit q=2 role was rechecked without the extra condition
h=2*6=2.
```

For:

```text
q=2
6*2=0
6*0=r
```

the ladder gives:

```text
r*6=pred0(2)=1
```

Diagnostic:

```text
r in {1,3,4,7}
```

All values closed:

```text
r=1 -> closed
r=3 -> closed
r=4 -> closed
r=7 -> closed
```

Therefore the role is:

```text
q=2, 6*2=0 closed
```

not merely the narrower earlier node:

```text
q=2, 6*2=0, h=2*6=2
```

## Relation To The Two-Sided Square

The two-sided square for:

```text
6*6=8
6*8=q
```

uses:

```text
h=q*6
s=6*q
r=s*6
8*h=6
q*r=8
```

When:

```text
s=0
```

the square should immediately be extended by the zero-hit rule:

```text
r=6*0
r*6=pred0(q)
```

This explains why `q=2, s=0` should not be treated as an arbitrary hard tail.

## Working Hypothesis

Hard q-tails in the special branch are controlled by how the source row-6 orbit
interacts with the known row-0 cycle.

Priority order:

```text
1. Continue the source row-6 orbit.
2. If it hits 0, apply the zero-hit rule.
3. If it avoids 0, classify the short source-orbit cycle or path.
4. Only then branch inside the active q-row.
```

## Next Structural Question

For the remaining q-values:

```text
q in {2,3,4,7}
```

do not enumerate h/s cases.  Ask:

```text
Does the source row-6 orbit from 8 hit 0 quickly?
If yes, use pred0(q).
If no, what short zero-avoiding source-orbit role appears?
```

This is the next candidate lemma path.

## Boundary Check 2026-05-28

The zero-hit rule was tested on a second representative:

```text
q=3
s=6*3=0
r=6*0
```

The rule predicts:

```text
r*6=pred0(3)=2
```

Diagnostic:

```text
r=6*0 in {1,2,4,7}
```

Results:

```text
r=2 -> closed
r=4 -> closed
r=7 -> closed
r=1 -> timeout
```

So the zero-hit rule is useful but not yet a complete closing lemma by itself.

The new special residue was:

```text
6*8=3
6*3=0
6*0=1
1*6=2
```

This should not be continued as an arbitrary branch.  It is a new role:

```text
source orbit hits 0, then immediately hits 1
8 -> 3 -> 0 -> 1
```

The next structural question becomes:

```text
What is special about the source row-6 orbit segment 8 -> q -> 0 -> 1?
```

Do not dig into this residue until this role is compared with the already
closed `q=2, s=0` residue.

## Update 2026-05-28: Zero-Hit-Plus-One Closed

The residue:

```text
8 -> 3 -> 0 -> 1
```

was tested by continuing the source row-6 orbit one more step:

```text
u=6*1
```

Diagnostic:

```text
u in {4,6,7}
```

Each value closed:

```text
u=4 -> closed
u=6 -> closed
u=7 -> closed
```

Therefore the full zero-hit representative:

```text
q=3
6*3=0
```

is now closed.

Structural meaning:

```text
If zero-hit leaves a residue 8 -> q -> 0 -> 1,
continue the source row-6 orbit once more.
```

The source-orbit ladder now has two useful roles:

```text
zero-hit:
  8 -> q -> 0

zero-hit-plus-one:
  8 -> q -> 0 -> 1
```

Both should be treated as structural roles before branching inside row `q`.

## Update 2026-05-31: q=4/q=7 zero-hit and delayed zero-hit

Immediate zero-hit was tested on the remaining top representatives:

```text
q=4
6*4=0
6*0=t
pred0(4)=3
=> t*6=3
```

Diagnostic:

```text
t=6*0 in {1,2,3,7}
```

All values closed:

```text
t=1 -> closed
t=2 -> closed
t=3 -> closed
t=7 -> closed
```

For:

```text
q=7
6*7=0
6*0=t
pred0(7)=6
=> t*6=6
```

Diagnostic:

```text
t=6*0 in {1,2,3,4}
```

All values closed:

```text
t=1 -> closed
t=2 -> closed
t=3 -> closed
t=4 -> closed
```

A first zero-avoiding representative was also tested:

```text
q=4
6*4=1
6*1=0
```

This is a delayed zero-hit role:

```text
8 -> 4 -> 1 -> 0
```

It gives:

```text
6*0=r
r*6=pred0(1)=0
```

Diagnostic:

```text
r=6*0 in {2,3,7}
```

All values closed:

```text
r=2 -> closed
r=3 -> closed
r=7 -> closed
```

A second delayed zero-hit representative repeated the same role:

```text
q=4
6*4=2
6*2=0
```

It gives:

```text
6*0=r
r*6=pred0(2)=1
```

Diagnostic:

```text
r=6*0 in {1,3,7}
```

All values closed:

```text
r=1 -> closed
r=3 -> closed
r=7 -> closed
```

A longer representative from a different `q` also followed the same eventual
zero-hit logic:

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

It gives:

```text
6*0=r
r*6=pred0(2)=1
```

Admissible values:

```text
r in {3,4}
```

Both closed:

```text
r=3 -> closed
r=4 -> closed
```

Conclusion:

```text
source-orbit ladder is now a real candidate role mechanism.
It is not yet a complete proof of the whole 6*6=8 layer.
The next useful object is source_orbit_role_map.md.
```

## Update 2026-05-31: Transfer to neighboring layer `6*6=2`

The same zero-hit mechanism was tested outside the original `6*6=8` layer.

Neighboring layer:

```text
case45
7*0=5
6*5=5
6*6=2
```

Zero-hit representative:

```text
6*2=0
```

Then:

```text
6*0=r
r*6=pred0(2)=1
```

Diagnostic:

```text
r in {1,3,4,7,8}
```

All values closed:

```text
r=1 -> closed
r=3 -> closed
r=4 -> closed
r=7 -> closed
r=8 -> closed
```

Conclusion:

```text
The source-orbit zero-hit mechanism transfers to at least one neighboring
special-branch layer.  This strengthens the candidate lemma status.
```

## Update 2026-05-31: Transfer to neighboring layer `6*6=3`

A second neighboring layer was tested:

```text
case45
7*0=5
6*5=5
6*6=3
```

Zero-hit representative:

```text
6*3=0
```

Then:

```text
6*0=r
r*6=pred0(3)=2
```

Diagnostic:

```text
r in {1,2,4,7,8}
```

All values closed:

```text
r=1 -> closed
r=2 -> closed
r=4 -> closed
r=7 -> closed
r=8 -> closed
```

Conclusion:

```text
The same source-orbit zero-hit role now transfers to two neighboring layers:
6*6=2 and 6*6=3.
```

## Update 2026-05-31: Transfer to neighboring layer `6*6=4`

Third neighboring layer:

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

Then:

```text
6*0=r
r*6=pred0(4)=3
```

Diagnostic:

```text
r in {1,2,3,7,8}
```

All values closed:

```text
r=1 -> closed
r=2 -> closed
r=3 -> closed
r=7 -> closed
r=8 -> closed
```

Conclusion:

```text
The source-orbit zero-hit role transfers across 6*6 in {2,3,4}.
```

## Boundary 2026-05-31: Self-loop layer `6*6=6`

The remaining neighboring layer behaves differently:

```text
case45
7*0=5
6*5=5
6*6=6
```

The source row starts with a self-loop:

```text
6 -> 6
```

A non-root zero-hit representative was tested:

```text
6*8=0
6*0=r
r*6=pred0(8)=7
```

Results:

```text
r=7 -> closed
r=2 -> timeout at 60s
r=3 -> timeout at 60s
```

Conclusion:

```text
The current zero-hit mechanism transfers across 6*6 in {2,3,4,8}, but the
self-loop layer 6*6=6 is a boundary.  It likely needs a self-loop/no-tail
invariant rather than higher timeouts.
```

Resolution:

```text
double_fixed_self_loop_lemma.md
```

The self-loop boundary closes by:

```text
6*5=5
6*6=6
u=5*6
=> 5*u=5
```

Diagnostic:

```text
u=5*6 in {1,2,3,7,8}
```

All values closed:

```text
u=1 -> closed
u=2 -> closed
u=3 -> closed
u=7 -> closed
u=8 -> closed
```
