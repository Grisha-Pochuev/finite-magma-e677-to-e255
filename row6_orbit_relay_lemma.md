# Row-6 Orbit Relay Lemma

Date: 2026-05-25.

## Status

```text
candidate / general orbit relay extracted from senior-column fallback
```

This file upgrades `senior_column_fallback_lemma.md`.

The previous fallback used only the first senior marker:

```text
6*8=m
r=6*m
h=r*6
=> m*h=8
```

The actual mechanism is more general: every edge in the orbit of row `6`
creates a return edge one row later.

## General Orbit Relay

In any finite E677 magma, every left row is a permutation and the inverse edge
chain holds:

```text
a*z=c  ==>  z = c*((a*c)*a)
```

Apply this with `a=6`.

If the row-6 orbit contains two consecutive edges:

```text
6*z0=z1
6*z1=z2
```

then:

```text
z0 = z1*(z2*6)
```

So row `z1` sends the column `(z2*6)` back to the previous orbit point `z0`.

This is the row-6 orbit relay:

```text
z0 --6--> z1 --6--> z2
        gives
z1*(z2*6)=z0
```

## Relation To Senior Fallback

The senior fallback is the first instance with:

```text
z0=8
z1=m
z2=r
```

Thus:

```text
6*8=m
6*m=r
=> m*(r*6)=8
```

This is exactly the earlier formula:

```text
h=r*6
m*h=8
```

## Zero-Hit Sublayer

If the row-6 orbit hits `0` as the second successor:

```text
6*z0=z1
6*z1=0
```

then row `0` is already known in case45:

```text
0*6=7
```

Therefore the relay becomes explicit:

```text
z1*7=z0
```

For the senior marker:

```text
6*8=m
6*m=0
=> m*7=8
```

This explains the previously observed zero-relay sublayer.

## Zero Pass-Through Formula

There is a second useful zero case.  If the row-6 orbit has:

```text
6*z0=0
6*0=z2
```

then the orbit relay gives:

```text
z0 = 0*(z2*6)
```

Since row `0` is the fixed 9-cycle, this determines `z2*6` uniquely:

```text
z2*6 = pred0(z0)
```

Here `pred0(z0)` means the unique element `p` such that:

```text
0*p=z0
```

Example used below:

```text
6*1=0
6*0=k
0*0=1
=> k*6=0
```

This is why the prefix `8 -> 1 -> 0` becomes much stronger after choosing the
next edge.

## Current No-Bridge Evidence

Current frontier:

```text
case45
7*0=t, t in {2,3}
6*t=5
6*6=6
6*5=t
no bridge row a with a*t=5 and a*5=6
```

In the no-bridge branch, fixing only:

```text
6*8=m
```

leaves:

```text
t=2: row6 domain <= 90
t=3: row6 domain <= 90
```

After fixing the second orbit edge:

```text
6*m=r
```

the row-6 domain becomes small in tested representatives:

```text
t=2, m=1, r=3: row6 domain 16
t=2, m=1, r=0: row6 domain 18
t=3, m=1, r=2: row6 domain 16
```

This is not yet a closure proof.  It is evidence that the right structural
object is the row-6 orbit containing `8`, not a raw enumeration of all row-6
permutations.

## Important Negative Result

Trying to branch over the 16 row-6 candidates after:

```text
t=2
no bridge
6*8=1
6*1=3
```

timed out at the first-branch diagnostic limit.

Interpretation:

```text
do not continue by enumerating the 16 candidates of row 6
```

The next split must be by the role of the row-6 orbit:

```text
does the orbit hit 0?
does it close a short cycle before hitting 0?
which return edge z1*(z2*6)=z0 becomes explicit?
```

## Short Zero-Avoiding 3-Cycle Check

The first zero-avoiding orbit type tested was a short cycle through the senior
point:

```text
8 -> m -> r -> 8
```

This means:

```text
6*8=m
6*m=r
6*r=8
```

In the `t=2` no-bridge branch, the representative:

```text
m=1
r=3
6*3=8
```

left only four possible row-6 shapes:

```text
4 3 5 8 0 2 6 7 1
4 3 5 8 7 2 6 0 1
7 3 5 8 0 2 6 4 1
7 3 5 8 4 2 6 0 1
```

All four closed:

```text
status: none
```

In the neighboring `t=3` no-bridge branch, the analogous representative:

```text
m=1
r=2
6*2=8
```

left only three possible row-6 shapes:

```text
4 2 8 5 0 3 6 7 1
4 2 8 5 7 3 6 0 1
7 2 8 5 4 3 6 0 1
```

All three closed:

```text
status: none
```

