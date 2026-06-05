# Senior Far Transfer Lemma

Status:

```text
historical transfer lemma
```

This file summarizes the senior/far transfer mechanism discovered in the
case45 branch analysis.

## Idea

A far value can look independent from the local bad-cycle block.  The
senior/far transfer showed that this independence is often false: `E677`
forces the far value to transfer pressure back into an older row.

Schematic form:

```text
far forced value
  -> senior row interaction
  -> predecessor relay
  -> older occupied row or zero pressure
```

## Current role

This is part of the historical evidence for the no-free-tail philosophy:
fresh-looking values are often forced to return, descend, or collide.

Related files:

```text
far_row_killer_lemma.md
main_bad_cycle_no_free_tail_lemma.md
double_interval_pressure_lemma.md
```

