# Fixed eta full ATP run — 2026-07-11

Purpose: attack the unresolved fixed eta-return implication

```text
U*Ib=r  =>  A=Ib*c=z
```

from E677, left cancellation, and the strict period-3 setup.

The GitHub Actions portfolio starts 20 independent jobs:

- 10 E prover jobs: `--auto` and `--auto-schedule`;
- 10 Vampire jobs: `casc` and `casc_sat`;
- five equivalent/search-guiding formulations in each pair of modes;
- up to 5 h 45 min of prover time per job;
- all generated problems, logs, metadata, and proof output are uploaded as artifacts.

The five formulations are `base`, `row-image`, `expanded`, `contradiction`, and `ground-boost`. The last adds only explicit ground instances of the universal E677 axiom, so it does not strengthen the theory.