Interpretation:

```text
short zero-avoiding 3-cycles of the senior orbit are not a promising live
counterexample shape; they behave like a finite killer sublayer.
```

This still is not a general proof for all zero-avoiding orbits.  It is a
strong diagnostic that the next zero-avoiding test should be a longer orbit
or a cycle using `0` in the other residual component, not another 3-cycle with
the same role.

## First Zero-Hit Check Beyond The First Marker

After:

```text
t=2
no bridge
8 -> 1 -> 3
```

the zero-hit branch:

```text
6*3=0
```

gives:

```text
8 -> 1 -> 3 -> 0
```

The orbit relay gives the explicit return edge:

```text
3*7=1
```

because row `0` has `0*6=7`.

Diagnostic:

```text
status: ok
row 3 forced: 7->1
row6 domain: 4
```

The four remaining row-6 shapes were:

```text
4 3 5 0 7 2 6 8 1
4 3 5 0 8 2 6 7 1
8 3 5 0 4 2 6 7 1
8 3 5 0 7 2 6 4 1
```

All four closed:

```text
zh1: status none, 12.41s, 106 nodes
zh2: status none, 12.47s, 86 nodes
zh3: status none, 12.66s, 243 nodes
zh4: status none, 15.74s, 909 nodes
```

Interpretation:

```text
early zero-hit in the senior orbit also behaves as a killer sublayer
```

## Full Closure Of The Prefix `8 -> 1 -> 3`

For:

```text
t=2
no bridge
6*8=1
6*1=3
```

the row-6 domain after closure was:

```text
16
```

The possible next values were:

```text
6*3 in {0,4,7,8}
```

Each role was checked:

```text
6*3=0  early zero-hit      -> all 4 row6 shapes closed
6*3=8  short 3-cycle       -> all 4 row6 shapes closed
6*3=4  longer zero-avoiding -> all 4 row6 shapes closed
6*3=7  longer zero-avoiding -> all 4 row6 shapes closed
```

The concrete longer zero-avoiding closures:

```text
6*3=4:
  l4a status none, 13.89s, 90 nodes
  l4b status none, 8.29s, 1 node
  l4c status none, 14.49s, 146 nodes
  l4d status none, 8.37s, 1 node

6*3=7:
  l7a status none, 11.82s, 70 nodes
  l7b status none, 8.16s, 1 node
  l7c status none, 14.51s, 29 nodes
  l7d status none, 8.11s, 1 node
```

Conclusion:

```text
the full orbit prefix 8 -> 1 -> 3 is closed in the t=2 no-bridge self layer
```

This should be treated as a finite local certificate, not yet as a general
proof for all prefixes.  The next prefix to test should be role-distinct,
for example:

```text
8 -> 1 -> 0
```

## Full Closure Of The Prefix `8 -> 1 -> 0`

For:

```text
t=2
no bridge
6*8=1
6*1=0
```

the row-6 domain was:

```text
18
```

The possible next values were:

```text
6*0 in {3,4,8}
```

The orbit relay through row `0` gives a strong explicit rule:

```text
6*1=0
6*0=k
=> 0*(k*6)=1
=> k*6=0
```

because row `0` has `0*0=1`.

Checks:

```text
6*0=3:
  forced 3*6=0
  row6 domain 6
  all 6 row6 shapes closed

6*0=4:
  row6 domain 4
  all 4 row6 shapes closed

6*0=8:
  contradiction
```

Concrete closures:

```text
6*0=3:
  zp3a status none, 8.14s, 1 node
  zp3b status none, 8.04s, 1 node
  zp3c status none, 7.10s, 1 node
  zp3d status none, 8.60s, 1 node
  zp3e status none, 7.47s, 1 node
  zp3f status none, 8.33s, 1 node

6*0=4:
  zp4a status none, 7.36s, 1 node
  zp4b status none, 8.53s, 1 node
  zp4c status none, 8.30s, 1 node
  zp4d status none, 8.04s, 1 node
```

Conclusion:

```text
t=2 no-bridge prefix 8 -> 1 -> 0 is closed
```

Together with the previous section, this closes two role-distinct second
edges after `6*8=1`:

```text
6*1=0
6*1=3
```

## Full Closure Of The Senior 2-Cycle `8 <-> 1`

The next role-distinct prefix was:

```text
t=2
no bridge
6*8=1
6*1=8
```

This is a short senior 2-cycle:

```text
8 -> 1 -> 8
```

Diagnostic:

```text
status: ok
row6 domain: 16
```

Splitting by the image of `0` in row `6`:

```text
6*0 in {3,4,7}
```

