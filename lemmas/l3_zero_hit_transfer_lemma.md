# L3 Zero-Hit Transfer Lemma

Date: 2026-06-03.

Status:

```text
candidate transfer lemma / row-5 descent route
```

Scope:

```text
case45
7*0=5
6*5=5
6*6=k
k in {2,3,4}
L3 zero-hit:
  6*k=0
  6*0=r
  r*6=pred0(k)
```

This file records the current higher-level target after the late `e=6`
residual was closed symbolically in `row3_late_trap_lemma.md`.

## General L3 Normal Form

The source-orbit zero-hit gives:

```text
6*k=0
6*0=r
=> r*6=pred0(k)
```

The row-0 predecessor ladder also gives:

```text
5*(6*0)=4
```

so:

```text
5*r=4
```

This means L3 is not only a return in row `6`; it immediately transfers to row
`5`.

## Shared Row-`k` Marker

Closure diagnostics for representatives in `k=2`, `k=3`, and the previously
studied `k=4` showed the same forced row-`k` pair:

```text
k*5=7
k*7=6
```

For example:

```text
k=2, r=1 -> 2*5=7, 2*7=6
k=3, r=1 -> 3*5=7, 3*7=6
k=4       -> 4*5=7, 4*7=6 in the hard late base
```

This pair is symbolic, not merely diagnostic.

First, apply the source-orbit ladder to:

```text
6*k=0
6*0=r
```

or directly to the segment:

```text
6 -> k -> 0
```

It gives:

```text
k*(0*6)=6
```

Since:

```text
0*6=7
```

we get:

```text
k*7=6
```

Now use E677 with:

```text
x=7
y=k
```

Since:

```text
k*7=6
6*k=0
7*0=5
```

we get:

```text
7 = k*(7*((k*7)*k))
  = k*(7*(6*k))
  = k*(7*0)
  = k*5
```

so:

```text
k*5=7
```

Thus L3 has two synchronized transfers:

```text
row 6 return -> row 5 bridge
row k marker -> fixed pair k*5=7, k*7=6
```

The row-`k` marker is now a proved subpiece of the candidate transfer lemma.

## Row-5 Descent Route

The active route is:

```text
6*0=r
5*r=4
w=5*6
a=5*0
4*a=3
b=5*a
a*(b*5)=0
```

Interpretation:

```text
row 6 return -> row 5 bridge -> row 4 predecessor -> row 5 source orbit
```

The first part of this route is symbolic.  Let:

```text
w=5*6
```

From the inverse-edge chain applied to:

```text
6*5=5
```

we get:

```text
5 = 5*((6*5)*6)
  = 5*(5*6)
  = 5*w
```

Thus:

```text
5*6=w
5*w=5
```

So row `5` contains a short source orbit:

```text
6 -> w -> 5
```

The source-orbit ladder on this segment gives:

```text
w*(5*5)=6
```

This is the next general row-5 marker.  The hard representative used:

```text
w=2
```

but the proof should treat `w` first and only then descend to:

```text
a=5*0
```

## The `k=4` Domain For `w`

For the hard low layer:

```text
k=4
```

the marker above gives an exact symbolic restriction:

```text
w in {1,2,3,7,8} \ {r}
```

Reason:

```text
w != 4
```

because `5*r=4`, and if `w=4` then `5*6=5*r`, forcing `6=r`.

```text
w != 5
```

because `5*6=w` and `5*w=5`; if `w=5`, row `5` sends both `6` and `5` to
`5`.

```text
w != 6
```

because if `w=6`, then `5*6=6`, but `5*w=5` is the same cell and would force
`6=5`.

```text
w != r
```

because `5*w=5`, while `5*r=4`.

Finally:

```text
w != 0
```

in the `k=4` layer.  If `w=0`, then `5*6=0`, and `5*w=5` gives:

```text
5*0=5
```

Let:

```text
a=5*0
```

Then `a=5`.  But the row-0 predecessor ladder gives:

```text
4*a=3
```

so:

```text
4*5=3
```

while the proved row-`k` marker for `k=4` gives:

```text
4*5=7
```

contradiction.

Thus, for `k=4`, the only possible `w=5*6` values are:

```text
w in {1,2,3,7,8} \ {r}
```

This matches the diagnostics:

```text
r=1 -> w in {2,3,7,8}
r=2 -> w in {1,3,7,8}
```

The hard representative was:

```text
k=4
r=1
w=5*6=2
a=5*0=3
b=5*a=8
c=b*5=3
e=5*8
```

