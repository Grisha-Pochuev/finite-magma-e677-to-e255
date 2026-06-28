# Row-5 Descent Bridge Lemma

Date: 2026-06-03.

Status:

```text
candidate bridge / diagnostic support
```

Scope:

```text
case45
7*0=5
6*5=5
low-layer L3 zero-hit:
  6*6=k
  6*k=0
  6*0=r
  r*6=pred0(k)
```

This file records the next step upward after the low-layer meta-lemma.  The
direct attempt to close the hard `k=4` branch by adding only:

```text
5*r=4
```

did not significantly speed the solver.  The active object is not the single
cell `5*r=4`, but the descent through row `5`.

## Structural Facts

The general row-0 predecessor ladder gives:

```text
z*(succ0(z)*0)=pred0(z)
```

Important instances:

```text
5*(6*0)=4
4*(5*0)=3
```

In the zero-hit notation:

```text
6*0=r
```

the first instance is:

```text
5*r=4
```

The next descent marker is:

```text
a=5*0
```

and the second instance gives:

```text
4*a=3
```

So the hard zero-hit tail should descend:

```text
row 6 return -> row 5 bridge -> row 4 predecessor
```

not:

```text
enumerate r
```

## Diagnostic Evidence

Hard representative tested:

```text
k=4
r=1
6*6=4
6*4=0
6*0=1
1*6=3
5*1=4
```

Adding only `5*1=4` did not close quickly:

```text
without 5*r=4 -> timeout at 25s
with    5*r=4 -> timeout at 25s
```

Row diagnostics showed row `5` is the active row, not row `p=pred0(k)`.

Next marker:

```text
w=5*6
```

For `k=4,r=1`, admissible values were:

```text
w in {2,3,7,8}
```

The split result:

```text
w=7 -> closed
w=2,3,8 -> not closed directly
```

For the residual values `w=2,3,8`, the next marker:

```text
a=5*0
4*a=3
```

closed all checked representatives:

```text
w=2, a in {1,3,8} -> all closed
w=3, a in {1,2,8} -> all closed
w=8, a in {1,2,3} -> all closed
```

Sanity check on another broad return value:

```text
k=4
r=2
```

representatives also closed with the same descent marker:

```text
w=1,a=1 -> closed
w=3,a=1 -> closed
w=8,a=8 -> closed
```

## Candidate Interpretation

The hard L3 zero-hit residue is not controlled by row `p` alone.  The better
role map is:

```text
6*0=r
5*r=4
w=5*6
a=5*0
4*a=3
```

This is a descending row-0 ladder:

```text
6 -> 5 -> 4
```

The next proof attempt should show symbolically that after the row-5 bridge,
the value `a=5*0` forces a contradiction through row `4`, instead of closing
the remaining `a` values by computation.

## Row-5 Orbit Continuation

After the marker:

```text
a=5*0
4*a=3
```

the active row remains row `5`.  The next natural source-orbit marker is:

```text
b=5*a
```

The row-5 source-orbit ladder gives:

```text
5*0=a
5*a=b
=> a*(b*5)=0
```

Diagnostic representative:

```text
k=4
r=1
w=5*6=2
a=5*0=3
4*3=3
```

Rowscores showed `5*3` was one of the most active cells:

```text
b=5*3 in {0,6,7,8}
```

Splitting by this source-orbit marker closed all values:

```text
b=0 -> closed
b=6 -> closed
b=7 -> closed
b=8 -> closed
```

Interpretation:

```text
The descent bridge is not a one-cell trick.  It continues as a row-5 source
orbit:
  0 -> a -> b
with the relay:
  a*(b*5)=0.
```

This gives a clearer proof target than enumerating `r`, `w`, or `a`
independently.

## Late Row-5 Orbit Tail

The previous line still hid one small residual.  For:

```text
b=7 or b=8
```

continue the row-5 orbit:

```text
c=b*5
```

The relay from:

```text
5*0=3
5*3=b
```

is:

```text
3*(b*5)=0
```

so:

```text
3*c=0
```

Diagnostics show the late tail is almost completely killed by `c`:

```text
b=7, all c-values close immediately.
b=8, all c-values close immediately except c=3.
```

The unique residual is:

```text
b=8
c=8*5=3
3*3=0
```

In that residual, row `5` has only four candidates.  Continue the same orbit:

```text
e=5*8
```

Allowed values:

```text
e in {1,6}
```

Both close:

```text
e=1 -> closed
e=6 -> closed
```

So the late row-5 orbit tail is closed in the hard representative:

```text
5*0=3
5*3=8
8*5=3
5*8=e
e in {1,6}
```

The next symbolic task is to prove why the unique self-return:

```text
5*3=8
8*5=3
3*3=0
```

cannot survive the two possibilities for `5*8`.

## Next Proof Obligations

```text
1. Derive the admissible domain for w=5*6 from injectivity and E677.
2. Explain why w=7 is a direct exit.
3. For residual w, prove that a=5*0 with 4*a=3 is a killer descent.
4. Use the row-5 source-orbit continuation b=5*a and a*(b*5)=0 to remove
   the remaining residuals symbolically.
5. Prove the late tail:
   b=8, c=3, 3*3=0, e=5*8 in {1,6}.
6. Transfer the same argument from k=4,r=1 to all L3 zero-hit returns.
```

Do not continue by raising the timeout on:

```text
6*6=4
6*4=1
```

The useful next work is to turn the row-5 descent bridge into a symbolic
lemma.

## Update 2026-06-03: Late `e=6` Tail Status

The late file `row3_late_trap_lemma.md` now records the refined closure of:

```text
5*3=8
8*5=3
3*3=0
5*8=6
```

Under this base, row diagnostics give:

```text
3*5 in {4,6}
```

and each value separately contradicts the propagated E677 constraints:

```text
3*5=4 -> closed
3*5=6 -> closed
```

Thus the hard representative:

```text
k=4
r=1
w=2
a=3
b=8
c=3
e=6
```

is now symbolically closed at the row-3 trap level.

The two final exclusions are:

```text
3*5=4 -> forces 5*5=0, 3*8=5, 8*7=0; then E677 with x=7,y=8 gives 7=3.
3*5=6 -> forces 5*7=0, 7*1=0, 1*1=0; then 0*(1*1)=1 violates the bad-element diagonal obstruction.
```

The remaining task for the bridge is therefore higher-level: transfer the
row-5 descent and row-3 late trap from this hard representative to all L3
zero-hit returns.  Do not branch below `e=6` again.