gave finite row-6 layers:

```text
6*0=3 -> 6 shapes
6*0=4 -> 6 shapes
6*0=7 -> 2 shapes
```

All 14 shapes closed.

Concrete closures:

```text
6*0=3:
  cy2_k3_a none, 10.74s, 73 nodes
  cy2_k3_b none, 11.68s, 518 nodes
  cy2_k3_c none, 12.80s, 265 nodes
  cy2_k3_d none, 8.36s, 1 node
  cy2_k3_e none, 12.99s, 33 nodes
  cy2_k3_f none, 7.38s, 1 node

6*0=4:
  cy2_k4_a none, 12.74s, 81 nodes
  cy2_k4_b none, 12.77s, 105 nodes
  cy2_k4_c none, 11.34s, 70 nodes
  cy2_k4_d none, 7.51s, 1 node
  cy2_k4_e none, 12.84s, 70 nodes
  cy2_k4_f none, 8.44s, 1 node

6*0=7:
  cy2_k7_a none, 13.56s, 37 nodes
  cy2_k7_b none, 13.91s, 341 nodes
```

Conclusion:

```text
t=2 no-bridge prefix 8 -> 1 -> 8 is closed
```

In the layer:

```text
t=2
no bridge
6*8=1
```

closed second-edge values are now:

```text
6*1 in {0,3,8}
```

Remaining second-edge values:

```text
6*1 in {4,7}
```

## Closure Of The Remaining Pair `6*1 in {4,7}`

The two remaining second-edge values after `6*8=1` were:

```text
6*1=4
6*1=7
```

Diagnostics:

```text
6*1=4 -> row6 domain 16
6*1=7 -> row6 domain 18
```

Both closed by direct targeted search without enumerating every row-6 shape
manually:

```text
6*1=4:
  status none
  time 27.24s
  nodes 2866
  dead ends 2856

6*1=7:
  status none
  time 27.29s
  nodes 1945
  dead ends 1933
```

Conclusion:

```text
t=2
no bridge
6*8=1
status: closed
```

This is the first complete marker closure in the no-bridge senior orbit layer.

The closed second-edge split was:

```text
6*1 in {0,3,4,7,8}
```

All values close.

## Closure Of Senior Fixed-Point Marker `6*8=8`

The next role-distinct marker was:

```text
t=2
no bridge
6*8=8
```

This is a senior fixed-point in row `6`:

```text
8 -> 8
```

The orbit relay gives:

```text
8*(8*6)=8
```

So the natural split is not by another row-6 cell, but by:

```text
k=8*6
```

Diagnostics:

```text
row8 domain: 904
k=8*6 in {0,2,3,4,5}
```

Representative check for `k=0` forced:

```text
8*0=8
```

as predicted by the relay.  It also compressed row `8` to domain `35`.

All `k` values closed:

```text
k=0:
  status none
  time 24.33s
  nodes 57
  dead ends 54

k=2:
  status none
  time 34.08s
  nodes 2665
  dead ends 2632

k=3:
  status none
  time 37.93s
  nodes 2496
  dead ends 2463

k=4:
  status none
  time 35.98s
  nodes 2038
  dead ends 2018

k=5:
  status none
  time 35.82s
  nodes 1688
  dead ends 1663
```

Conclusion:

```text
t=2
no bridge
6*8=8
status: closed
```

This is the second complete marker closure in the no-bridge senior orbit
layer.  Unlike `6*8=1`, it closes by transferring activity into row `8`.

## Closure Of Remaining Low/Far Markers `6*8 in {3,4,7}`

After the complete closures:

```text
6*8=1
6*8=8
```

the remaining markers in the `t=2` no-bridge self layer were:

```text
6*8 in {3,4,7}
```

Each has the same broad shape:

```text
row6 domain: 84
```

For `6*8=3`, diagnostics showed the natural next orbit split:

```text
6*3 in {0,1,4,7,8}
```

But the whole marker closed directly by targeted search:

```text
6*8=3:
  status none
  time 52.73s
  nodes 8752
  dead ends 8711

6*8=4:
  status none
  time 49.81s
  nodes 10576
  dead ends 10539

6*8=7:
  status none
  time 55.11s
  nodes 10821
  dead ends 10778
```

Conclusion:

```text
t=2
no bridge
6*8 in {3,4,7}
status: closed
```

Combining all marker closures:

```text
6*8 in {1,3,4,7,8}
```

gives:

```text
t=2
no bridge
status: closed
```

This is a major local result.  It does not close the bridge branch for `t=2`,
and it does not close `t=3`, but it proves that absence of a bridge is not a
live counterexample route in the `t=2` self layer.