## Late Row-3 Trap

When:

```text
a=3
5*3=8
8*5=3
3*3=0
```

the final split:

```text
e=5*8 in {1,6}
```

is symbolically closed.

For:

```text
e=1
```

row `8` injectivity and row `5` collision close the branch.

For:

```text
e=6
```

the residual reduces to:

```text
3*5 in {4,6}
```

and both values are symbolically impossible:

```text
3*5=4 -> forces 8*7=0; E677 with x=7,y=8 gives 7=3.
3*5=6 -> forces 1*1=0; then 0*(1*1)=1 violates the bad-element diagonal obstruction.
```

So the late row-3 trap is closed as a reusable sublemma.

## Remaining Transfer Obligation

The current gap is not below the late trap.  The current gap is transferring
the descent route from the hard representative to all L3 zero-hit returns.

The proved row-`k` marker suggests a sharper split:

```text
k=4:
  row k is row 4, the same row used in the descent marker 4*(5*0)=3.
  Therefore the row-k marker and the row-5 descent interact directly.
  This is the hard case that reaches the row-3 late trap.

k=2 or k=3:
  row k is not the descent row 4.
  The marker k*5=7, k*7=6 should close the zero-hit return earlier or route it
  into the already closed low-layer role split.
```

So the next transfer proof should not treat all `k` uniformly too soon.
The likely correct structure is:

```text
L3 zero-hit
  -> universal row-k marker: k*7=6, k*5=7
  -> universal row-5 bridge: 5*r=4
  -> if k=4, row-k and row-4 merge, giving the row-5 descent / row-3 trap
  -> if k=2,3, the row-k marker should close before the late trap
```

Precise obligation:

```text
For every admissible L3 zero-hit return
  6*6=k
  6*k=0
  6*0=r
  r*6=pred0(k)

show that the row-5 descent either:
  closes before the late trap, or
  reaches the late row-3 trap above.
```

Do not continue by branching below:

```text
e=5*8
```

That part is closed.

## Next Useful Check

The next proof step is now one layer lower in the `k=4` descent, but still
above the late trap.

Current proved `k=4` reduction:

```text
L3 zero-hit with k=4
=> w=5*6 in {1,2,3,7,8} \ {r}
```

The value:

```text
w=7
```

is a separate quick-exit role; it should be explained or certified separately,
not forced into the late-trap proof.

For the remaining values:

```text
w in {1,2,3,8} \ {r}
```

continue to the descent marker:

```text
a=5*0
4*a=3
```

For the representative:

```text
k=4
r=1
w=2
```

the `a`-layer has:

```text
a=5*0 in {1,3,8}
```

The value:

```text
a=1
```

is a quick-exit role.  A closure trace forces:

```text
1*7=0
7*1=6
7*8=7
```

and the branch contradicts without entering the late row-3 trap.

The remaining values continue to the next row-5 source step:

```text
b=5*a
```

Their domains differ:

```text
a=3 -> b=5*3 in {0,6,7,8}
a=8 -> b=5*8 in {1,3,6,7}
```

So the late row-3 trap is not the universal next step for every `a`.  It is the
deepest tail of the `a=3, b=8` route.  The transfer lemma should be written as
a cascade:

```text
w-domain
  -> w=7 quick exit
  -> residual w-values
     -> a-domain
        -> a=1 quick exit
        -> a=3 or a=8 source-orbit split by b=5*a
           -> quick exits or late row-3 trap
```

## First `b`-Layer Map For `k=4,r=1,w=2`

For:

```text
k=4
r=1
w=2
```

the current `a/b` cascade is:

```text
a=1 -> quick exit

a=3:
  b=5*3 in {0,6,7,8}
  b=0 -> quick contradiction
  b=6 -> quick contradiction
  b=7 -> continues to c=b*5
  b=8 -> continues to c=b*5 and contains the late row-3 trap

a=8:
  b=5*8 in {1,3,6,7}
  b=1 -> contradiction after a longer completion trace
  b=6 -> quick contradiction
  b=3 -> continues to c=b*5
  b=7 -> continues to c=b*5
```

Closure-trace markers:

```text
a=3,b=0 -> forces 3*5=2 and 4*0=5 before contradiction.
a=3,b=6 -> forces 3*5=0 before contradiction.
a=8,b=1 -> forces a row-5 completion including 5*4=0, 5*5=3, 5*7=6,
            plus 8*5=3 and 7*7=0 before contradiction.
a=8,b=6 -> forces 8*5=0 before contradiction.
```

