# Beta Zipper Shifted-Repeat Split Lemma

Date: 2026-06-18.

Status:

```text
proved reduction / first shifted-column repeat gives same-input split
```

## Purpose

This sharpens the first-hit boundary for a fresh beta zipper ladder.

If a shifted side column repeats before the main `Z` chain repeats, then the
repeat is not merely a vague collision.  It is a genuine same-input split.

## Setup

Use:

```text
Z_i^{-2}=x_{i+1},
Z_i^{-1}=b,
Z_i^0=A_i,
Z_i^1=Beta_i,
Z_i^{m+1}=pred_{x_i}(Z_i^m).
```

For every `m>=0`, the zipper side edge is:

```text
row Z_i^{m-1}: T_i^m -> Z_i^m,
```

where:

```text
T_i^m=Z_i^{m-2}*x_i.
```

## Statement

Assume:

```text
T_i^r=T_i^s
```

with:

```text
r>s>=0,
```

and assume no earlier repeat occurred in the main chain:

```text
Z_i^u are pairwise distinct up to r.
```

Then:

```text
Z_i^{r-1} != Z_i^{s-1},
Z_i^r     != Z_i^s.
```

Therefore the two side edges form a proper same-input split:

```text
row Z_i^{r-1}: T -> Z_i^r,
row Z_i^{s-1}: T -> Z_i^s,
```

with:

```text
T=T_i^r=T_i^s.
```

## Proof

If:

```text
Z_i^{r-1}=Z_i^{s-1},
```

then the main `Z` chain already repeated before level `r`, contrary to the
assumption.

If:

```text
Z_i^r=Z_i^s,
```

then the main chain repeats at levels `r` and `s`, again contrary to the
assumption.

So the source rows and outputs of the two side edges are both distinct.

## Target Lift

By:

```text
same_input_split_target_lift_lemma.md
```

the split at the common input `T` lifts into the common target graph `H_T`.

Define:

```text
P_T=T*(Z_i^r*Z_i^{r-1}),
Q_T=T*(Z_i^s*Z_i^{s-1}).
```

Then:

```text
Z_i^{r-1}*P_T=T,
Z_i^{s-1}*Q_T=T.
```

So in `H_T`:

```text
P_T -> Z_i^r     carried by row Z_i^{r-1},
Q_T -> Z_i^s     carried by row Z_i^{s-1}.
```

## Consequence

The fresh beta zipper has only two clean finite closure types:

```text
1. first main-chain repeat Z_i^r=Z_i^s:
   same-row recurrence in row x_i;

2. first shifted-column repeat T_i^r=T_i^s before any Z repeat:
   proper same-input split, which lifts to H_T.
```

Thus the shifted repeat is the stronger branch.  It creates a new cross-role
same-target pair and should be attacked before treating the pure `Z` repeat as
the final residual.
