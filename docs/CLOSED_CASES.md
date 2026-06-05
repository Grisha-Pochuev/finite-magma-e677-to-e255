# Closed cases and recorded evidence

This file is the compact public status table.  It separates closed computational
or structural regions from the open proof frontier.

## Main finite-size status

| Region | Status | Evidence in this repository |
| --- | --- | --- |
| Size 5 | Closed | Recorded project status; smoke-testable through `verify_smoke.ps1`. |
| Size 6 | Closed | Recorded project status; no separate public rerun script yet. |
| Size 7 | Closed | Recorded project status; no separate public rerun script yet. |
| Size 8 | Closed | Reproducibility script `verify_size8_closed.ps1`; log `logs/size8_verified_split_log.txt`. |
| Size 9, cases 1-33 | Recorded closed | Recorded in project status, but not yet packaged as an independent public rerun certificate. |
| Size 9, case45 branch `7*0=4` | Closed | File `lemmas/case45_7zero4_closed.md`; related relay files in `lemmas/`. |

## Current open frontier

The project is not claiming a complete proof of `E677 -> E255` yet.

The current active obstruction is the **double interval pressure** frontier.
In the notation used in the research files, nonzero `r_2=t` becomes a common
pivot of two forced intervals:

```text
row b_2:
  u_2 -> 0 -> t

row b_3:
  c_{-1} -> t -> b_4
```

The next candidate lemma says that these two intervals cannot both keep fresh
predecessors while also avoiding the forced pressure in rows `t` and `b_4`.

See:

- `docs/CURRENT_FRONTIER.md`;
- `lemmas/double_interval_pressure_lemma.md`;
- `lemmas/offset_pressure_diamond_lemma.md`;
- `lemmas/two_sided_offset_orbit_lemma.md`.

## Important caveat

Some older closures are recorded in the historical research log rather than in
a polished independent certificate.  This repository therefore distinguishes:

- **verified reproducible checkpoint**: currently the size-8 script and log;
- **recorded closed research region**: closure recorded in project status,
  lemma files, and historical logs;
- **candidate lemma**: a structural statement under active proof development.

The current first public release is strongest for the size-8 computational
checkpoint.  The size-9 material is published as research status and lemma
history, not yet as a standalone public rerun certificate.
