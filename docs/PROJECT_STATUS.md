# Project Status

Date: 2026-06-17.

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

The sizes `5`, `6`, and `7` closure is now independently rerunnable from this
repository through:

```text
verify_sizes_5_6_7_closed.ps1
logs/sizes_5_6_7_rerun_20260617_143540.txt
```

This script checks all `38` normalized row-0 representatives across sizes
`5`, `6`, and `7`.

The size-8 checkpoint remains separately packaged through:

```text
verify_size8_closed.ps1
logs/size8_verified_split_log.txt
```

Some size-9 closures remain research records rather than standalone public
rerun scripts.

## Structural progress

The earlier common-edge fan and zipper mechanism has been generalized into an
arbitrary-target bridge recursion.

Recent proved ingredients include:

```text
complete certificate for every target edge q*a=b, q*b=c;
labeled right-translation graph constraints;
right-P orbit bridge recursion;
cycle-entry two-sided fan creation;
hub transport for the new fan center;
target-swap fan duality;
balanced witness reduction from a right fixer;
bicyclic core branch-fan reduction.
```

## Current frontier

The active candidate is the branch-closure No-Free-Tail Lemma.

Current candidate files:

```text
lemmas/branch_closure_no_free_tail_candidate.md
lemmas/crossed_double_fan_pressure_candidate.md
```

The exact open task is to rule out the remaining branch-closure configurations:

```text
triple core fan;
mixed 2+1 core junction.
```

The project has finite evidence for crossed double-fan exclusion in raw-label
searches of sizes `6` and `7`, but that evidence is not promoted to a general
lemma.

## Audit correction

The earlier size-8/9 crossed-fan and size-9 directed-diamond claims used an
invalid double normalization and are withdrawn.  They should not be cited as
closed cases.

## Read next

1. `docs/RESEARCH_UPDATE_2026-06-17.md`
2. `docs/LEMMA_STATUS.md`
3. `docs/CURRENT_FRONTIER.md`
4. `docs/CLOSED_CASES.md`
5. `docs/REPRODUCIBILITY.md`
