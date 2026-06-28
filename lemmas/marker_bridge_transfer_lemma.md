# Marker Bridge Transfer Lemma

Date: 2026-05-24.

## Status

```text
candidate / general relay identity
```

This file records the new bridge formulation for transferring the row-6
mechanism from the closed branch:

```text
case45
7*0=4
```

to the remaining top branches:

```text
7*0=2
7*0=3
7*0=5
```

The main point: the old formula

```text
6*0=s*6
```

is not universal. In the closed branch `7*0=4`, row `0` worked because it was a
bridge row.

## General Identity

Assume finite E677, so left rows are permutations.

If we have two chains:

```text
d*z=c
d*c=s
```

and

```text
a*z=c
a*c=b
```

then the inverse E677 chain gives:

```text
z = c*((d*c)*d) = c*(s*d)
z = c*((a*c)*a) = c*(b*a)
```

Since row `c` is injective:

```text
s*d = b*a
```

This is the marker bridge transfer.

## Case45 Top-Branch Form

In `case45`, for a top branch:

```text
7*0=t
```

the ladder gives:

```text
6*t=5
```

Let:

```text
s=6*5
u=s*6
```

Then the inverse chain gives:

```text
5*u=t
```

If there is a bridge row `a`:

```text
a*t=5
a*5=6
```

then the same inverse chain gives:

```text
5*(6*a)=t
```

and row `5` is injective, so:

```text
6*a=u=s*6
```

## Why `7*0=4` Was Diagonal

In the closed branch `t=4`, the bridge row was `a=0`:

```text
0*4=5
0*5=6
```

Therefore:

```text
6*0=s*6
```

So the old `6*0` marker was not intrinsically special. It was the bridge marker
for the path:

```text
4 -> 5 -> 6
```

inside row `0`.

## What Changes For `7*0=2,3`

For `t=2` and `t=3`, row `0` is not the same bridge:

```text
0*2=3
0*3=4
```

So `6*0=s*6` should not be expected automatically.

Short diagnostics and a subagent check suggested:

```text
t=2, 6*6=6, 6*5=2: a candidate marker is 6*8
t=3, 6*6=6, 6*5=3: after the natural layer, 6*8 appears again
```

This matches the bridge view: if `a=8` satisfies

```text
8*t=5
8*5=6
```

then the forced transferred marker is:

```text
6*8=s*6
```

## Sanity Checks

For `t=2`, the node:

```text
7*0=2
6*2=5
6*6=6
6*5=2
8*2=5
8*5=6
```

remains alive as a diagnostic node. The branch explicitly violating the bridge
equality closes immediately:

```text
2*6=2
6*8=0
status: none
```

For `t=3`, the analogous node:

```text
7*0=3
6*3=5
6*6=6
6*5=3
8*3=5
8*5=6
```

also remains alive as a diagnostic node. The branch explicitly violating the
bridge equality closes immediately:

```text
3*6=3
6*8=0
status: none
```

These checks are not a closure of the top branches. They confirm that the new
manual identity is consistent with the diagnostics.

## Bridge Candidate Map In The Self Layer

The first useful test was the self layer:

```text
6*6=6
6*5=t
```

For `t=2`, one-row diagnostics gave:

```text
possible bridge rows: a in {1,3,4,7,8}
immediate contradictions: a in {0,2,5,6}
```

For `t=3`, the same role pattern appeared:

```text
possible bridge rows: a in {1,2,4,7,8}
immediate contradictions: a in {0,3,5,6}
```

Role form:

```text
possible a are exactly outside {0,t,5,6}
```

Here "possible" means locally alive under the row-domain diagnostic, not a full
branch closure.

## Exclusivity Of A Bridge

The bridge is not unique by diagnostics, but it is exclusive in any actual
model.

If both `a` and `a'` are bridge rows, then:

```text
6*a=s*6
6*a'=s*6
```

Therefore:

```text
6*a=6*a'
```

Since row `6` is injective:

```text
a=a'
```

So the bridge layer is a controlled split:

```text
at most one bridge row a can occur
```

The local solver did not immediately exploit this manual lemma: a sample
double-bridge check timed out after ten seconds.  This is a solver limitation,
not a mathematical contradiction to the identity.

## Next Question

Do not mechanically close `7*0=2` and `7*0=3`.

The next question is now sharper than before:

```text
either prove that a bridge row exists,
or understand the no-bridge branch.
```

If a bridge exists, it is unique and the old row-6 transfer extends by replacing:

```text
0 -> a
6*0 -> 6*a
```

