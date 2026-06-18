# Special Branch Role Split Lemma

Date: 2026-05-31.

Status:

```text
candidate / organizing role split
```

Scope:

```text
case45
7*0=5
6*5=5
```

This file collects the current structural split for the special branch.  It is
not a final proof of the whole branch yet.  Its purpose is to prevent the next
work from becoming blind case enumeration.

## Role 1: Source-Orbit Zero-Hit

If the row-6 source orbit has consecutive edges:

```text
6*z0=z1
6*z1=z2
```

then the finite E677 inverse-edge rule gives:

```text
z1*(z2*6)=z0
```

In case45, row `0` is the fixed cycle:

```text
0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 0
```

So if the source orbit hits `0`:

```text
6*p=0
6*0=r
```

then:

```text
0*(r*6)=p
r*6=pred0(p)
```

Confirmed transfer layers:

```text
6*6=2, 6*2=0 -> r*6=pred0(2)=1 -> closed for all r
6*6=3, 6*3=0 -> r*6=pred0(3)=2 -> closed for all r
6*6=4, 6*4=0 -> r*6=pred0(4)=3 -> closed for all r
6*6=8, q=6*8 in {2,4,7}, 6*q=0 -> closed for all admissible r/t
```

Interpretation:

```text
This role is controlled by the source row-6 orbit and the fixed row-0 cycle,
not by the particular layer 6*6=8.
```

## Role 2: Eventual Zero-Hit

The same mechanism applies when `0` appears after more than one source step:

```text
6*z0=z1
6*z1=z2
...
6*p=0
6*0=r
```

The final step still forces:

```text
r*6=pred0(p)
```

Confirmed representatives in the `6*6=8` layer:

```text
8 -> 4 -> 1 -> 0
8 -> 4 -> 2 -> 0
8 -> 7 -> 1 -> 2 -> 0
```

All checked admissible return values close.

First transfer representative outside `6*6=8`:

```text
6*6=2
6*2=1
6*1=0
```

Then:

```text
6*0=r
0*(r*6)=1
r*6=pred0(1)=0
```

Targeted checks closed all admissible return values:

```text
r in {3,4,6,7,8}
```

This shows that eventual zero-hit also transfers to a neighboring layer, not
only immediate zero-hit.

Longer transfer representative in the same neighboring layer:

```text
6*6=2
6*2=1
6*1=3
6*3=0
```

Then:

```text
6*0=r
r*6=pred0(3)=2
```

Targeted checks closed all admissible return values:

```text
r in {4,6,7,8}
```

This supports the broader formulation:

```text
whenever the row-6 source orbit eventually reaches 0, the next return edge is
forced by pred0 of the predecessor of 0.
```

## Role 2a: Closed Zero-Avoiding Prefix

After:

```text
6*6=2
6*2=1
6*1=3
```

diagnostic gives:

```text
6*3 in {0,4,6,7,8}
```

The `6*3=0` exit is eventual zero-hit and closes by:

```text
6*0=r
r*6=pred0(3)=2
```

The first genuinely zero-avoiding branch:

```text
6*3=4
```

has:

```text
6*4 in {0,6,7,8}
```

where:

```text
6*4=0 closes by eventual zero-hit;
6*4=6 closes as the source cycle 6 -> 2 -> 1 -> 3 -> 4 -> 6;
6*4=7 closes directly;
6*4=8 closes directly.
```

The remaining exits:

```text
6*3=6
6*3=7
6*3=8
```

also close directly.  Therefore:

```text
case45, 7*0=5, 6*5=5, 6*6=2, 6*2=1, 6*1=3
status: closed
```

Structural reading:

```text
The first tested zero-avoiding prefix does not create a new residual type.
It either returns to eventual zero-hit or collapses as a short source-cycle /
direct-killer sublayer.
```

The sibling prefix:

```text
6*6=2
6*2=1
6*1=4
```

has the same domain size and the same role shape.  Its zero-hit exit:

```text
6*4=0
6*0=r
r*6=pred0(4)=3
```

closes for all admissible `r`, and the remaining exits:

```text
6*4 in {3,6,7,8}
```

also close.  The remaining direct successors:

```text
6*1=6
6*1=7
6*1=8
```

close as well.  Therefore the whole node:

```text
case45, 7*0=5, 6*5=5, 6*6=2, 6*2=1
status: closed
```

Structural reading:

```text
The first nonzero successor after 6*6=2 does not leave a live residual.
Once 6*2=1, the next source step is killed either by eventual zero-hit or by
a compact zero-avoiding prefix collapse.
```

The next nonzero source value also closes:

```text
6*6=2
6*2=3
```

Its zero-hit exit:

```text
6*3=0
6*0=r
r*6=pred0(3)=2
```

closes for all admissible `r`.  The first nonzero sibling:

```text
6*3=1
```

has:

```text
6*1 in {0,4,6,7,8}
```

where `6*1=0` closes by eventual zero-hit and the other exits close directly.
The remaining direct exits:

```text
6*3=6
6*3=7
6*3=8
```

also close.  Therefore:

```text
case45, 7*0=5, 6*5=5, 6*6=2, 6*2=3
status: closed
```

Structural reading:

```text
The prefix-collapse role repeats for two different nonzero successors,
6*2=1 and 6*2=3.
```

The third nonzero source value repeats the same pattern:

```text
6*6=2
6*2=4
```

Its zero-hit exit:

