# Project Status

Date: 2026-06-25.

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
sizes 5, 6, 7: public rerun script and recorded verification log included
size 8: public rerun script and recorded verification log included
size 9, cases 1-33: recorded closed
case45, branch 7*0=4: recorded closed
normalized size-9 role u=b_3: recorded closed
```

No new finite-size closure is claimed in this update.  The new material is a
structural relay-reduction layer and a set of bounded diagnostics around the
current residual.

## Reproducible finite checkpoints

Sizes `5`, `6`, and `7` are rerunnable through:

```text
verify_sizes_5_6_7_closed.ps1
logs/sizes_5_6_7_rerun_20260617_143540.txt
```

Size `8` is rerunnable through:

```text
verify_size8_closed.ps1
logs/size8_verified_split_log.txt
```

Some size-9 closures remain research records rather than standalone public
rerun scripts.

## Structural progress since 2026-06-17

The branch-closure layer has been pushed through several local relay
reductions:

```text
crossed-fan clean external bridge routing;
right-b orbit and ported-interval transition reductions;
beta-layer and reversible-square reductions;
same-row recurrence inventory;
shared-step anchored triangle reduction;
anchored-X3/M7 source-orbit routing.
```

The main published continuation point is:

```text
NEXT_ACTION.md
```

## Current frontier

The active residual is:

```text
shared-step anchored triangle / anchored-X3 / M7
clean same-orbit right-h self-repeat
```

The strong target around a shared step is:

```text
U*h = W*h.
```

The negated branch has been reduced to an anchored-X3/M7 configuration.  Its
first finite events are routed unless the first event is a clean self-repeat
inside one right-`h` source orbit.

## Experimental ATP surface

The repository now includes experimental ATP/TPTP templates:

```text
atp/anchored_x3_m7_self_repeat.p
atp/anchored_m7_cycle_end.p
```

These are working surfaces for testing local consequences.  They are not a
formal proof and should not be cited as a closed theorem.

## Boundary

Not proved:

```text
branch-closure No-Free-Tail Lemma;
anchored identity U*h=W*h in full generality;
E677 => E255 for all finite magmas.
```

## Read next

1. `NEXT_ACTION.md`
2. `docs/RESEARCH_UPDATE_2026-06-25.md`
3. `docs/CURRENT_FRONTIER.md`
4. `docs/RESULTS_INDEX.md`
5. `docs/LEMMA_STATUS.md`
6. `docs/REPRODUCIBILITY.md`