If no bridge exists, the row-6 transfer has reached its boundary and the next
split should move to the upper markers `7*7` or `1*1`.

## No-Bridge Diagnostic

To test whether bridge existence is forced, the local tool was extended with a
pair-forbid diagnostic:

```text
a:t:5~5:6
```

meaning:

```text
not (a*t=5 and a*5=6)
```

In the self layer, forbidding all locally possible bridges does not close the
branch.

For `t=2`, forbid:

```text
a in {1,3,4,7,8}
```

Result:

```text
status: ok
row 6 domain: 486
```

For `t=3`, forbid:

```text
a in {1,2,4,7,8}
```

Result:

```text
status: ok
row 6 domain: 468
```

So bridge existence is not forced by the current constraints.

However, the no-bridge branch still keeps activity in row `6`.  The smallest
row-6 marker remains the senior-column marker:

```text
6*8
```

Role notation:

```text
8=b1
```

Therefore the next fallback after bridge-transfer is:

```text
no bridge -> split by 6*b1
```

not a return to the old universal `6*0` split.

## Senior-Column Fallback Size

The no-bridge row-6 histograms give a bounded fallback.

For `t=2`:

```text
6*8 in {0,1,3,4,7,8}
counts: 0:54, 1:90, 3:84, 4:84, 7:90, 8:84
```

For `t=3`:

```text
6*8 in {0,1,2,4,7,8}
counts: 0:54, 1:90, 2:84, 4:78, 7:84, 8:78
```

Thus:

```text
no-bridge + fixed 6*b1=m -> row 6 has at most 90 candidates
```

A representative check:

```text
t=2
no bridge
6*8=0
status: ok
best row: 6
best domain: 54
```

This is not yet a conceptual closure.  It is a small finite certificate layer:
if the bridge branch is absent, the next useful row remains row `6`, but it is
cut down to a small domain by the senior-column marker.

## T=2 Bridge Representative `a=8`

Update 2026-05-25.

Current bridge layer:

```text
t=2
6*2=5
6*6=6
6*5=2
a*2=5
a*5=6
```

For the bridge representative:

```text
a=8
8*2=5
8*5=6
```

the bridge transfer gives:

```text
6*8=2*6
```

So the natural finite split is:

```text
u=2*6=6*8
```

Diagnostics gave:

```text
u in {0,1,3,4,7,8}
```

The `u=8` layer was immediately contradictory. The other layers closed by
targeted search:

```text
u=0 -> status none, 12.55s, 107 nodes
u=1 -> status none, 12.37s, 85 nodes
u=3 -> status none, 20.23s, 634 nodes
u=4 -> status none, 19.47s, 932 nodes
u=7 -> status none, 24.79s, 691 nodes
```

Conclusion:

```text
t=2
bridge row a=8
status: closed
```

This confirms that bridge-transfer is not only a diagnostic equality; it gives
a practical closure split for at least one bridge row.

## T=2 Bridge Representative `a=1`

Update 2026-05-25.

Second bridge representative:

```text
a=1
1*2=5
1*5=6
```

The bridge transfer gives:

```text
6*1=2*6
```

Natural split:

```text
u=2*6=6*1
```

Diagnostics:

```text
u in {0,1,3,4,7,8}
u=1 -> contradiction
```

The remaining layers closed:

```text
u=0 -> status none, 9.55s, 93 nodes
u=3 -> status none, 25.30s, 817 nodes
u=4 -> status none, 20.36s, 1077 nodes
u=7 -> status none, 23.32s, 457 nodes
u=8 -> status none, 23.27s, 440 nodes
```

Conclusion:

```text
t=2
bridge row a=1
status: closed
```

Together with `a=8`, this supports the working bridge-closure pattern:

```text
a*2=5
a*5=6
=> split by u=2*6=6*a
```

## T=2 Bridge Representative `a=3`

Update 2026-05-25.

Third bridge representative:

```text
a=3
3*2=5
3*5=6
```

Bridge transfer:

```text
6*3=2*6
```

Split:

```text
u=2*6=6*3
```

Diagnostics:

```text
u in {0,1,3,4,7,8}
u=1 -> contradiction
u=3 -> contradiction
```

The remaining layers closed:

```text
u=0 -> status none, 9.74s, 33 nodes
u=4 -> status none, 12.31s, 320 nodes
u=7 -> status none, 11.83s, 332 nodes
u=8 -> status none, 17.26s, 639 nodes
```

Conclusion:

```text
t=2
bridge row a=3
status: closed
```

