# R-b5 A-Layer Cycle Base-Bridge Relay Lemma

Date: 2026-06-19.

Status:

```text
proved reduction / R-b5 A-layer cycle is a chain of base bridge A-hits
```

## Purpose

This attacks:

```text
R-b5. row-b A-layer/predecessor cycle
```

from:

```text
same_row_recurrence_inventory.md
```

The point is that an A-layer row-`b` cycle is not an anonymous row cycle.  Each
edge:

```text
b*A_j=A_i
```

is exactly the base row-b/generated bridge at the generated input `A_j`, with
the row-`b` output hitting the generated `A`-layer.

## Setup

Use the generated data:

```text
x_j*A_j=b,
x_j*b=x_{j+1},
H_j=pred_b(A_j),
b*H_j=A_j.
```

At every generated input `A_j`, row `b` and row `x_j` give:

```text
row b:   A_j -> D_j=b*A_j,
row x_j: A_j -> b.
```

This is the unavoidable base bridge from:

```text
row_b_generated_input_bridge_lemma.md
```

## A-Layer Hit

If an R-b5 edge has:

```text
b*A_j=A_i,
```

then:

```text
D_j=A_i.
```

So the base bridge at `A_j` is:

```text
row b:   A_j -> A_i,
row x_j: A_j -> b.
```

This is a same-input two-target bridge whose row-`b` output is a watched
generated A-layer hit.

If:

```text
i=j,
```

then:

```text
b*A_j=A_j,
```

which is the row-`b` fixed point boundary R-b3.

So the clean R-b5 cycle may assume:

```text
i!=j.
```

## Lift To H_{A_j}

The same-input lift at `A_j` gives two edges in `H_{A_j}`:

```text
H_j    -> A_i      carried by row b,
Beta_j -> b        carried by row x_j.
```

where:

```text
x_j*Beta_j=A_j.
```

This is the beta-anchor/row-b partner shape already used in:

```text
beta_anchor_row_b_partner_reduction_lemma.md
clean_external_bridge_fifth_stage_reduction_lemma.md
```

Because the output `A_i` is generated, the pair is not a fresh same-target
matching.  It is an A-layer hit in the lifted target graph.

## Cycle Form

An R-b5 A-layer cycle:

```text
A_{i_0} -> A_{i_1} -> ... -> A_{i_m} -> A_{i_0}
```

under row `b` is therefore a cycle of base-bridge A-hits:

```text
D_{i_r}=A_{i_{r+1}}.
```

At every vertex `A_{i_r}` it carries the generated same-input split:

```text
row b:       A_{i_r} -> A_{i_{r+1}},
row x_{i_r}: A_{i_r} -> b.
```

and the lifted `H_{A_{i_r}}` pair:

```text
H_{i_r}    -> A_{i_{r+1}},
Beta_{i_r} -> b.
```

## Consequence

R-b5 is not an independent fresh recurrence branch.

It is a closed chain of already routed base-bridge A-layer hits.  Therefore in
a minimal relay loop, an R-b5 cycle must be treated as one of:

```text
1. a visible/generated attachment if any A-cycle vertex is in the retained
   footprint;
2. a repeated lifted beta-anchor/row-b partner configuration;
3. a regenerated clean external bridge at a smaller A-layer footprint;
4. or a same-row recurrence boundary for row b.
```

The remaining nonlocal step is again minimality/descent: show that a closed
chain of A-layer base-bridge hits cannot be the first unresolved recurrence in
a minimal relay loop unless it repeats a full ported interval in an
independent role.
