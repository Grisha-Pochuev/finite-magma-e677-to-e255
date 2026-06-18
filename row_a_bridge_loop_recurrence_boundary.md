# Row-a Bridge Loop Recurrence Boundary

Date: 2026-06-18.

Status:

```text
general proved / same-row recurrence boundary
```

## Setup

In the bad-target crossed-fan row-a bridge edge, let:

```text
k=pred_a(b),
a*k=b,
t=a*b.
```

Assume:

```text
t=k.
```

That is:

```text
a*b=k.
```

## Statement

Row `a` swaps `b` and `k`:

```text
a*k=b,
a*b=k.
```

Therefore, in `H_b`, row `a` gives a loop:

```text
k -> k.
```

Under target advance this is a two-state same-row recurrence:

```text
(b,k,k) -> (k,b,b) -> (b,k,k).
```

So the case `a*b=k` belongs to the same-row recurrence boundary, not to the
clean external bridge case.

## Proof

For target `b`, row `a` has:

```text
a*k=b,
a*b=k.
```

Thus the full ported interval is:

```text
(b,k,k).
```

The target-advance rule sends:

```text
(target,input,output)=(b,k,k)
```

to:

```text
(k,b,a*k)=(k,b,b).
```

Applying target advance again gives:

```text
(b,k,a*b)=(b,k,k).
```

This is exactly the same sliding-window recurrence already isolated in:

```text
target_advance_row_orbit_lemma.md
```

## Use

When reducing the proper bad-target crossed-fan frontier, the clean external
row-a bridge case may assume:

```text
a*b != k.
```

The excluded equality is not a contradiction by itself; it is routed to the
same-row recurrence boundary.

