# Row-a Second-Bridge Visible-Hit Cases

Date: 2026-06-18.

Status:

```text
general routing classification / not a closure
```

## Setup

In the clean external-bridge residual, let:

```text
t=a*b,
ell=t*a=pred_b(k),
b*ell=k.
```

Thus row `b` has the predecessor fan:

```text
b*h=a,
b*ell=k.
```

with:

```text
h!=ell,
a!=k.
```

## Purpose

This file classifies what it means if the second bridge input `ell` hits the
already visible two-target footprint.  These cases are routing information;
they are not automatically contradictions.

## Cases

### 1. `ell=h`

This is impossible inside the clean residual:

```text
ell=h -> k=a
```

by row `b` injectivity.

### 2. `ell=a`

Then:

```text
t*a=a.
```

Since `t=a*b`, the element `t` right-fixes `a`.  This is a right-fixer/good-`a`
boundary.  It does not contradict the badness of `b` by itself, because `a`
is not assumed bad.

### 3. `ell in {c,d}`

Then the row-`b` predecessor fan starts at an outgoing tip of the visible
`H_b` fan:

```text
b*c=k
```

or:

```text
b*d=k.
```

This is a row-`b` attachment to the visible outgoing footprint.

### 4. `ell in {u,v}`

Then the row-`b` predecessor fan starts at a target-swapped tip.  This is a
dual-footprint attachment in the two-target relay, not a local `H_b`
attachment.

### 5. `ell=k`

Then:

```text
b*k=k.
```

This is a row-`b` fixed point at the bridge vertex `k`.  It is not a right
fixer of the bad target `b`, so it is not an immediate contradiction.

### 6. `ell=t`

Then:

```text
b*t=k.
```

The predecessor fan starts at the output of the row-a bridge edge and returns
to the bridge source `k`.

### 7. `ell=b`

Then:

```text
b*b=k.
```

This identifies the bridge source `k` with the row-`b` output at the bad
target.  Since `b` is bad, this only confirms `k!=b`; it is not a closure by
itself.

## Clean Next Residual

If none of the visible hits occur, the second bridge is also external:

```text
ell not in {a,b,c,d,u,v,h,k,t}.
```

The next proof step should then treat:

```text
b*h=a,
b*ell=k
```

as a fresh row-`b` predecessor fan coupled to the self-labeled edge recursion.

## Diagnostic Note

Short saturation checks with:

```text
ta=h,
ta=k,
ta=a,
ta=c
```

show:

```text
ta=h -> k=a
```

and no other immediate local collapse or short right-fixer for the bad target
`b`.  So the visible-hit cases should be routed, not treated as proved
impossible.
