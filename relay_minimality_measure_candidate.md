# Relay Minimality Measure Candidate

Date: 2026-06-19.

Status:

```text
candidate / lexicographic measure for the remaining same-row recurrence gap
```

## Purpose

This refines the measure proposed in:

```text
minimal_relay_cycle_dichotomy_candidate.md
corridor_side_attachment_shortening_lemma.md
clean_external_bridge_to_relay_recurrence_frontier.md
```

The clean external bridge route has reduced to:

```text
E11. global same-row recurrence / minimal relay descent.
```

The remaining proof needs one measure that handles both:

```text
1. ordinary side attachments inside a relay corridor;
2. row-b recurrence descendants R-b4/R-b5 from the clean external bridge.
```

## Proposed Minimal Object

Among all hypothetical bad-target relay loops with no right fixer and no
independent full ported-interval collision, choose one lexicographically
minimal by:

```text
M0. old-corridor footprint:
    the number of old relay-corridor vertices between the active split and
    first merge, measured on the retained old core corridor;

M1. first-event position:
    the earliest point on that old corridor where the next side attachment,
    first merge, return, or recurrence-generated relay is born;

M2. right-b first-repeat footprint:
    for clean external bridge descendants, the length of the right-b orbit
    segment up to first repeat;

M3. A-layer base-bridge footprint:
    for R-b5 descendants, the length of the generated A-layer base-bridge
    chain up to first repeat;

M4. relay period:
    the number of target-swap/relay steps before the same target/split
    configuration recurs.
```

This measure deliberately prioritizes old-corridor footprint over the total
length of any outside return path.  That matches:

```text
corridor_side_attachment_shortening_lemma.md
```

where the outside path may be long but its old-corridor footprint is smaller.

## Extension For First-Extra V3 Bridges

The period `>= 3` same-source residual is now sharpened by:

```text
two_row_orbit_theta_boundary.md
two_row_first_extra_intersection_routing_lemma.md
clean_first_extra_matching_bridge_alignment.md
general_v3_bridge_descent_boundary.md
```

The clean first-extra branch creates a general V3-type same-input two-target
bridge.  To measure it, extend the lexicographic object by:

```text
M5. first-extra offset:
    the first position i>1 where two active same-row target-advance cycles
    meet again after their shared step;

M6. clean V3 bridge rank:
    the first clean same-input two-target bridge born at that first extra
    intersection.
```

The intended use is:

```text
same-output fan / path / full interval / core hit
=> already routed;

clean V3 bridge
=> must be admissible as a smaller measured relay object under M0-M6,
   or else the first-extra branch remains the exact residual.
```

## Compatibility With R-b4

For R-b4, the first repeat is:

```text
x_i=x_j,
0 <= i < j.
```

If:

```text
i=0,
```

the recurrence returns to the original visible crossed-fan vertex and is not a
clean independent recurrence.

If:

```text
i>0,
```

then:

```text
rb4_internal_repeat_right_b_footprint_descent_lemma.md
```

gives:

```text
j-i < j.
```

So the regenerated relay has smaller `M2`.

Thus R-b4 is incompatible with minimality unless:

```text
visible/core attachment,
independent full ported-interval collision,
or failure of admissibility for the regenerated relay
```

has already occurred.

## Compatibility With R-b5

For R-b5, the first A-layer repeat is:

```text
A_{i_m}=A_{i_n},
0 <= m < n.
```

If:

```text
m>0,
```

then:

```text
rb5_a_layer_footprint_descent_boundary.md
```

gives:

```text
n-m < n.
```

So the regenerated A-layer base-bridge cycle has smaller `M3`.

The only R-b5 case not removed by this local measure is:

```text
m=0,
```

a start-return minimal A-cycle.  This case is no longer an independent local
residual after:

```text
rb5_beta_necklace_first_hit_reduction_lemma.md
```

because its lifted beta-anchor necklace routes to existing beta/Z3 reductions
or to the unified same-row recurrence frontier.

## Compatibility With Ordinary Side Attachment

If an extra core incidence attaches at an internal old-corridor vertex `w`,
then:

```text
corridor_side_attachment_shortening_lemma.md
```

constructs a new corridor whose old-corridor footprint is a proper subpath of
the old one.

So the new relay has smaller `M0`, regardless of the length of the outside
return path.

## Remaining Unproved Step

The measure candidate reduces the remaining proof to one exact sentence:

```text
Every regenerated relay object produced by R-b4, R-b5, an ordinary side
attachment, or a clean first-extra V3 bridge is admissible as a relay object
measured by M0-M6, unless it has already produced a visible/core hit,
fan/path hit, same-output first-extra fan, or an independent full
ported-interval collision.
```

Once this admissibility sentence is proved, minimality rules out all internal
side attachments and internal row-b recurrence repeats.

The remaining cases are therefore:

```text
1. clean orbit-theta translation to strict clean theta;
2. clean first-extra V3 bridge descent/admissibility;
3. strict clean theta, already excluded.
```