Closed bridge rows so far:

```text
a in {1,3,8}
```

Remaining bridge rows:

```text
a in {4,7}
```

## T=2 Bridge Representatives `a=4` And `a=7`

Update 2026-05-25.

For:

```text
a=4
4*2=5
4*5=6
```

bridge-transfer gives:

```text
6*4=2*6
```

Split:

```text
u=2*6=6*4
```

Diagnostics:

```text
u=0 -> contradiction
u=4 -> contradiction
u in {1,3,7,8} -> live
```

Live layers closed:

```text
u=1 -> status none, 7.43s, 53 nodes
u=3 -> status none, 9.17s, 71 nodes
u=7 -> status none, 10.66s, 87 nodes
u=8 -> status none, 10.68s, 73 nodes
```

For:

```text
a=7
7*2=5
7*5=6
```

bridge-transfer gives:

```text
6*7=2*6
```

Split:

```text
u=2*6=6*7
```

Diagnostics:

```text
u=7 -> contradiction
u in {0,1,3,4,8} -> live
```

Live layers closed:

```text
u=0 -> status none, 8.52s, 29 nodes
u=1 -> status none, 9.92s, 49 nodes
u=3 -> status none, 20.07s, 210 nodes
u=4 -> status none, 20.51s, 384 nodes
u=8 -> status none, 15.89s, 176 nodes
```

Conclusion:

```text
t=2
bridge rows a in {4,7}
status: closed
```

Combining all bridge rows:

```text
a in {1,3,4,7,8}
```

gives:

```text
t=2
bridge branch
status: closed
```

Combined with the no-bridge closure from `row6_orbit_relay_lemma.md`, this
closes the whole `t=2` self layer:

```text
t=2
6*2=5
6*6=6
6*5=2
status: closed
```

## Transfer To `t=3`: Bridge Representative `a=8`

Update 2026-05-25.

Neighboring bridge layer:

```text
t=3
6*3=5
6*6=6
6*5=3
8*3=5
8*5=6
```

Bridge-transfer gives:

```text
6*8=3*6
```

Split:

```text
u=3*6=6*8
```

Diagnostics:

```text
u=8 -> contradiction
u in {0,1,2,4,7} -> live
```

Live layers closed:

```text
u=0 -> status none, 7.59s, 51 nodes
u=1 -> status none, 19.37s, 655 nodes
u=2 -> status none, 9.94s, 128 nodes
u=4 -> status none, 15.73s, 517 nodes
u=7 -> status none, 17.50s, 422 nodes
```

Conclusion:

```text
t=3
bridge row a=8
status: closed
```

This confirms that bridge-transfer also works in the neighboring `t=3`
self layer.

## Transfer To `t=3`: Remaining Bridge Rows

Update 2026-05-25.

Bridge rows for `t=3`:

```text
a in {1,2,4,7,8}
```

The representative `a=8` is closed above.  The remaining bridge rows also
close by the same bridge-transfer split:

```text
a*3=5
a*5=6
=> 6*a=3*6
```

For `a=1`:

```text
u=1 -> contradiction
u=0 -> none, 7.64s, 84 nodes
u=2 -> none, 7.86s, 70 nodes
u=4 -> none, 15.08s, 544 nodes
u=7 -> none, 17.81s, 394 nodes
u=8 -> none, 18.39s, 392 nodes
```

For `a=2`:

```text
u=2 -> contradiction
u=0 -> none, 6.55s, 86 nodes
u=1 -> none, 10.71s, 404 nodes
u=4 -> none, 10.07s, 324 nodes
u=7 -> none, 13.81s, 311 nodes
u=8 -> none, 17.24s, 448 nodes
```

For `a=4`:

```text
u=0 -> contradiction
u=2 -> contradiction
u=4 -> contradiction
u=1 -> none, 10.92s, 94 nodes
u=7 -> none, 11.61s, 82 nodes
u=8 -> none, 12.99s, 138 nodes
```

For `a=7`:

```text
u=7 -> contradiction
u=0 -> none, 8.77s, 22 nodes
u=1 -> none, 13.79s, 70 nodes
u=2 -> none, 11.96s, 204 nodes
u=4 -> none, 20.28s, 276 nodes
u=8 -> none, 13.43s, 127 nodes
```

Conclusion:

```text
t=3
bridge branch
status: closed
```

Combined with `row6_orbit_relay_lemma.md`, this closes the whole neighboring
self layer:

```text
t=3
7*0=3
6*3=5
6*6=6
6*5=3
status: closed
```
