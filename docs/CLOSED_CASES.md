# Closed cases and recorded evidence

This file is the compact public status table.  It separates closed computational
or structural regions from the open proof frontier.

## Main finite-size status

| Region | Status | Evidence in this repository |
| --- | --- | --- |
| Size 5 | Closed | Reproducibility script `verify_sizes_5_6_7_closed.ps1`; log `logs/sizes_5_6_7_rerun_20260617_143540.txt`. |
| Size 6 | Closed | Reproducibility script `verify_sizes_5_6_7_closed.ps1`; log `logs/sizes_5_6_7_rerun_20260617_143540.txt`. |
| Size 7 | Closed | Reproducibility script `verify_sizes_5_6_7_closed.ps1`; log `logs/sizes_5_6_7_rerun_20260617_143540.txt`. |
| Size 8 | Closed | Reproducibility script `verify_size8_closed.ps1`; log `logs/size8_verified_split_log.txt`. |
| Size 9, cases 1-33 | Recorded closed | Recorded in project status, but not yet packaged as an independent public rerun certificate. |
| Size 9, case45 branch `7*0=4` | Closed | File `lemmas/case45_7zero4_closed.md`; related relay files in `lemmas/`. |
| Normalized size-9 role `u=b_3` | Recorded closed | Final occupied fan-tip roles `C=b_7` and `C=b_6` closed in bounded diagnostics; see `lemmas/bad_tail_u_equals_s_fan_lemma.md`. |

## Current open frontier

The project is not claiming a complete proof of `E677 -> E255` yet.

The current active obstruction is the **branch-closure No-Free-Tail** frontier.
The bridge recursion has been generalized from the old common edge `0 -> P`
to an arbitrary target edge:

```text
q*a=b
q*b=c.
```

The open task is to rule out the remaining branch-closure configurations:
either a triple core fan or a mixed `2+1` core junction.  The project has
finite evidence for this pressure pattern, but it is not yet a proved lemma.

See:

- `docs/CURRENT_FRONTIER.md`;
- `lemmas/double_interval_edge_certificate_lemma.md`;
- `lemmas/bicyclic_component_branch_fan_lemma.md`;
- `lemmas/bad_target_core_fan_lemma.md`;
- `lemmas/bicyclic_core_junction_lemma.md`;
- `lemmas/branch_closure_no_free_tail_candidate.md`.

## Important caveat

Some older closures are recorded in the historical research log rather than in
a polished independent certificate.  This repository therefore distinguishes:

- **verified reproducible checkpoint**: currently the size-5/6/7 script and
  log, plus the size-8 script and log;
- **recorded closed research region**: closure recorded in project status,
  lemma files, and historical logs;
- **candidate lemma**: a structural statement under active proof development.

The size-9 material is published as research status and lemma history, not yet
as a standalone public rerun certificate.
