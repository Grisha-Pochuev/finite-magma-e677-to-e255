# T5 Layer `6*6=8`: Row-8 Relay Progress

Date: 2026-05-26.

## Status

```text
paused / structural pivot
```

Scope:

```text
case45
7*0=5
6*5=5
6*6=8
```

## Structural Rule

Use the row-6 orbit relay:

```text
6*z0=z1
6*z1=z2
=> z1*(z2*6)=z0
```

For:

```text
6*6=8
q=6*8
h=q*6
```

the relay gives:

```text
8*h=6
```

So the intended first split is:

```text
q=6*8
h=q*6
8*h=6
```

Diagnostic:

```text
q=6*8 in {0,1,2,3,4,6,7}
```

## Current Coverage

Immediate q-values:

```text
q=0 -> h=0*6=7, plus 8*7=6 -> none, 0.95s, 1 node
q=6 -> h=6*6=8, plus 8*8=6 -> none, 0.76s, 1 node
```

Direct checks for:

```text
q in {1,2,3,4,7}
```

timed out, so they should not be continued by raising direct timeouts.

## Closed q=1

For:

```text
q=1
6*8=1
```

direct check timed out:

```text
q=1 -> timeout at 25.24s, 37 nodes
```

The relay layer is:

```text
h=1*6
8*h=6
```

Admissible h-values used:

```text
h in {2,3,4,5,8}
```

The first two h-values timed out directly:

```text
h=2 -> timeout at 25.16s, 554 nodes
h=3 -> timeout at 25.41s, 417 nodes
```

Diagnostics showed row `6` was the compact active row.  The useful next split
was the next source-orbit edge:

```text
6*6=8
6*8=1
6*1=s
=> 1*(s*6)=8
```

For each:

```text
h in {2,3,4,5,8}
```

the split:

```text
s=6*1 in {0,2,3,4,6,7}
```

closed all values.

Therefore:

```text
6*6=8
q=6*8=1
status: closed
```

## Remaining Frontier

```text
q=6*8 in {2,3,4,7}
```

## Pivot Note 2026-05-27

Do not continue by mechanically closing:

```text
q=2,3,4,7
```

The test on `q=2` showed that the one-sided continuation is insufficient:

```text
q=2
s=6*2
```

timed out for several `s` values.  Even the explicit relay node:

```text
s=0
0*6=7
2*7=8
```

still timed out.  Adding the other side:

```text
h=2*6
8*h=6
```

gave mixed results:

```text
h=0 -> closed
h=3 -> closed
h=2 -> timeout
```

Therefore the next object is not a longer q-case list.  The next object is:

```text
two_sided_relay_square_lemma.md
```

Recommended next move:

```text
Compare q=1 and q=2 structurally.
Find the missing diagonal constraint before doing more local checks.
```

## Update 2026-05-27: q=2, s=0, h=2 closed structurally

The stubborn node was:

```text
q=2
s=6*2=0
2*7=8
h=2*6=2
8*2=6
```

It closed by continuing the source row-6 orbit one more step:

```text
r=6*0
```

From:

```text
6*2=0
6*0=r
```

the row-6 relay gives:

```text
0*(r*6)=2
```

Since:

```text
0*1=2
```

we get the concrete condition:

```text
r*6=1
```

Checked values:

```text
r=1 -> none, 15.25s, 18 nodes
r=3 -> none, 12.35s, 47 nodes
r=4 -> none, 12.22s, 33 nodes
r=7 -> none, 8.79s, 1 node
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
q=2, 6*2=0 was rechecked without requiring h=2*6=2.
```

The same zero-hit rule:

```text
6*0=r
r*6=pred0(2)=1
```

closed all admissible values:

```text
r=1 -> closed
r=3 -> closed
r=4 -> closed
r=7 -> closed
```

So the immediate zero-hit role for `q=2` is fully closed, not only the
previously recorded `h=2` subnode.

Structural meaning:

```text
When the two-sided square stalls, continue the source row-6 orbit:
6*6=8, 6*8=q, 6*q=s, 6*s=t
=> s*(t*6)=q.
```

This is recorded in:

```text
two_sided_relay_square_lemma.md
```

## Boundary Check 2026-05-28

Second zero-hit representative:

```text
q=3
6*3=0
r=6*0
pred0(3)=2
=> r*6=2
```

Results:

```text
r=2 -> none, 20.96s, 1717 nodes
r=4 -> none, 21.59s, 513 nodes
r=7 -> none, 20.16s, 18 nodes
r=1 -> timeout at 25.32s, 1601 nodes
```

Conclusion:

```text
zero-hit is a useful role split, but not complete.
new residue: 6*8=3, 6*3=0, 6*0=1, 1*6=2.
```

Do not continue this residue mechanically.  It needs a structural comparison
of source orbit roles.

## Update 2026-05-31: Source-Orbit Role Map

The source-orbit ladder was corrected to depend explicitly on the finite E677
fact that left rows are permutations, via the inverse edge chain:

```text
a*z=c  ==>  z = c*((a*c)*a)
```

Thus:

```text
6*z0=z1
6*z1=z2
=> z1*(z2*6)=z0
```

Immediate zero-hit was tested for the remaining top q-values:

```text
q=4, 6*4=0:
  6*0=t in {1,2,3,7}
  t*6=pred0(4)=3
  all t closed

q=7, 6*7=0:
  6*0=t in {1,2,3,4}
  t*6=pred0(7)=6
  all t closed
```

A first delayed zero-hit representative was tested:

```text
q=4
6*4=1
6*1=0
6*0=r in {2,3,7}
r*6=pred0(1)=0
```

All `r` values closed.

A second delayed zero-hit representative repeated the pattern:

```text
q=4
6*4=2
6*2=0
6*0=r in {1,3,7}
r*6=pred0(2)=1
```

All `r` values closed.

A longer eventual zero-hit representative in a different `q` was also checked:

```text
q=7
6*7=1
6*1=2
6*2=0
6*0=r in {3,4}
r*6=pred0(2)=1
```

Both `r` values closed.

Structural status:

```text
source-orbit ladder is a candidate role mechanism;
the whole q-layer is not yet closed;
remaining work is role classification for zero-avoiding source orbits.
```
