# Beta Fresh Extension First-Hit Boundary

Date: 2026-06-18.

Status:

```text
boundary / exact first-hit split for a fresh beta extension
```

## Purpose

This records what remains after:

```text
Beta_i
```

is fresh in the beta-layer first-hit split.

The extension is governed by:

```text
beta_fresh_predecessor_zipper_ladder_lemma.md
```

and therefore has more structure than a plain new predecessor.

## Setup

Use the zipper notation:

```text
Z_i^{-2}=x_{i+1},
Z_i^{-1}=b,
Z_i^0=A_i,
Z_i^1=Beta_i,
Z_i^{m+1}=pred_{x_i}(Z_i^m).
```

For every `m>=0`:

```text
row x_i:       Z_i^{m+1} -> Z_i^m -> Z_i^{m-1},
row Z_i^{m-1}: (Z_i^{m-2}*x_i) -> Z_i^m.
```

Let the watched set be:

```text
W = visible footprint
    union generated A-layer
    union generated X-layer
    union generated H-layer
    union known beta feet.
```

## First-Hit Split

Follow the pairs:

```text
Z_i^m,
T_i^m=Z_i^{m-2}*x_i.
```

The first nonfresh event is one of:

### 1. `Z_i^m` hits the watched set

This routes by the layer hit:

```text
visible hit -> core attachment;
A/X/H hit   -> generated layer routing;
beta hit    -> beta-coupled same-target pair or reversible square routing.
```

### 2. `T_i^m` hits the watched set

Then the shifted side edge:

```text
row Z_i^{m-1}: T_i^m -> Z_i^m
```

attaches the fresh beta extension to a watched input.  This is not a silent
fresh extension; it is a concrete side attachment from row `Z_i^{m-1}`.

### 3. A new chain repeat `Z_i^r=Z_i^s`

If:

```text
r>s>=1
```

and no earlier watched hit occurred, then row `x_i` has a same-row predecessor
cycle:

```text
Z_i^r -> Z_i^{r-1} -> ... -> Z_i^s -> Z_i^{s-1}.
```

This is a same-row recurrence boundary, not an immediate contradiction.

### 4. A shifted-column repeat `T_i^r=T_i^s`

If shifted columns repeat before any watched hit and before any main `Z`
repeat, then by:

```text
beta_zipper_shifted_repeat_split_lemma.md
```

two side rows:

```text
Z_i^{r-1}, Z_i^{s-1}
```

use the same shifted input with distinct outputs:

```text
Z_i^r, Z_i^s.
```

This is a same-input split:

```text
row Z_i^{r-1}: T -> Z_i^r,
row Z_i^{s-1}: T -> Z_i^s.
```

It should be lifted by:

```text
same_input_split_target_lift_lemma.md
```

This is the first place where the fresh beta extension can become a genuine
cross-role fan/split rather than a mere same-row recurrence.

## Exact Remaining Residual

After all watched hits are routed, the only clean fresh beta extension is:

```text
a finite row-x_i predecessor cycle whose zipper side columns also avoid the
watched set until their first repeat.
```

This is now the precise residual.  It is narrower than the old phrase:

```text
fresh beta-layer extension.
```

The shifted-repeat branch is routed in:

```text
beta_zipper_shifted_repeat_split_lemma.md
```

If no shifted repeat occurs before the main `Z` repeat, the remaining case is
not an independent clean cycle.  It is corrected by:

```text
fresh_beta_extension_eventual_x_hit_lemma.md
```

The first watched return must be a generated X-hit, at worst:

```text
Z_i^m=x_{i+1}.
```
