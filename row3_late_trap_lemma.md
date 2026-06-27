# Row-3 Late Trap Lemma

Date: 2026-06-03.

Status:

```text
candidate trap / final residual symbolically closed
```

Scope:

```text
row5_descent_bridge hard representative
5*0=3
5*3=b
b in {7,8}
c=b*5
```

This file records the late part of the row-5 descent bridge.  It should be
read after:

```text
row5_descent_bridge_lemma.md
```

## General Transfer Into Row 3

From the row-5 orbit:

```text
5*0=3
5*3=b
```

the source-orbit ladder gives:

```text
3*(b*5)=0
```

With:

```text
c=b*5
```

this is:

```text
3*c=0
```

So the late row-5 tail transfers into row `3`.

## Row-3 Trap Consequences

From:

```text
3*c=0
```

and the inverse-edge chain:

```text
3*z=0 => z = 0*((3*0)*3)
```

letting:

```text
d=3*0
```

gives:

```text
d*3=pred0(c)
```

Also E677 with:

```text
x=c
y=3
```

gives:

```text
c = 3*(c*((3*c)*3))
```

Since:

```text
3*c=0
0*3=4
```

this becomes:

```text
c = 3*(c*4)
```

So the row-3 trap has the form:

```text
3*c=0
3*(c*4)=c
d=3*0
d*3=pred0(c)
```

Together with:

```text
4*3=3
```

the inverse-edge chain on `4*3=3` gives:

```text
3 = 3*(3*4)
```

So row `3` simultaneously contains:

```text
3*c=0
3*(c*4)=c
3*(3*4)=3
```

This is the trap: late `c` values close when they collide with this short
row-3 chain.

## Diagnostic Status

For the hard representative:

```text
k=4
r=1
w=5*6=2
a=5*0=3
b=5*a
```

the late diagnostic gave:

```text
b=7: all c=b*5 values close immediately.
b=8: all c=b*5 values close immediately except c=3.
```

The unique late residual is:

```text
b=8
c=3
3*3=0
```

Then:

```text
e=5*8 in {1,6}
```

and both close.

## Last Residual: `e=1`

If:

```text
e=5*8=1
```

then from:

```text
5*3=8
5*8=1
```

the source-orbit ladder gives:

```text
8*(1*5)=3
```

But:

```text
8*5=3
```

so injectivity of row `8` forces:

```text
1*5=5
```

The inverse-edge chain on:

```text
1*5=5
```

using:

```text
5*1=4
```

gives:

```text
5*4=5
```

But the inverse-edge chain on:

```text
6*5=5
```

using:

```text
5*6=2
```

already gives:

```text
5*2=5
```

This contradicts injectivity of row `5`:

```text
5*2=5
5*4=5
2 != 4
```

Thus the `e=1` late residual is symbolically closed.

## Last Residual: `e=6`

If:

```text
e=5*8=6
```

then row `5` has only three possible completions:

```text
A: 5*4=0, 5*5=1, 5*7=7
B: 5*4=1, 5*5=0, 5*7=7
C: 5*4=7, 5*5=1, 5*7=0
```

All three close immediately in diagnostics.  The next symbolic target is to
replace these three completions with short inverse-edge contradictions.

For case `A`, one visible route is:

```text
5*4=0
=> 3*5=3
=> 3*4=5
```

and `3*4=5` is already impossible under the `e=6` base conditions.

The remaining work is to derive the corresponding short contradictions for:

```text
B: 5*5=0
C: 5*7=0
```

without running another branch search.

## Reduction Of The Three `e=6` Completions

In the `e=6` residual, the three row-5 completions force the following
row-3 values:

```text
A: 5*4=0 -> 3*5=3
B: 5*5=0 -> 3*5=4
C: 5*7=0 -> 3*5=6
```

Reason:

```text
5*q=0
=> q = 0*((5*0)*5)
=> q = 0*(3*5)
```

Since row `0` is the fixed cycle, this determines `3*5`.

### Case `3*5=3`

This one is symbolically closed.

Use E677 with:

```text
x=5
y=3
```

Then:

```text
5 = 3*(5*((3*5)*3))
```

If:

```text
3*5=3
```

and:

```text
3*3=0
5*0=3
```

then:

```text
5 = 3*(5*(3*3))
  = 3*(5*0)
  = 3*3
  = 0
```

contradiction.

### Case `3*5=4`

The same E677 instance gives:

```text
5 = 3*(5*((3*5)*3))
```

Using:

```text
3*5=4
4*3=3
5*3=8
```

gives:

```text
3*8=5
```

Diagnostics show that `3*8=5` is already impossible in the `e=6` base
residual.  The remaining symbolic target for this case is:

```text
prove e=6 base => 3*8 != 5.
```

### Case `3*5=6`

The same E677 instance gives:

```text
5 = 3*(5*(6*3))
```

