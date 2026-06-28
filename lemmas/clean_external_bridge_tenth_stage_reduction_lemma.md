# Clean External-Bridge Tenth-Stage Reduction Lemma

Date: 2026-06-19.

Status:

```text
proved reduction / paired Z3 shell reduces to collision routes or same-row recurrence
```

## Purpose

This updates:

```text
clean_external_bridge_ninth_stage_reduction_lemma.md
```

using:

```text
z3_paired_source_ladder_eventual_merge_lemma.md
```

## Ninth-Stage Residuals

The previous residual list was:

```text
N1. same-row recurrence boundaries;

N3. clean paired four-edge shell at A_j:
    H_{A_j} matching
      P      -> S,
      U*p    -> V,
      Beta_j -> b,
      H_j    -> D_j;

    target-advance bridge
      H_S:     A_j -> U,
      H_V:     A_j -> S*V,
      H_b:     A_j -> x_{j+1},
      H_{D_j}: A_j -> b*D_j.
```

## N3 Reduction

The clean paired shell carries two deterministic source-successor ladders in
the finite graph `H_{A_j}`:

```text
p   -> S -> V   -> ...
x_j -> b -> D_j -> ...
```

where the arrows are right multiplication by `A_j`.

At each ladder step, the edge in `H_{A_j}` is:

```text
row r_n: pred_{r_n}(A_j) -> r_{n+1}.
```

The predecessor is controlled by:

```text
pred_{r_{n+1}}(A_j)=(r_n*r_{n+1})*r_n.
```

By finiteness, the paired ladders have a first source-row or edge-endpoint
event.  The first-event roles are:

```text
same input       -> outgoing fan in H_{A_j};
same output      -> incoming fan in H_{A_j};
input-output hit -> directed path in H_{A_j};
same full edge   -> ported-interval source collision;
cross-ladder source hit -> ported-interval repeat across branch roles;
same-ladder source repeat -> same-row recurrence boundary.
```

The first four roles are routed by:

```text
same_target_pair_collision_trichotomy_lemma.md
ported_interval_state_lemma.md
```

The cross-ladder source hit is a branch-role collision unless it has already
been classified as a watched hit.

The only non-routed outcome is:

```text
same-ladder source repeat,
```

which is a same-row recurrence boundary.

## Tenth-Stage Residual List

The clean external bridge is now reduced to:

```text
T1. same-row recurrence boundaries.
```

All independent clean bridge branches from the Y/Z layers have been routed to:

```text
fan/path/full-interval collision,
visible/generated hit,
base row-b/generated bridge,
or same-row recurrence.
```

## Remaining Gap

This does not yet prove the bad target impossible.

The remaining work is to classify the accumulated same-row recurrence
boundaries and decide whether each:

```text
1. attaches back to the visible crossed-fan/core relay;
2. forces a right fixer/E255 witness;
3. produces a smaller clean external bridge already covered above;
4. or remains as a genuine global relay-termination gap.
```

The next useful file should be an inventory of all same-row recurrence
boundaries produced along the clean external bridge route, so they can be
merged instead of handled as separate leftovers.
