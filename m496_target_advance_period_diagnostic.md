# M496 Target-Advance Period Diagnostic

Date: 2026-06-20.

Status:

```text
diagnostic / supports the period >= 3 residual as non-vacuous
```

## Purpose

This records a short diagnostic for:

```text
target_advance_same_row_period_lemma.md
```

The question was whether the remaining same-source `period >= 3` target-
advance residue is only an artifact of the proof language, or whether it is
visible in the known size-496 E677 model.

## Script

The permanent script is:

```text
tools/m496_target_advance_periods.js
```

It uses the same M496 operation as:

```text
tools/core_orientation_diagnostics.js
```

## Result

The scan over all `496` rows found:

```text
row type histogram:
  "1,5,10,30": 496 rows

cycle length histogram:
  period 1:   496 cycles
  period 5:  1488 cycles
  period 10: 1488 cycles
  period 30: 7440 cycles

max period: 30
rows with only periods <= 2: 0
```

## Interpretation

The known M496 model has no row whose target-advance behavior is made only
from fixed/swap periods.

So after the proof removes periods `1` and `2` by the local fixed/swap
classification, the period `>= 3` same-source residual is still a real
structural phenomenon in known E677 behavior.

This diagnostic does not prove the G12 residual possible in a bad-target core.
It only warns that the remaining period `>= 3` case cannot be dismissed as a
short-cycle artifact.