Diagnostics show that `3*5=6` is impossible in the `e=6` base residual, but
the short symbolic contradiction is not yet extracted.

The remaining symbolic target is:

```text
prove e=6 base => 3*5 != 6.
```

## Update 2026-06-03: `e=6` Residual Closed Diagnostically

Using the corrected full 9-cycle row-0 representative:

```text
0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 0
```

the fixed `e=6` base was checked with:

```text
7*0=5
6*5=5
6*6=4
6*4=0
6*0=1
1*6=3
5*1=4
5*6=2
5*0=3
4*3=3
5*3=8
8*5=3
3*3=0
5*8=6
```

A row-limited diagnostic on rows `3` and `5` gives:

```text
3*5 in {4,6}
```

The two possible values both close immediately:

```text
base + 3*5=4 -> status none, 2.47s, 1 node
base + 3*5=6 -> status none, 2.40s, 1 node
```

So the whole `e=6` final residual is now diagnostically closed.  The remaining
mathematical work is narrower than before: extract the short symbolic reason
why the row-3 late trap forbids the two values:

```text
3*5=4
3*5=6
```

This replaces the previous wording that treated `3*8=5` as the main B-target.
The stronger current fact is:

```text
e=6 base => 3*5 notin {4,6}
```

and since diagnostics also give `3*5 in {4,6}`, the residual is closed.

## Closure Traces For The Two Last Values

The base `e=6` closure is still consistent before choosing `3*5` and forces:

```text
4*5=7
4*7=6
8*1=7
```

in addition to the base cells.

Adding:

```text
3*5=4
```

closes with contradiction after forcing:

```text
5*5=0
3*8=5
8*0=5
8*7=0
```

The symbolic chain currently visible is:

```text
3*5=4
=> 5*5=0              by 5*q=0 => q=0*(3*5)
=> 3*8=5              by E677 with x=5,y=3
=> 8*0=5              by E677 with x=5,y=8
```

Adding:

```text
3*5=6
```

closes with contradiction after forcing:

```text
5*7=0
1*1=0
2*0=1
7*1=0
```

The symbolic chain currently visible is:

```text
3*5=6
=> 5*7=0              by 5*q=0 => q=0*(3*5)
=> 7*1=0              by inverse-edge / row-0 return from 5*7=0
```

The remaining proof extraction target is therefore more precise:

```text
B-trap: show base + 5*5=0 + 3*8=5 + 8*0=5 is impossible.
C-trap: show base + 5*7=0 + 1*1=0 + 7*1=0 is impossible.
```

These are small row-3/row-5/row-8 and row-1/row-7 traps, not a reason to
branch below `e=6`.

## Symbolic Closure Of The Two Traps

### B-Trap

Assume:

```text
3*5=4
```

Then the closure chain gives:

```text
5*5=0
3*8=5
8*0=5
8*7=0
```

The final contradiction is a direct E677 instance with:

```text
x=7
y=8
```

Indeed:

```text
7 = 8*(7*((8*7)*8))
  = 8*(7*(0*8))
  = 8*(7*0)
  = 8*5
  = 3
```

contradiction.

So:

```text
base + 3*5=4
```

is symbolically impossible.

### C-Trap

Assume:

```text
3*5=6
```

Use E677 with:

```text
x=0
y=5
```

Since:

```text
5*0=3
3*5=6
0*6=7
```

we get:

```text
0 = 5*(0*((5*0)*5))
  = 5*(0*(3*5))
  = 5*(0*6)
  = 5*7
```

so:

```text
5*7=0
```

Now use E677 with:

```text
x=0
y=7
```

Since:

```text
7*0=5
5*7=0
0*0=1
```

we get:

```text
0 = 7*(0*((7*0)*7))
  = 7*(0*(5*7))
  = 7*(0*0)
  = 7*1
```

so:

```text
7*1=0
```

Now use E677 with:

```text
x=0
y=1
```

Since:

```text
1*0=7
7*1=0
0*0=1
```

we get:

```text
0 = 1*(0*((1*0)*1))
  = 1*(0*(7*1))
  = 1*(0*0)
  = 1*1
```

so:

```text
1*1=0
```

But the standard bad-element diagonal obstruction says there is no `y` with:

```text
0*(y*y)=y
```

Here, for `y=1`:

```text
0*(1*1)=0*0=1
```

contradiction.

So:

```text
base + 3*5=6
```

is symbolically impossible.

## Conclusion

The final `e=6` residual is no longer only diagnostically closed.  It is closed
by two short symbolic traps:

```text
3*5=4 -> B-trap -> E677(x=7,y=8) gives 7=3.
3*5=6 -> C-trap -> forbidden 0*(1*1)=1.
```

Together with the earlier symbolic closure of `e=1`, the unique late residual:

```text
5*3=8
8*5=3
3*3=0
5*8 in {1,6}
```

is symbolically closed.
