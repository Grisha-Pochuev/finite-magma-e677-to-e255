# Closed cases and recorded evidence

This file is the compact public status table.  It separates closed computational
or structural regions from the open proof frontier.

## Main finite-size status

| Region | Status | Evidence in this repository |
| --- | --- | --- |
| Size 5 | Recorded closed | Recorded project status; `verify_smoke.ps1` includes only a short one-case environment check, not a complete certificate. |
| Size 6 | Recorded closed | Recorded project status; no separate public rerun script yet. |
| Size 7 | Recorded closed | Recorded project status; no separate public rerun script yet. |
| Size 8 | Closed | Reproducibility script `verify_size8_closed.ps1`; log `logs/size8_verified_split_log.txt`. |
| Size 9, cases 1-33 | Recorded closed | Recorded in project status, but not yet packaged as an independent public rerun certificate. |
| Size 9, case45 branch `7*0=4` | Closed | File `lemmas/case45_7zero4_closed.md`; related relay files in `lemmas/`. |
| Normalized size-9 role `u=b_3` | Recorded closed | Final occupied fan-tip roles `C=b_7` and `C=b_6` closed in bounded diagnostics; see `lemmas/bad_tail_u_equals_s_fan_lemma.md`. |

## Current open frontier

The project is not claiming a complete proof of `E677 -> E255` yet.

The current active obstruction is the **three-source good-six pressure**
frontier.  Three source rows share a forced edge:

```text
q*0=P
q*P=T
T*q=h.
```

Each source produces a bridge, and each bridge produces a backward zipper
return.  Bounded size-9 diagnostics close the normalized role, but the general
symbolic first-intersection classification of three bridge paths is still
missing.

See:

- `docs/CURRENT_FRONTIER.md`;
- `lemmas/fan_tip_bridge_expansion_lemma.md`;
- `lemmas/fan_bridge_zipper_extension_lemma.md`;
- `lemmas/terminal_source_anchored_fan_lemma.md`;
- `lemmas/three_source_good_six_pressure_candidate.md`.

## Important caveat

Some older closures are recorded in the historical research log rather than in
a polished independent certificate.  This repository therefore distinguishes:

- **verified reproducible checkpoint**: currently the size-8 script and log;
- **recorded closed research region**: closure recorded in project status,
  lemma files, and historical logs;
- **candidate lemma**: a structural statement under active proof development.

The strongest independently packaged computational checkpoint remains the
size-8 script and log.  The size-9 material is published as research status and
lemma history, not yet as a standalone public rerun certificate.