```text
6*4=0
6*0=r
r*6=pred0(4)=3
```

closes for all admissible `r`.  The first nonzero sibling:

```text
6*4=1
```

has:

```text
6*1 in {0,3,6,7,8}
```

where `6*1=0` closes by eventual zero-hit and the other exits close directly.
The remaining direct exits:

```text
6*4=3
6*4=6
6*4=7
6*4=8
```

also close.  Therefore:

```text
case45, 7*0=5, 6*5=5, 6*6=2, 6*2=4
status: closed
```

Structural reading:

```text
The prefix-collapse role now repeats for 6*2 in {1,3,4}.
Together with the earlier zero-hit closure 6*2=0, most of the layer 6*6=2
is now explained by the same source-orbit role split.
```

The remaining values also close:

```text
6*2=6 -> closed directly
6*2=7 -> closes after splitting by 6*7
6*2=8 -> closes after splitting by 6*8
```

For `6*2=7`, the zero-hit exit:

```text
6*7=0
6*0=r
r*6=pred0(7)=6
```

closes for all admissible `r`, and the remaining exits:

```text
6*7 in {1,3,4,6,8}
```

close directly.

For `6*2=8`, the zero-hit exit:

```text
6*8=0
6*0=r
r*6=pred0(8)=7
```

closes for all admissible `r`, and the remaining exits:

```text
6*8 in {1,3,4,6,7}
```

close directly.

Therefore:

```text
case45, 7*0=5, 6*5=5, 6*6=2
status: closed
```

Structural reading:

```text
The role split is now strong enough to close a whole neighboring layer:
6*6=2.  This makes it a serious local lemma candidate for the special branch,
not just a collection of q-node repairs.
```

Open point:

```text
This is not yet a complete classification of every zero-avoiding source orbit.
The next useful checks should test one representative at a time and classify
its role, not enumerate arbitrary row entries.
```

## Role 3: Double-Fixed Self-Loop Boundary

The layer:

```text
6*6=6
```

is different because the source orbit starts:

```text
6 -> 6
```

The zero-hit role does not start at the root.  A non-root zero-hit test
`6*8=0` timed out for two return values, so the correct next invariant was
not a larger timeout.

Instead:

```text
6*5=5
6*6=6
```

and E677 with `x=5, y=6` gives:

```text
u=5*6
5*u=5
```

All possible values:

```text
u in {1,2,3,7,8}
```

close.  Therefore:

```text
case45, 7*0=5, 6*5=5, 6*6=6
status: closed
```

## Current Boundary Of The Candidate

The split now explains:

```text
zero-hit representatives across 6*6 in {2,3,4,8}
self-loop layer 6*6=6
```

It does not yet prove:

```text
all zero-avoiding source orbits in 6*6=2,3,4,8
```

Next structurally meaningful task:

```text
Use the closed 6*6=2 layer as the model case.
Next test whether the same full-layer closure transfers to 6*6=3, starting
with one nonzero value after the already closed zero-hit branch 6*3=0.
```

First transfer into `6*6=3`:

```text
6*6=3
6*3=1
```

The direct check timed out, but the source split repeated the model pattern.
The zero-hit exit:

```text
6*1=0
6*0=r
r*6=pred0(1)=0
```

closed for all admissible `r`, and all remaining exits:

```text
6*1 in {2,4,6,7,8}
```

closed directly.  Therefore:

```text
case45, 7*0=5, 6*5=5, 6*6=3, 6*3=1
status: closed
```

Interpretation:

```text
The prefix-collapse role transfers from the closed layer 6*6=2 into the next
neighboring layer 6*6=3.
```

Current pause point in the same layer:

```text
6*6=3
6*3=2
```

Direct check:

```text
timeout at 60s
```

This should be treated like the earlier nonzero successors: diagnose the next
source edge rather than increasing the timeout.  If the next source edge is
`6*2=0`, the expected source-orbit condition is:

```text
6*0=r
r*6=pred0(2)=1
```

Resolution:

```text
6*6=3
6*3=2
```

The row-6 diagnostic gave:

```text
6*2 in {0,1,4,6,7,8}
```

The zero-hit exit:

```text
6*2=0
6*0=r
r*6=pred0(2)=1
```

closed for all admissible `r`, and all remaining exits:

```text
6*2 in {1,4,6,7,8}
```

closed directly.  Therefore:

```text
case45, 7*0=5, 6*5=5, 6*6=3, 6*3=2
status: closed
```

Interpretation:

```text
The transfer into 6*6=3 is now confirmed for two nonzero successors,
6*3=1 and 6*3=2.
```

Third nonzero successor:

```text
6*6=3
6*3=4
```

Direct check timed out, but the source split again closed it.  Diagnostic:

```text
6*4 in {0,1,2,6,7,8}
```

The zero-hit exit:

```text
6*4=0
6*0=r
r*6=pred0(4)=3
```

closed for all admissible `r`, and all remaining exits:

```text
6*4 in {1,2,6,7,8}
```

closed directly.  Therefore:

```text
case45, 7*0=5, 6*5=5, 6*6=3, 6*3=4
status: closed
```

Current status in layer `6*6=3`:

```text
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

Therefore:

```text
case45, 7*0=5, 6*5=5, 6*6=3
status: closed
```

Structural reading:

```text
The special-branch role split now closes two full neighboring layers:
6*6=2 and 6*6=3.
```
