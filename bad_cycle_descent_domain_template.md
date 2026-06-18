# Bad-Cycle Descent Domain Template

Date: 2026-06-04.

Status:

```text
symbolic template / extracted from k=4 L3 transfer
```

Purpose:

```text
Rewrite the local k=4 restriction a in {1,2,3,8}\{w} in bad-cycle notation.
```

This file is a bridge between the local L3 work and the main candidate:

```text
main_bad_cycle_no_free_tail_lemma.md
```

## Setup In Bad-Cycle Notation

Let:

```text
b_j = L_0^{-j}(0)
r_j = b_j*0
```

The current special branch instance has:

```text
b_1=8
b_2=7
b_3=6
b_4=5
b_5=4
b_6=3
b_7=2
b_8=1
```

The local `k=4` L3 setup translates to:

```text
b_3*b_3=b_5
b_3*b_5=0
b_3*0=r
r*b_3=b_6
b_4*r=b_5
```

The row-`k` marker for `k=b_5` gives:

```text
b_5*b_2=b_3
b_5*b_4=b_2
```

The row-`b_4` descent defines:

```text
w=b_4*b_3
b_4*w=b_4
a=b_4*0
b_5*a=b_6
```

## Template Statement

Under the setup above, for every nonzero residual `w`:

```text
a notin {0,b_2,b_3,b_4,b_5,w}.
```

Equivalently:

```text
a lies outside the already occupied block {0,b_2,b_3,b_4,b_5}
and is not w.
```

In the pure 9-cycle case this becomes:

```text
a in {b_1,b_6,b_7,b_8} \ {w}
```

which is exactly:

```text
a in {8,3,2,1} \ {w}
```

or, in the numeric order used in the local file:

```text
a in {1,2,3,8} \ {w}.
```

## Proof Of Exclusions

### `a != 0`

If:

```text
b_4*0=0
```

then E677 with:

```text
x=0
y=b_4
```

gives:

```text
0 = b_4*(0*((b_4*0)*b_4)).
```

Using:

```text
b_4*0=0
0*b_4=b_3
0*b_3=b_2
```

this becomes:

```text
0=b_4*b_2.
```

But row `b_4` already has:

```text
b_4*0=0.
```

So row `b_4` repeats output `0`, contradiction.

### `a != b_5`

If:

```text
b_4*0=b_5
```

then row `b_4` repeats output `b_5`, because:

```text
b_4*r=b_5
```

and:

```text
r != 0.
```

### `a != b_4`

If:

```text
b_4*0=b_4
```

then row `b_4` repeats output `b_4`, because:

```text
b_4*w=b_4
```

and:

```text
w != 0.
```

### `a != b_3`

If:

```text
b_4*0=b_3
```

then E677 with:

```text
x=0
y=b_4
```

gives:

```text
0 = b_4*(0*((b_4*0)*b_4)).
```

Now:

```text
(b_4*0)*b_4 = b_3*b_4.
```

In the current special branch:

```text
b_3*b_4=b_4
```

because `b_3*b_4=b_4` is exactly `6*5=5`.

Thus:

```text
0 = b_4*(0*b_4)=b_4*b_3=w,
```

contradicting residual:

```text
w != 0.
```

### `a != b_2`

If:

```text
a=b_2
```

then the descent marker gives:

```text
b_5*b_2=b_6.
```

But the row-`b_5` marker already gives:

```text
b_5*b_2=b_3.
```

Since:

```text
b_6 != b_3,
```

this is impossible.

### `a != w`

If:

```text
a=w
```

then:

```text
b_4*0=w
b_4*b_3=w,
```

so row `b_4` repeats output `w`, impossible.

## Interpretation

The local set:

```text
{1,2,3,8}
```

is not accidental.  It is the complement of the already occupied bad-cycle
block:

```text
{0,b_2,b_3,b_4,b_5}
```

inside the normalized pure 9-cycle, with `w` also removed.

This is exactly the kind of invariant needed for the main no-free-tail lemma:

```text
the descent does not create a new arbitrary value;
it pushes the next value outside an occupied block, into a small finite role
set.
```

## Current Boundary

The proof of `a != b_3` uses the special fixed edge:

```text
b_3*b_4=b_4
```

which came from:

```text
r_2=b_4.
```

So the general no-free-tail lemma must either:

```text
1. prove an analogous fixed/return edge for every bad-cycle tail type; or
2. split bad-cycle tails by the offset r_2=b_t and prove a corresponding
   occupied-block exclusion for each offset.
```

This is now the precise boundary between the local k=4 proof and the desired
global theorem.
