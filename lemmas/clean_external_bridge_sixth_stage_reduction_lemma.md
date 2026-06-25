# Clean External-Bridge Sixth-Stage Reduction Lemma

Date: 2026-06-18.

Status:

```text
proved reduction / removes base row-b/generated bridge as independent residual
```

## Purpose

This updates:

```text
clean_external_bridge_fifth_stage_reduction_lemma.md
```

after routing the unavoidable row-b/generated bridge at each generated input:

```text
row_b_generated_input_bridge_lemma.md
row_b_successor_eventual_h_hit_lemma.md
row_b_successor_h_hit_role_lemma.md
```

## Fifth-Stage Residuals

The fifth-stage list was:

```text
W1. same-row recurrence boundaries;
W2. shared-edge divergence Beta_i=H_i;
W3. clean same-input two-target bridge at a generated input A_j.
```

## Base W3 Bridge

At every generated input `A_j`, rows `b` and `x_j` give:

```text
row b:   A_j -> D_j=b*A_j,
row x_j: A_j -> b.
```

The base W3 split is:

```text
1. D_j=b:
   common-edge fan over A_j -> b;

2. D_j hits a watched layer:
   route by that hit;

3. D_j fresh:
   row-b successor chain from A_j eventually hits H_k and then A_k.
```

The fresh case follows from:

```text
row_b_successor_eventual_h_hit_lemma.md
row_b_successor_h_hit_role_lemma.md
```

Thus the base row-b/generated bridge folds back into:

```text
row-b A-layer cycle/cross-hit analysis,
or same-row row-b recurrence.
```

## Extra-Source W3 Bridge

If W3 has an additional source:

```text
p*A_j=S,
p notin {b,x_j},
```

then:

```text
generated_input_three_source_bridge_expansion_lemma.md
```

expands it in `H_{A_j}` to:

```text
P      -> S,
Beta_j -> b,
H_j    -> D_j.
```

After pairwise local collisions are routed, the remaining clean case is a
three-edge matching in `H_{A_j}`.

## Sixth-Stage Residual List

The clean external bridge is now reduced to:

```text
X1. same-row recurrence boundaries;

X2. shared-edge divergence:
    rows b and x_i share H_i -> A_i;

X3. extra-source clean three-edge matching at a generated input A_j:
    P      -> S,
    Beta_j -> b,
    H_j    -> D_j
    in H_{A_j},
    with p notin {b,x_j}.
```

The removed residual is:

```text
base row-b/generated same-input bridge.
```

## Next Useful Target

Attack X3.

The next question is whether a clean three-edge matching in `H_{A_j}` can
remain disjoint after target advance, or whether the three advanced edges:

```text
H_S:     A_j -> p*S,
H_b:     A_j -> x_{j+1},
H_{D_j}: A_j -> b*D_j
```

force a watched hit, a fan, or a full ported interval collision.
