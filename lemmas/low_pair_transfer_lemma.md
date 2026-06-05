# Low-Pair Transfer Lemma

Status:

```text
historical working lemma
```

This lemma summarizes an earlier transfer pattern in low rows of the case45
analysis.

## Idea

When two low-row values are forced near the bad-cycle block, `E677` often
transfers pressure from one row to another.  This creates either:

```text
zero hit
occupied-row descent
short return
collision with a previous forced output
```

## Why it mattered

The low-pair transfer was one of the first clear signs that branches were not
closing by accidental search pressure.  They were closing because local
`E677` consequences repeatedly relayed pressure into already occupied rows.

## Current role

The current proof attempt uses the same idea in a more symbolic form:

```text
source_orbit_zipper_lemma.md
edge_predecessor_triangle_lemma.md
double_interval_pressure_lemma.md
```

