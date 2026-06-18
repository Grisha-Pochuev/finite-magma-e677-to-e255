# Minimal Relay Cycle Dichotomy Candidate

Date: 2026-06-17.

Status:

```text
candidate / next No-Free-Tail proof target
```

## Purpose

After the canonical-collapse warning, the main No-Free-Tail route should not
depend on the directed two-edge right-fixer candidate as a black box.

The remaining structural route is to prove that recursive relay cannot cycle.

## Relay State

Track a relay state by:

```text
target b,
split/merge vertex v,
the two active ported intervals from the current majority branches,
the minority/return interval when the state is mixed 2+1.
```

The important part is the full ported interval:

```text
(target,input,output),
```

not only a bridge pair.  A repeated full ported interval reconstructs the same
source row by:

```text
ported_interval_state_lemma.md
```

## Candidate Dichotomy

Take a shortest closed relay cycle, meaning a finite sequence of relays that
returns to an already seen target/split configuration before producing E255.

Then one of the following must happen:

```text
1. a full ported interval repeats in two independent branch occurrences;
2. a full ported interval repeats only in the same source-row role;
3. the cycle has an internal side attachment or extra incidence;
4. the cycle is strict clean theta.
```

Case 1 contradicts two-step source reconstruction.

Case 2 is not automatically contradictory.  It is now isolated in:

```text
ported_interval_recurrence_boundary.md
```

It must be converted either into a smaller bad own-row cycle or into a shorter
target-swapped relay.

Case 3 should contradict minimality of the chosen relay cycle, because the
existing side-attachment and first-return lemmas classify such an incidence as
an earlier relay:

```text
corridor_side_attachment_shortening_lemma.md
earliest_side_attachment_mixed_junction_lemma.md
side_attachment_orientation_reduction_lemma.md
minority_core_return_relay_lemma.md
first_merge_target_swap_junction_dichotomy.md
```

Case 4 is impossible by:

```text
strict_clean_theta_exclusion_lemma.md
```

## What Remains To Prove

The missing formal step is case 2:

```text
In a shortest closed relay cycle, any extra incidence creates a strictly
shorter closed relay cycle or a repeated full ported interval.
```

This is now the cleanest No-Free-Tail frontier.  It avoids the circular
two-edge witness route and uses the proved local relay classifications.

## Minimality Measure To Use

The useful minimal object should not be "the first relay found".  It should be
chosen lexicographically:

```text
1. minimum number of vertices in the two-branch corridor between the active
   split and first merge;
2. subject to that, earliest possible return/side-attachment point;
3. subject to that, minimum number of relays before the target/split pair
   repeats.
```

This choice is designed to make every extra incidence expensive:

```text
an internal side attachment before the sink
=> a new split strictly inside the old corridor;

an extra incidence at the sink
=> target-swap relay at the endpoint;

an extra incidence at the split
=> either the retained third core incidence or a shorter return to the split.
```

The first two cases are already locally classified.  The remaining proof
obligation is to show that the new relayed corridor is strictly smaller in the
lexicographic measure unless it repeats a full ported interval.

## Exact Local Proof Obligation

The key unresolved sentence can be isolated as:

```text
Let C be a minimal active two-branch corridor in the cycle core.
If an extra core incidence attaches at an internal vertex w of C, then the
relay generated at w either:

1. has first merge before the old sink z;
2. repeats one of the old full ported intervals;
3. or returns to the old split, giving a shorter closed relay cycle.
```

This is purely the No-Free-Tail step.  It should be attacked before returning
to right-fixer candidates.

The graph part of this sentence is now separated in:

```text
corridor_side_attachment_shortening_lemma.md
```

That file also records a caution: a side attachment gives a smaller footprint
on the old corridor, but its outside return path can be long.  Therefore the
minimality measure must prioritize old-corridor footprint / first-return
position, not just total vertex count.

What remains algebraic/relay-specific is to prove that this footprint descent
is respected by the target-swapped relay, or else that the relay repeats a full
ported interval.

Together with `ported_interval_recurrence_boundary.md`, the active obstruction
has been narrowed to same-row recurrence in a minimal closed relay cycle.

There is one sharper split for returns to the old split:

```text
figure_eight_closure_crossed_fan_boundary.md
```

If two distinct branch returns come back to the old split, the closure is a
crossed double fan.  Only the degenerate same-row return remains outside that
candidate.