## Transfer To `t=3`: Marker `6*8=1`

Update 2026-05-25.

The neighboring no-bridge self layer is:

```text
t=3
7*0=3
6*3=5
6*6=6
6*5=3
no bridge
```

Start with the same senior marker:

```text
6*8=1
```

Diagnostic:

```text
row6 domain: 90
6*1 in {0,2,4,7,8}
```

All second-edge values closed by targeted search:

```text
6*1=0:
  status none
  time 19.72s
  nodes 19
  dead ends 18

6*1=2:
  status none
  time 27.62s
  nodes 1904
  dead ends 1895

6*1=4:
  status none
  time 27.39s
  nodes 2204
  dead ends 2195

6*1=7:
  status none
  time 27.24s
  nodes 1986
  dead ends 1977

6*1=8:
  status none
  time 24.67s
  nodes 1419
  dead ends 1412
```

Conclusion:

```text
t=3
no bridge
6*8=1
status: closed
```

This confirms that the senior-orbit marker closure transfers from `t=2` to
`t=3`; only the role label changes from `6*1=3` to `6*1=2`.

## Transfer To `t=3`: Fixed-Point Marker `6*8=8`

For:

```text
t=3
no bridge
6*8=8
```

the same fixed-point relay applies:

```text
8*(8*6)=8
```

Diagnostic:

```text
row6 domain: 78
row8 domain: 904
```

Split by:

```text
k=8*6 in {0,2,3,4,5}
```

All layers closed:

```text
k=0 -> status none, 25.69s, 68 nodes
k=2 -> status none, 31.14s, 1615 nodes
k=3 -> status none, 32.96s, 1817 nodes
k=4 -> status none, 36.76s, 1362 nodes
k=5 -> status none, 30.46s, 1211 nodes
```

Conclusion:

```text
t=3
no bridge
6*8=8
status: closed
```

## Transfer To `t=3`: Remaining Low/Far Markers

The remaining markers in the `t=3` no-bridge self layer were:

```text
6*8 in {2,4,7}
```

All closed by direct targeted search:

```text
6*8=2:
  status none
  time 46.67s
  nodes 6429
  dead ends 6399

6*8=4:
  status none
  time 50.30s
  nodes 7920
  dead ends 7888

6*8=7:
  status none
  time 48.46s
  nodes 8095
  dead ends 8062
```

Combining with:

```text
6*8=1 closed
6*8=8 closed
```

gives:

```text
t=3
no bridge
status: closed
```

So the no-bridge senior-orbit fallback now closes both neighboring self layers:

```text
t=2 no bridge closed
t=3 no bridge closed
```

## Candidate Lemma Form

A possible next lemma is:

```text
In the no-bridge self layer, the residual work is controlled by the orbit of
8 under left multiplication by 6.  Every two-step segment of that orbit gives a
forced return edge.  If the orbit hits 0, the return edge becomes explicit
because row 0 is fixed.
```

This is currently a candidate, not a final proof.

## Next Step

Do not enumerate all values of `m`, `r`, or all row-6 candidates.

Classify the residual row-6 orbit containing `8` by role:

```text
8 -> m -> r -> ...
```

The meaningful dichotomy is:

```text
zero-hit orbit:
  some second successor is 0, giving z1*7=z0

zero-avoiding orbit:
  the orbit closes before using 0; this should be checked as a separate
  structural obstruction
```

The next targeted diagnostic should test one zero-avoiding short-cycle
representative, not another arbitrary `(m,r)` value.

## T5 Zero-Pass-Through Application

Update 2026-05-25:

The special top branch:

```text
7*0=5
6*5=5
```

has a closed zero-pass-through layer:

```text
6*6=0
```

The relay gives:

```text
6*6=0
r=6*0
=> r*6=5
```

because `0*5=6` in the fixed row-0 cycle.

Coverage:

```text
r=1 -> closed
r=2 -> closed
r=3 -> closed
r=4 -> closed
r=8 -> closed after split by s=6*8 in {1,2,3,4,7}
```

This is recorded in:

```text
t5_zero_pass_through_lemma.md
```

## T5 Row-7 Relay Application

Update 2026-05-25:

The special top branch also has a closed layer:

```text
7*0=5
6*5=5
6*6=7
```

The row-6 orbit relay gives:

```text
6*6=7
q=6*7
h=q*6
=> 7*h=6
```

Coverage:

```text
q=1 closes directly
q=2,3,4 close by the h-layer
h=8 tails close by 8*8 in {2,3,4,5}
```

This is recorded in:

```text
t5_k7_row7_relay_lemma.md
```