Thus the next unresolved layer is:

```text
c=b*5
```

for the four live shells:

```text
(a,b)=(3,7), (3,8), (8,3), (8,7).
```

The known late row-3 trap is only one of these four shells:

```text
(a,b)=(3,8)
```

After the row-8 work below, the representative:

```text
k=4
r=1
w=2
```

is structurally closed:

```text
a=1 -> quick exit
a=3 -> b=0,6 quick exits; b=7/8 close by c-layer and row-3 trap
a=8 -> closes by the a-row zero trap, row-8 instance
```

## General `a`-Row Zero Trap

The `c`-layer has a general form.

Detailed sublemma file:

```text
a_row_zero_trap_lemma.md
```

Assume:

```text
5*0=a
5*a=b
c=b*5
```

The source-orbit ladder on the row-5 segment:

```text
5 -> 0 -> a -> b
```

gives:

```text
a*(b*5)=0
```

so:

```text
a*c=0
```

This is the reusable late trap.  It should not be treated as a special row-3
accident.

From:

```text
a*c=0
```

the inverse-edge chain gives, with:

```text
d=a*0
```

the relation:

```text
d*a=pred0(c)
```

Also E677 with:

```text
x=c
y=a
```

gives:

```text
c = a*(c*((a*c)*a))
  = a*(c*(0*a))
```

Since row `0` is the fixed cycle:

```text
0*a=succ0(a)
```

the trap has the reusable form:

```text
a*c=0
d=a*0
d*a=pred0(c)
c=a*(c*succ0(a))
```

Special cases:

```text
a=3:
  3*c=0
  d=3*0
  d*3=pred0(c)
  c=3*(c*4)

a=8:
  8*c=0
  d=8*0
  d*8=pred0(c)
  c=8*(c*0)
```

So the next task is to prove the `a=8` zero trap or show that its live shells
fall back to already closed quick exits.  The old row-3 trap is the `a=3`
instance.

## First `a=8` Zero-Trap Findings

The live `a=8` shells begin with:

```text
(a,b)=(8,3)
(a,b)=(8,7)
```

### Shell `(a,b)=(8,3)`

Here:

```text
c=3*5
8*c=0
```

The `c`-layer reduces to:

```text
c in {2,3,4,8}
```

and:

```text
c=2 -> quick contradiction
c=3 -> quick contradiction
c=4 -> quick contradiction
c=8 -> row-8 self-zero shell
```

The last shell is:

```text
3*5=8
8*8=0
```

For it, the next marker:

```text
d=8*0
```

has:

```text
d in {2,3}
```

and both values close:

```text
d=2 -> contradiction
d=3 -> contradiction
```

So the shell:

```text
(a,b)=(8,3)
```

is fully closed by the row-8 zero trap.

### Shell `(a,b)=(8,7)`

Here:

```text
c=7*5
8*c=0
```

The first `c` reduction gives:

```text
c in {2,3,8}
```

Closure status so far:

```text
c=2 -> still live after closure
c=3 -> still live after closure
c=8 -> still live after closure
```

Refinement for:

```text
c=2
```

Use:

```text
d=8*0
d*8=pred0(2)=1
```

The `d`-domain is:

```text
d in {1,2,3,8}
```

and all values close:

```text
d=1 -> contradiction
d=2 -> contradiction
d=3 -> contradiction, includes the familiar 1*1=0 obstruction
d=8 -> contradiction
```

So:

```text
(a,b,c)=(8,7,2)
```

is closed by the row-8 zero trap.

The remaining live row-8 zero-trap shells are:

```text
(a,b,c)=(8,7,3)
(a,b,c)=(8,7,8)
```

For:

```text
(a,b,c)=(8,7,3)
```

the next marker:

```text
d=8*0
d*8=pred0(3)=2
```

has:

```text
d in {1,2,3,6,8}
```

The new value:

```text
d=6
```

also closes by contradiction.

### Row-8 Self-Zero Killer

The self-zero subcase:

```text
8*8=0
```

has a stable closed role.  It appears in both:

```text
(a,b,c)=(8,3,8)
(a,b,c)=(8,7,8)
```

In both shells:

```text
d=8*0
d*8=7
d in {2,3}
```

and:

```text
d=2 -> contradiction
d=3 -> contradiction
```

So row-8 self-zero is a closed subrole of the `a`-row zero trap.

The remaining row-8 work is non-self:

```text
(a,b,c)=(8,7,3)
```

with:

```text
d=8*0 in {1,2,3,6,8}
d=6 -> contradiction
```

