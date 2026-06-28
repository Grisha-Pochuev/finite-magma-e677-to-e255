# Minimal G12 Loop Normal Form Boundary

Date: 2026-06-20.

Status:

```text
boundary / normal form for the remaining global relay loop
```

## Purpose

This combines:

```text
relay_minimality_measure_candidate.md
relay_same_source_return_split_boundary.md
fixed_target_same_source_return_collapse_lemma.md
target_advance_same_row_period_lemma.md
two_row_target_advance_window_separation_lemma.md
two_row_orbit_theta_boundary.md
two_row_first_extra_intersection_routing_lemma.md
clean_first_extra_matching_bridge_alignment.md
clean_external_bridge_twelfth_stage_reduction_lemma.md
strict_clean_theta_exclusion_lemma.md
```

It records what a counterexample to relay termination must look like after all
local clean external bridge and recurrence reductions.

## Assumption

Assume, for contradiction, that a bad target has a closed relay loop that does
not produce:

```text
1. a right fixer;
2. visible/core attachment that closes by an existing local relay;
3. an independent full ported-interval collision;
4. strict clean theta.
```

Choose such a loop minimal by:

```text
relay_minimality_measure_candidate.md
```

using the lexicographic measure `M0-M4`.

## Normal Form Consequences

### No internal side attachment

If an extra core incidence attaches to an internal old-corridor vertex, then:

```text
corridor_side_attachment_shortening_lemma.md
```

gives a new relay corridor with smaller old-corridor footprint `M0`.

So minimality forbids internal side attachments.

### No R-b4/R-b5 internal recurrence

If R-b4 is internal, it has smaller right-`b` footprint `M2`.

If R-b5 is internal, it has smaller A-layer footprint `M3`.

Thus minimality forbids those as first unresolved recurrences.

The start-return R-b5 beta necklace is routed by:

```text
rb5_beta_necklace_first_hit_reduction_lemma.md
```

so it is not a fresh exception.

### No fresh beta/Z3/local recurrence branch

The local recurrence inventory is exhausted by:

```text
clean_external_bridge_twelfth_stage_reduction_lemma.md
```

Therefore no fresh beta, Z3, source-ladder, or local swap/fixed recurrence
can appear as a new branch outside the global relay loop.

### No independent return to old split

If two distinct source rows return to the old split, then:

```text
relay_same_source_return_split_boundary.md
figure_eight_closure_crossed_fan_boundary.md
```

turn it into a crossed fan, whose local case tree is already exhausted back
to G12.

In a minimal loop, this either gives a smaller/earlier G12 state or repeats a
full ported interval in an independent role.

Thus the remaining returns must be same-source row-orbit returns.

The fixed-target same-source cleanup:

```text
fixed_target_same_source_return_collapse_lemma.md
```

adds one useful sharpening: a same-source return to the same old split inside
the same `H_b` is not a new incidence at all.  It is the same edge again.
Therefore any genuine new fixed-target return to the old split is already an
independent return and routes through the crossed-fan path above.

So the remaining same-source returns are only target-advance row-orbit
recurrences, not new fixed-target double returns.

The pure same-row period is classified by:

```text
target_advance_same_row_period_lemma.md
```

Periods `1` and `2` are local fixed/swap recurrences already routed by the
local recurrence inventory.  Therefore a genuine remaining same-source
target-advance component must have row-orbit period at least `3`.

When two active branch rows share a target-advance step, the local window is
separated on both sides by:

```text
two_row_target_advance_window_separation_lemma.md
```

So a remaining two-row step has no left-neighbor equality and no right-neighbor
equality unless it already gives an independent full ported-interval
collision.

The separated windows then have the global split:

```text
two_row_orbit_theta_boundary.md
```

Either the two row cycles have a first extra intersection, or their union is a
clean two-row orbit theta in the target-advance state space.

The first-extra-intersection branch is routed by:

```text
two_row_first_extra_intersection_routing_lemma.md
```

to a full interval collision, fan/path attachment, or clean same-input
two-target bridge after target advance.

The clean matching subcase is aligned with the V3-type bridge frontier in:

```text
clean_first_extra_matching_bridge_alignment.md
```

## Remaining Normal Form

A genuine remaining G12 counterexample must therefore be:

```text
a closed relay loop with no internal side attachment,
no independent return,
no fresh clean external bridge subcase,
no beta/Z3/local recurrence escape,
and only same-source target-advance row-orbit recurrences of period at least
3, assembled from separated two-row target-advance windows whose row cycles
either have a first extra intersection or form a clean orbit theta.
```

Equivalently, every active ported interval advances along its own source-row
cycle and returns only to itself in the same branch role.

## Next Target

The next proof step should compare this normal form with:

```text
strict_clean_theta_exclusion_lemma.md
```

The likely final obstruction is:

```text
translate the clean orbit-theta branch to the strict clean theta already
excluded, and prove descent/admissibility for the V3-type bridge left by the
clean first-extra matching branch.
```
