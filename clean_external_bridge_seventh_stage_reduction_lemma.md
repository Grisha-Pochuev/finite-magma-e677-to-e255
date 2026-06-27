# Clean External-Bridge Seventh-Stage Reduction Lemma

Date: 2026-06-19.

Status:

```text
proved reduction / X3 becomes three-row cycle comparison at A_j
```

## Purpose

This updates:

```text
clean_external_bridge_sixth_stage_reduction_lemma.md
```

after the X3 target-advance and source-successor work:

```text
x3_three_edge_matching_advance_boundary.md
x3_advanced_edge_triangle_pressure_lemma.md
x3_self_renewal_boundary.md
source_successor_eventual_predecessor_hit_lemma.md
```

## X3 Normal Form

The extra-source X3 residual has three source rows through the same generated
input `A_j`:

```text
p,
x_j,
b.
```

Their predecessor/current/successor triples around `A_j` are:

```text
row p:   P      -> A_j -> S,
row x_j: Beta_j -> A_j -> b,
row b:   H_j    -> A_j -> D_j.
```

where:

```text
p notin {b,x_j},
D_j=b*A_j.
```

The clean assumptions are:

```text
P, Beta_j, H_j are pairwise distinct;
S, b, D_j are pairwise distinct;
no input-output cross hit among these six endpoints;
no watched-layer hit.
```

## Finite Cycle Return

By:

```text
source_successor_eventual_predecessor_hit_lemma.md
```

each source row's forward orbit from `A_j` eventually hits its predecessor:

```text
row p   eventually hits P,
row x_j eventually hits Beta_j,
row b   eventually hits H_j.
```

For rows `x_j` and `b`, the first steps are already tracked:

```text
row x_j: A_j -> b -> x_{j+1},
row b:   A_j -> D_j -> ...
```

and the row-`b` return to `H_j` routes through:

```text
row_b_successor_eventual_h_hit_lemma.md
row_b_successor_h_hit_role_lemma.md
```

## Seventh-Stage Residual List

The clean external bridge is now reduced to:

```text
Y1. same-row recurrence boundaries;

Y2. shared-edge divergence:
    rows b and x_i share H_i -> A_i;

Y3. clean three-row cycle comparison at a generated input A_j:
    rows p, x_j, b all pass through A_j,
    with predecessor triple P, Beta_j, H_j
    and successor triple S, b, D_j,
    all locally clean.
```

The removed residual is:

```text
X3 as an open-ended three-edge matching.
```

## Next Useful Target

Attack Y3 as a finite three-cycle comparison.

The useful split is the first return among the three source-row cycles:

```text
row p returns to P,
row x_j returns to Beta_j,
row b returns to H_j.
```

If any return hits another row's predecessor/successor layer first, route by
the hit.  If all three cycles remain clean until their own predecessor return,
the remaining object is a synchronized clean three-cycle boundary at `A_j`.