Additional representatives:

```text
d=1 -> contradiction, same quick role as the earlier a=1 exit:
       forces 1*7=0 and 7*1=6.
d=2 -> contradiction, includes the familiar 1*1=0 obstruction.
```

Remaining unchecked representatives in this non-self shell:

```text
d=3
d=8
```

Update:

```text
d=3 -> contradiction
d=8 -> contradiction
```

Therefore:

```text
(a,b,c)=(8,7,3)
```

is closed.

Together with the row-8 self-zero killer:

```text
(a,b,c)=(8,7,8)
```

is also closed.  Thus the whole `a=8` branch in the representative cascade:

```text
k=4
r=1
w=2
a=8
```

is closed by the `a`-row zero trap.

At this point the pattern is clear enough to stop treating the row-8 trap as
independent branch accounting.  The reusable sublemma should be:

```text
a*c=0
d=a*0
d*a=pred0(c)
c=a*(c*succ0(a))
```

plus a small finite role split for the row `a=8` cases.  This is still an
`a=8` trap branch, not a return to broad row-6 search.

Compare the closed `k=2` and `k=3` zero-hit layers against the `k=4,r=1`
hard representative only after this `a`-layer is understood:

```text
Does each return close at w=5*6?
If not, does it close at a=5*0 with 4*a=3?
If not, does it enter b=5*a and the late row-3 trap?
```

The output should be a transfer table, not another list of branch closures.

## `a=2` Row-5 Completion Trap

New sublemma file:

```text
a2_row5_completion_trap_lemma.md
```

The transfer check for the remaining residual `w` values exposed the missing
role:

```text
w=5*6=3
a=5*0=2
```

For this branch, the late values:

```text
b=5*2 in {7,8}
```

do not create a new deep `a`-row zero trap.  They fold back into row `5`.
Closure forces:

```text
5*3=5
```

Together with:

```text
5*6=3
```

the source-orbit ladder gives, for:

```text
p=5*5
```

the marker:

```text
3*p=6
```

The row-5 completion tail compresses to five one-node contradictions:

```text
5*2=7, p=0
5*2=7, p=1
5*2=7, p=8
5*2=8, p=0
5*2=8, p=1
```

So the current cascade has three closed late roles:

```text
a=3 -> row-3 zero trap
a=8 -> row-8 zero trap
a=2 -> row-5 completion trap via p=5*5
```

This is the first genuine transfer beyond the hard `w=2` representative: the
`w=3` branch introduces `a=2`, and `a=2` is now factored into a small marker
lemma rather than a row-completion enumeration.

Next transfer obligation:

```text
Build the k=4 L3 transfer table by w:
  w=7 quick exit;
  residual w values route through a in {1,2,3,8};
  a=1 quick exit;
  a=2 row-5 completion trap;
  a=3 row-3 zero trap;
  a=8 row-8 zero trap.
```

## `a`-Domain Restriction For `k=4`

New sublemma file:

```text
k4_l3_a_domain_restriction_lemma.md
```

This sublemma is now symbolic, not just diagnostic.  In the `k=4` L3 layer,
after:

```text
w=5*6
a=5*0
```

the row-5 bridge and row-4 descent force:

```text
a in {1,2,3,8} \ {w}
```

for every nonzero residual `w`.

The proof excludes:

```text
a=0  by E677 with x=0,y=5, which would force a row-5 collision;
a=4  by row-5 collision with 5*r=4;
a=5  by row-5 collision with 5*w=5;
a=6  by E677 with x=0,y=5, which would force w=0;
a=7  by contradiction between 4*a=3 and 4*7=6;
a=w  by row-5 collision between columns 0 and 6.
```

Diagnostics across representatives agree:

```text
r=1:
  w=2 -> a in {1,3,8}
  w=3 -> a in {1,2,8}
  w=8 -> a in {1,2,3}

r=2:
  w=1 -> a in {2,3,8}
  w=3 -> a in {1,2,8}
  w=8 -> a in {1,2,3}

additional representatives:
  r=3,w=1 -> a in {2,3,8}
  r=7,w=1 -> a in {2,3}
  r=8,w=1 -> a in {2,3,8}
```

So the k=4 transfer table is now structurally reduced to the four known
`a`-roles:

```text
a=1 quick exit
a=2 row-5 completion trap
a=3 row-3 zero trap
a=8 row-8 zero trap
```

Next remaining obligation:

```text
prove or certify that each of these four a-roles attaches uniformly for all
allowed residual w and r values.
```
