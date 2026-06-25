# Clean External-Bridge Fifth-Stage Reduction Lemma

Date: 2026-06-18.

Status:

```text
proved reduction / folds V4 into common same-input bridge frontier
```

## Purpose

This updates:

```text
clean_external_bridge_fourth_stage_reduction_lemma.md
```

after:

```text
beta_anchor_row_b_partner_reduction_lemma.md
```

The main conclusion is:

```text
V4 is not an independent beta-anchored square residual.
```

It folds into the V3-type clean same-input two-target bridge frontier.

## Fourth-Stage Residuals

The fourth-stage list was:

```text
V1. same-row recurrence boundaries;
V2. shared-edge divergence Beta_i=H_i;
V3. clean same-input two-target bridge;
V4. beta-anchored reversible square.
```

## V4 Folding

Every beta anchor:

```text
Beta_j -> b in H_{A_j}
```

has the row-`b` same-target partner:

```text
H_j -> D_j in H_{A_j},
```

where:

```text
D_j=b*A_j.
```

After common-input/common-output/full-interval/cross-hit cases are routed,
target advance gives:

```text
H_b:     A_j -> x_{j+1}       carried by row x_j,
H_{D_j}: A_j -> b*D_j         carried by row b.
```

So a clean V4 is a same-input two-target bridge sharing the generated input
`A_j`.

## Fifth-Stage Residual List

The clean external bridge is now reduced to:

```text
W1. same-row recurrence boundaries;

W2. shared-edge divergence:
    rows b and x_i share H_i -> A_i;

W3. clean same-input two-target bridge at a generated input:
    p*A_j=S,
    q*A_j=R,
    S!=R,
    with its lifted same-target pair locally clean.
```

The removed residual is:

```text
beta-anchored reversible square as an independent case.
```

## Concrete Sources Of W3

The W3 bridge appears in two main ways:

```text
1. beta-A hit:
   row x_i: A_j -> A_i,
   row x_j: A_j -> b;

2. beta-anchor row-b partner:
   row x_j: A_j -> b,
   row b:   A_j -> D_j=b*A_j.
```

In both cases one branch is the generated row `x_j` edge:

```text
row x_j: A_j -> b -> x_{j+1}.
```

The unavoidable base bridge at every generated input is recorded in:

```text
row_b_generated_input_bridge_lemma.md
```

It is:

```text
row b:   A_j -> D_j=b*A_j,
row x_j: A_j -> b.
```

## Next Useful Target

Attack W3 directly.

The useful question is:

```text
Can a clean same-input two-target bridge at a generated input A_j remain
disjoint from the row-b predecessor layer H_j -> A_j and the generated H_b
edge A_j -> x_{j+1}?
```

If not, the clean external bridge returns to a fan/path/core-attachment case.
If yes, W3 is the exact remaining residual.

W3 is sharpened by:

```text
generated_input_three_source_bridge_expansion_lemma.md
row_b_generated_input_bridge_lemma.md
```

Any W3 bridge at `A_j` with an extra source row distinct from `b,x_j` expands
in `H_{A_j}` to:

```text
P      -> S,
Beta_j -> b,
H_j    -> D_j=b*A_j.
```

After local pair collisions are routed, the residual is a clean three-edge
matching in `H_{A_j}`, or after target advance, a clean three-target
same-input bridge at `A_j`.  If the extra source is row `b`, this is the
two-source V4-folded bridge instead.

The first W3 split should classify:

```text
D_j=b,
D_j hits a watched layer,
or D_j is fresh.
```
