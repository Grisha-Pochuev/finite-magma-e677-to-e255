# Clean External Bridge To Relay-Recurrence Frontier

Date: 2026-06-19.

Status:

```text
frontier alignment / clean external bridge now feeds the global recurrence gap
```

## Purpose

This connects:

```text
clean_external_bridge_tenth_stage_reduction_lemma.md
same_row_recurrence_inventory.md
```

to the global No-Free-Tail files:

```text
relay_termination_frontier.md
minimal_relay_cycle_dichotomy_candidate.md
ported_interval_recurrence_boundary.md
```

## Main Point

The clean external bridge route no longer leaves an independent fresh bridge
residual.

After the tenth-stage reduction, every non-visible clean branch has been
routed to:

```text
fan/path/full-interval collision,
visible/generated hit,
base row-b/generated bridge,
or same-row recurrence.
```

The only remaining clean external bridge obstruction is therefore:

```text
T1. same-row recurrence boundaries.
```

This is the same obstruction isolated in the global relay frontier:

```text
same full ported interval repeating in one source-row role
```

rather than in two independent branch roles.

## How The Row-b Repeats Feed Relay

A first repeat of the right-`b` orbit is not neutral:

```text
right_b_orbit_first_repeat_fan_lemma.md
```

It creates:

```text
1. a fresh incoming common-edge fan at the repeated vertex; or
2. an enlarged incoming fan at the original crossed vertex; or
3. a visible-source hit.
```

Thus an `R-b4` recurrence from:

```text
same_row_recurrence_inventory.md
```

regenerates an ordinary bad-target fan/relay object.  If that regenerated fan
is disjoint from the old visible footprint, the clean external bridge
reductions apply again.  If it is not disjoint, it is a core/visible
attachment.

This is sharpened in:

```text
rb4_first_repeat_target_swap_relay_lemma.md
rb4_internal_repeat_right_b_footprint_descent_lemma.md
```

The repeated right-`b` vertex has an automatic outgoing continuation, so R-b4
is a first-merge target-swap relay to a mixed `2+1` junction or outgoing
triple fan.  If the repeat is internal, it also has a strictly smaller
right-`b` footprint; if it returns to `x_0=a`, it is a visible/original fan
attachment.

The row-b A-layer cycle case R-b5 is sharpened in:

```text
rb5_a_layer_cycle_base_bridge_relay_lemma.md
rb5_a_layer_footprint_descent_boundary.md
```

Every A-layer cycle edge is a base row-b/generated bridge whose row-`b` output
hits the generated A-layer.  Internal A-layer repeats give smaller A-cycle
footprints; only start-return minimal A-cycles remain.

## Why This Is Not Yet A Proof

This still requires a minimality or descent argument.

The possible loop is:

```text
clean external bridge
-> same-row recurrence
-> regenerated fan
-> new clean external bridge
-> same-row recurrence
-> ...
```

The tenth-stage reduction shows that the loop cannot escape into fresh beta,
same-target matching, or Z3 paired-ladder branches.  But it does not yet show
that the regenerated fan is smaller or that a full ported interval repeats in
an independent branch role.

## Exact Next Target

Use the minimal relay-cycle framework:

```text
minimal_relay_cycle_dichotomy_candidate.md
```

and prove the descent statement for row-b recurrence:

```text
In a minimal clean external-bridge relay loop, an R-b4/R-b5 row-b recurrence
regenerates a standard relay junction or base-bridge A-hit chain whose
local footprint is strictly smaller, unless it is a start-return minimal
cycle, repeats a full ported interval in an independent branch role, or hits
the visible core.
```

This would merge the clean external bridge route into the global
No-Free-Tail proof rather than leaving it as a separate case tree.
