# Target-Advance Same-Row Period Lemma

Date: 2026-06-20.

Status:

```text
proved / classifies pure same-row target-advance recurrence
```

## Statement

Fix a source row `p` and write its row orbit as:

```text
x_{i+1}=p*x_i.
```

The target-advance ported interval at position `i` is:

```text
I_i=(x_i,x_{i-1},x_{i+1}).
```

Then:

```text
I_{i+k}=I_i
```

if and only if:

```text
x_{i+k}=x_i.
```

So the period of the same-row target-advance interval sequence is exactly the
period of the row orbit of `p` through `x_i`.

## Proof

If:

```text
I_{i+k}=I_i,
```

then equality of the first coordinate gives:

```text
x_{i+k}=x_i.
```

Conversely, if:

```text
x_{i+k}=x_i,
```

then applying the same row permutation forward gives:

```text
x_{i+k+1}=x_{i+1}.
```

Because row maps are bijections in a finite E677 magma, applying the inverse
row map gives:

```text
x_{i+k-1}=x_{i-1}.
```

Therefore:

```text
I_{i+k}=(x_{i+k},x_{i+k-1},x_{i+k+1})
       =(x_i,x_{i-1},x_{i+1})
       =I_i.
```

## Short Periods

### Period 1

If the row orbit has period `1`, then:

```text
p*x_i=x_i.
```

The interval is:

```text
(x_i,x_i,x_i).
```

This is a local fixed-point recurrence, not a fresh global relay loop.

### Period 2

If the row orbit has period `2`, then:

```text
p*x_i=x_{i+1},
p*x_{i+1}=x_i.
```

So row `p` swaps the two targets.  The target-advance sequence is exactly the
two-state swap loop from:

```text
swap_row_target_advance_loop_lemma.md
local_swap_fixed_recurrence_classification.md
```

Again this is already a local recurrence class, not a fresh G12 loop.

### Period At Least 3

Only period at least `3` gives a genuine moving same-row target-advance cycle:

```text
(x_i,x_{i-1},x_{i+1})
-> (x_{i+1},x_i,x_{i+2})
-> ...
```

with no immediate fixed/swap collapse.

## Consequence For G12

After:

```text
fixed_target_same_source_return_collapse_lemma.md
local_swap_fixed_recurrence_classification.md
```

the remaining same-source part of a minimal G12 loop can be assumed to use
row-orbit periods at least `3`.

Thus the active residual is not:

```text
same-source recurrence in general.
```

It is the narrower problem:

```text
coupled same-row target-advance cycles of period >= 3, with no independent
full ported-interval collision and no strict clean theta.
```
