# Project Status

Date: 2026-06-08.

## Problem

The project asks whether the finite-magma identity

```text
E677: x = y * (x * ((y * x) * y))
```

implies

```text
E255: x = ((x*x)*x)*x.
```

The full theorem remains open in this repository.

## Finite and computational status

```text
sizes 5, 6, 7, 8: closed
size 8: public rerun script and recorded verification log included
size 9, cases 1-33: recorded closed
case45, branch 7*0=4: recorded closed
normalized size-9 role u=b_3: recorded closed
```

The size-8 checkpoint is the strongest independently packaged computational
certificate.  Some size-9 closures remain research records rather than
standalone public rerun scripts.

## Structural progress

The earlier double-interval and paired-predecessor analysis has developed into
a common-edge fan framework.

Recent proved ingredients include:

```text
two-step source reconstruction;
aligned-overlap obstruction;
two-sided common-edge fan;
short fan-spine descent lemmas;
bridge expansion from every fan tip;
zipper extension from every bridge;
terminal-source anchoring to the original bad tail.
```

## Current frontier

The main remaining finite pattern is a three-source fan attached to a good
six-cycle.

Current candidate:

```text
lemmas/three_source_good_six_pressure_candidate.md
```

The next work is symbolic first-intersection classification for the three
bridge paths.  A new broad search is not the next step.

## Read next

1. `docs/RESEARCH_UPDATE_2026-06-08.md`
2. `docs/LEMMA_STATUS.md`
3. `docs/CURRENT_FRONTIER.md`
4. `lemmas/fan_tip_bridge_expansion_lemma.md`
5. `lemmas/fan_bridge_zipper_extension_lemma.md`
6. `lemmas/terminal_source_anchored_fan_lemma.md`
7. `lemmas/three_source_good_six_pressure_candidate.md`

