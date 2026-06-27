# Fresh Reversible Square Beta-Anchor Lemma

Date: 2026-06-18.

Status:

```text
proved reduction / fresh reversible squares are beta-anchored
```

## Purpose

This compares the second-stage residuals:

```text
R4. fresh reversible two-target square;
R5. fresh beta-layer extension.
```

The point is that R4 is not independent from R5.  Every fresh reversible square
already contains a beta foot:

```text
Beta_j=pred_{x_j}(A_j).
```

So a truly fresh reversible square is automatically anchored in the beta layer.

## G-Square Case

In the G branch:

```text
H_i=x_j.
```

The reversible square is:

```text
(A_i, x_j, b*A_i) <-> (x_j, alpha, A_i),
(b, A_j, x_{j+1}) <-> (A_j, Beta_j, b),
```

where:

```text
Beta_j=A_j*(b*x_j).
```

Thus the second half of the square uses the beta foot `Beta_j`.

If `Beta_j` hits the visible footprint, generated A/X/H layers, or satisfies
one of the beta first-hit equalities, the square is routed by:

```text
beta_layer_reduction_lemma.md
```

If none of those hits occurs, then the square contains a fresh beta foot and
therefore belongs to the fresh beta-layer extension residual.

## Beta-X Square Case

In the beta-X branch:

```text
Beta_i=x_j.
```

The reversible square is:

```text
(A_i, x_j, b)      <-> (x_j, delta, A_i),
(b, A_j, x_{j+1}) <-> (A_j, Beta_j, b),
```

again with:

```text
Beta_j=pred_{x_j}(A_j)=A_j*(b*x_j).
```

So the same conclusion holds: a fresh beta-X square is beta-anchored at index
`j`.

## Consequence

After beta first-hit routing, the residual:

```text
fresh reversible two-target square
```

can be treated as:

```text
fresh reversible square anchored at a fresh Beta_j.
```

Thus R4 should not be pursued as a separate infinite mechanism.  It is a
structured subcase of the fresh beta-layer extension problem.

The current clean external-bridge frontier can therefore be compressed to:

```text
1. same-row recurrence boundaries;
2. row-b independent predecessor cycle with beta pressure;
3. beta-coupled fresh same-target pair;
4. fresh beta-layer extension, possibly carrying a reversible square.
```

The next useful lemma should attack the fresh beta-layer extension directly.
