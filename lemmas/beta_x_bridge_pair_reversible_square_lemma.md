# Beta-X Bridge-Pair Reversible Square Lemma

Date: 2026-06-18.

Status:

```text
proved / beta-X bridge is a reversible two-target square
```

## Purpose

This is the beta-layer analogue of:

```text
x_layer_bridge_pair_reversible_square_lemma.md
```

It shows that the branch:

```text
Beta_i=x_j
```

does not create an unbounded new target-swap tower.  After the immediate hit
cases, it becomes a closed reversible two-target square.

## Setup

Use:

```text
x_{i+1}=x_i*b,
A_i=pred_{x_i}(b),
Beta_i=pred_{x_i}(A_i).
```

Assume:

```text
Beta_i=x_j.
```

Then:

```text
x_i*x_j=A_i,
x_i*A_i=b.
```

For row `x_j`:

```text
x_j*A_j=b,
x_j*b=x_{j+1}.
```

Define:

```text
delta=x_j*(A_i*x_i),
Beta_j=pred_{x_j}(A_j)=A_j*(b*x_j)=A_j*x_{j+1}.
```

Then:

```text
x_i*delta=x_j,
x_j*Beta_j=A_j.
```

## Two Target-Swapped Intervals

The original beta-X interval carried by row `x_i` is:

```text
P=(A_i, x_j, b).
```

The target-swapped interval is:

```text
P'=(x_j, delta, A_i).
```

For row `x_j`, the generated interval is:

```text
Q=(b, A_j, x_{j+1}).
```

and its target-swap at input `A_j` is:

```text
Q'=(A_j, Beta_j, b).
```

## Reversibility

Target advance of `P'` along row `x_i` gives:

```text
(x_j, delta, A_i)
  -> (A_i, x_j, x_i*A_i)
  =  (A_i, x_j, b)
  =  P.
```

Target advance of `Q'` along row `x_j` gives:

```text
(A_j, Beta_j, b)
  -> (b, A_j, x_j*b)
  =  (b, A_j, x_{j+1})
  =  Q.
```

Thus:

```text
P  <-> P',
Q  <-> Q'.
```

## Consequence

The beta-X hit:

```text
Beta_i=x_j
```

is reduced to:

```text
1. immediate hits of delta or Beta_j;
2. row x_i same-row swap x_j <-> A_i;
3. beta-coupled hit through Beta_j;
4. or a fresh reversible two-target square with source rows x_i and x_j.
```

So the beta-X branch is not a separate infinite extension mechanism.  Its
fresh part is another exact reversible-square residual.
