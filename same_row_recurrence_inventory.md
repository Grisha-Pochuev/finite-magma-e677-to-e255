# Same-Row Recurrence Inventory

Date: 2026-06-19.

Status:

```text
active inventory / remaining recurrence frontier after clean bridge reductions
```

## Purpose

After:

```text
clean_external_bridge_tenth_stage_reduction_lemma.md
```

the clean external bridge route no longer has an independent fresh bridge
residual.  The remaining obstruction is a family of same-row or same-ladder
recurrence boundaries.

This file collects them so the next proof step can merge them instead of
reopening old bridge cases.

## General Warning

A same-row recurrence is not by itself a contradiction.

Reference:

```text
ported_interval_recurrence_boundary.md
target_advance_row_orbit_lemma.md
```

It becomes decisive only if the repeated full ported interval occurs in two
independent branch roles, or if the row cycle attaches back to the visible
crossed-fan/core footprint.

## Recurrence Types Already Present

### R-a. Row-a bridge swap

Reference:

```text
row_a_bridge_loop_recurrence_boundary.md
```

Form:

```text
a*k=b,
a*b=k.
```

So row `a` swaps:

```text
b <-> k.
```

Ported recurrence:

```text
(b,k,k) -> (k,b,b) -> (b,k,k).
```

### R-b1. Generated row swap in H_b

Reference:

```text
right_b_orbit_local_repeat_roles.md
```

Form:

```text
A_i=x_{i+1}.
```

Then row `x_i` swaps:

```text
b <-> x_{i+1}.
```

The `H_b` edge is a loop:

```text
x_{i+1} -> x_{i+1}.
```

### R-b2. Right-b fixed orbit point

Reference:

```text
right_b_orbit_local_repeat_roles.md
```

Form:

```text
x_i*b=x_i,
x_i!=b.
```

This is a closed right-`b` orbit boundary, not a right fixer for the target
`b`.

### R-b3. Row-b fixed point

Reference:

```text
right_b_orbit_local_repeat_roles.md
```

Form:

```text
H_i=A_i,
b*A_i=A_i.
```

This is a row-`b` fixed point at `A_i`, again not a right fixer for `b`.

### R-b4. Closed right-b cycle

Reference:

```text
right_b_orbit_first_repeat_boundary.md
right_b_orbit_first_repeat_fan_lemma.md
rb4_first_repeat_target_swap_relay_lemma.md
rb4_internal_repeat_right_b_footprint_descent_lemma.md
```

Form:

```text
x_i -> x_{i+1} -> ... -> x_j=x_i
```

under right multiplication by `b`.

This creates an incoming fan in `H_b` at the first repeated vertex, so it is
not neutral.  The remaining gap is to attach that fan back to the visible core
or to another independent branch role.

Sharper status: the repeated vertex has an automatic outgoing continuation
because `A_i=pred_{x_i}(b)` gives `x_i -> A_i*b` in `H_b`.  Thus R-b4 is a
first-merge target-swap relay: after swapping target from `b` to the repeated
vertex, it becomes a mixed `2+1` junction or an outgoing triple fan.

If the repeat is internal (`i>0`), the closed right-`b` cycle has strictly
smaller footprint than the old right-`b` segment up to first repeat.  If it
returns to `x_0=a`, it is a visible/original fan attachment.

### R-b5. Row-b A-layer/predecessor cycle

References:

```text
row_b_a_layer_cycle_boundary.md
row_b_predecessor_tower_dichotomy_boundary.md
row_b_tower_first_hit_role_map.md
rb5_a_layer_cycle_base_bridge_relay_lemma.md
rb5_a_layer_footprint_descent_boundary.md
rb5_start_return_a_cycle_beta_pair_boundary.md
rb5_beta_necklace_reduction_candidate.md
rb5_beta_necklace_first_hit_reduction_lemma.md
```

Form:

```text
H_i -> A_i
```

continues through a row-`b` predecessor or successor cycle without a watched
hit.  Later beta and Z3 pressure reduce the independent fresh cases, but a
pure row-`b` same-row recurrence remains a boundary.

Sharper status: every A-layer cycle edge `b*A_j=A_i` is the unavoidable base
row-b/generated bridge at `A_j`, with row-`b` output `D_j=A_i` hitting the
generated A-layer.  So R-b5 is a closed chain of base-bridge A-hits, not a
fresh recurrence unrelated to the clean external bridge reductions.

An internal first repeat in the A-layer gives a smaller A-cycle footprint.
Only the start-return minimal A-cycle remains as a genuine recurrence
boundary.

The start-return minimal A-cycle carries a cyclic necklace of lifted
beta-anchor pairs:

```text
H_i -> next A,
Beta_i -> b.
```

The current candidate is that this necklace folds into the already proved
beta/Z3 reductions; the missing step is a finite first-hit coverage argument
around the A-cycle.

Sharper status: the first-hit coverage is now recorded in:

```text
rb5_beta_necklace_first_hit_reduction_lemma.md
```

So the start-return R-b5 A-cycle has no independent fresh residual beyond
visible hits, beta/Z3 routes, full-interval collisions, or same-row
recurrence.

### R-x. Row-x_i beta-chain recurrence

References:

```text
beta_fresh_extension_first_hit_boundary.md
fresh_beta_extension_eventual_x_hit_lemma.md
deep_beta_x_hit_reduction_lemma.md
```

The genuinely fresh beta-chain no longer remains independent: if it does not
hit earlier watched layers, it eventually hits the generated X-layer.  Any
same-row row-`x_i` recurrence that appears during this route is therefore
already coupled to a beta/X hit or a beta-anchored square.

### R-Z. Fixed-target source-ladder recurrence

References:

```text
fixed_target_source_orbit_first_merge_boundary.md
fixed_target_source_orbit_ladder_lemma.md
z3_paired_source_ladder_eventual_merge_lemma.md
```

Form:

```text
r_n=r_m
```

inside a source-successor ladder:

```text
r_{n+1}=r_n*A_j.
```

This is not a left-row orbit cycle.  It is a repeat of a source row in the
fixed target graph `H_{A_j}`.  If it is cross-ladder, it is routed as a
ported-interval collision.  If it is same-ladder, it is the remaining Z3
same-row/source recurrence boundary.

## Current Unified Recurrence Frontier

The remaining recurrence problem is:

```text
Show that every same-row recurrence above either:

1. attaches to the visible crossed-fan/core footprint;
2. repeats a full ported interval in an independent branch role;
3. regenerates a smaller clean external bridge already covered by the
   tenth-stage reduction;
4. or forces a right fixer/E255 witness for the bad target.
```

The first target `R-b4/R-b5` has now been sharpened: row-b cycles are shared by the
original clean external bridge and by the Z3 generated side:

```text
x_j -> b -> D_j -> ...
H_j -> A_j -> D_j -> ...
```

R-b4 relays by target swap at the first repeated right-`b` vertex.  R-b5 is a
closed chain of base-bridge A-layer hits.  Both have explicit local footprint
descent except for the start-return minimal cycle cases.  The remaining task
is the global minimality/descent step: prove that the relayed fan or A-hit
chain is visible-attached, smaller in the global relay measure, or repeats a
full ported interval in an independent role.
