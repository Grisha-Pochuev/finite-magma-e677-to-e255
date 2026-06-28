# Two-Sided Relay Square Lemma

Date: 2026-05-27.

Status:

```text
candidate / strategic pivot
```

This file records the first structural pivot.  The next work should not be
mechanical closure of the remaining `q` branches.

Update: the square has now been strengthened into a source-orbit ladder.  See:

```text
source_orbit_ladder_lemma.md
```

## General Relay Used

In any finite E677 magma every left row is a permutation.  The basic inverse
edge chain is:

```text
a*z=c  ==>  z=c*((a*c)*a)
```

Equivalently, if one row has two consecutive orbit edges:

```text
a*z0=z1
a*z1=z2
```

then:

```text
z1*(z2*a)=z0
```

This is the existing row-orbit relay.

## Current Source Situation

Current special branch:

```text
case45
7*0=5
6*5=5
6*6=8
```

Let:

```text
q = 6*8
h = q*6
s = 6*q
r = s*6
```

The row-6 orbit gives two relay constraints:

```text
6*6=8
6*8=q
=> 8*(q*6)=6
=> 8*h=6
```

and:

```text
6*8=q
6*q=s
=> q*(s*6)=8
=> q*r=8
```

So the correct object is not only one cell `q*6` or one cell `6*q`.
It is the two-sided square:

```text
        right side:  h = q*6,  8*h = 6
source edge: 6*8 = q
        left side:   s = 6*q,  r=s*6,  q*r = 8
```

Compact form:

```text
6*6=8
6*8=q
h=q*6
s=6*q
r=s*6
8*h=6
q*r=8
```

## Evidence

In the layer:

```text
7*0=5
6*5=5
6*6=8
```

we have:

```text
q=6*8 in {0,1,2,3,4,6,7}
```

Immediate closures:

```text
q=0 -> h=7 and 8*7=6 -> closed
q=6 -> h=8 and 8*8=6 -> closed
```

Closed representative:

```text
q=1
```

For `q=1`, direct q and direct h checks timed out, but the source-orbit side:

```text
s=6*1
1*(s*6)=8
```

closed all admissible h-values:

```text
h in {2,3,4,5,8}
```

Boundary example:

```text
q=2
```

For `q=2`, the one-sided source split:

```text
s=6*2
```

did not close directly.  Even the explicit relay node:

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

This is the signal that the two-sided square is the right next object, but it
is not yet a proved lemma.

## Working Hypothesis

The hard tails are not arbitrary branch noise.  They appear when the row-6
orbit reaches a `q` for which the two sides:

```text
h=q*6
s=6*q
```

do not collapse independently.

The next lemma should classify when the square:

```text
8*h=6
q*(s*6)=8
```

forces contradiction, and when it needs a third diagonal constraint.

## Update 2026-05-27: Third Source-Rung Signal

The first stubborn node was:

```text
q=2
s=6*q=0
h=q*6=2
```

So the active facts were:

```text
6*6=8
6*8=2
6*2=0
2*7=8
2*6=2
8*2=6
```

This is a secondary self-type:

```text
2*6=2
```

A short diagnostic showed row `6` remained the compact active row.  The missing
move was not to branch inside row `2`, but to continue the source row-6 orbit
one more step:

```text
r=6*0
```

Using the row-6 orbit relay on:

```text
6*2=0
6*0=r
```

gives:

```text
0*(r*6)=2
```

Since row `0` is the fixed cycle:

```text
0*1=2
```

this forces:

```text
r*6=1
```

Targeted check:

```text
r=1 -> closed
r=3 -> closed
r=4 -> closed
r=7 -> closed
```

Therefore the stubborn node:

```text
q=2
s=0
h=2
```

is closed by the third source-rung:

```text
6*0=r
r*6=1
```

This is stronger than the previous square view.  The candidate lemma should be
upgraded from a two-sided square to a source-orbit ladder:

```text
6*6=8
6*8=q
6*q=s
6*s=t

8*(q*6)=6
q*(s*6)=8
s*(t*6)=q
```

In the special subcase `s=0`, the last relation becomes concrete because row
`0` is known.

The upgraded file is:

```text
source_orbit_ladder_lemma.md
```

## Possible Third Diagonal

From:

```text
q*6=h
```

the inverse edge chain also gives:

```text
6 = h*((q*h)*q)
```

From:

```text
6*q=s
```

it gives:

```text
q = s*((6*s)*6)
```

These may be the missing diagonal constraints for the stubborn `q=2` tail.
Do not assume they close the case automatically; test them only as targeted
lemma checks.

After the third source-rung check, the more promising missing constraint is:

```text
if 6*s=t, then s*(t*6)=q
```

This stays inside the source row-6 orbit and should be tried before branching
inside row `q`.

## Do Not Do Next

Do not continue with:

```text
q=2
h=2*6
s=6*2
```

as a plain list of cases.

Do not mechanically enumerate all remaining:

```text
q in {2,3,4,7}
```

The previous computation already showed that the one-sided split is no longer
enough.

## Next Structural Task

Compare `q=1` and `q=2` as roles, not as branches:

```text
q=1 closes when s=6*q is fixed.
q=2 does not close when s=6*q is fixed, even with q*(s*6)=8.
```

Find the structural difference:

```text
Is q=1 special because it is the predecessor of 2 in row 0?
Is q=2 hard because it matches the bad square target b2?
Does q=2 require the diagonal 6 = h*((q*h)*q)?
Does q=2 require pairing h and s before any row can become small?
Does q=2 require continuing the source row-6 orbit until it hits row 0 or
another known row?
```

Only after answering one of these should computation resume.
