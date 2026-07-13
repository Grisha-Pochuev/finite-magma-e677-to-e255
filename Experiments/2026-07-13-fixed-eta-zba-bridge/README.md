# Fixed eta ZBA bridge run — 2026-07-13

## Purpose

This run tested the fixed-eta period-3 frontier:

```text
z*h=b, b*h=c, c*h=z,
b*Ib=h, c*Ic=h,
A=Ib*c, K=A*Ib, ZB=z*b,
r*b=z, r*z=U, U*r=h, U*Ib=r,
U*c=ZB, ZB*c=K.
```

The shortest closing bridge under test was:

```text
ZB*A=Ib  =>  A=z.
```

The narrower internal target was:

```text
(ZB*Ib)*ZB=c.
```

## Problems

- `01-zba-bridge.p`: prove `ZB*A=Ib`.
- `02-zbib-zb-c.p`: prove `(ZB*Ib)*ZB=c`.
- `03-b-zba-h.p`: prove `b*(ZB*A)=h`.
- `04-direct-az.p`: control target, prove `A=z`.
- `05-zba-bad-target.p`: prove `ZB*A=Ib` with the additional bad-target condition.

## Matrix

Each problem was tested by four profiles:

1. E prover, four-process auto schedule, 2500 MB per worker.
2. Vampire CASC, four workers, 2500 MB per worker.
3. Vampire CASC, two workers, 5000 MB per worker.
4. Vampire CASC with satisfiability intent, four workers, 2500 MB per worker.

The useful search limit was 350 minutes per job. The whole process tree was monitored and softly stopped only if it remained above 12 GiB or the machine fell below 2.5 GiB available memory.

## Completed run

- Run: <https://github.com/Grisha-Pochuev/finite-magma-e677-to-e255/actions/runs/29212167864>
- Head commit: `9fd857118fbf6a7aafc73da53c3092b01a17c6d4`
- Validation: passed.
- Matrix: 20/20 jobs completed and uploaded artifacts.
- Proofs: 0.
- Models/countermodels: 0.
- Technical crashes: 0.
- Final reviewed outcome: all 20 slots timed out without a decisive result.

See `RESULTS.md` for the interpretation and resource summary. The complete per-slot machine-readable record is in `run-29212167864-summary.csv`.

## Historical files

`workflow-used.yml` records the workflow configuration used for the corrected retry. The active workflow copy is `.github/workflows/fixed-eta-zba-bridge-2026-07-13.yml`.

The artifact `RESULT.txt` labels from the completed Vampire jobs are preserved in the CSV, but they were reviewed against the solver logs. The logs end with `SZS status Timeout`; the wrapper has been corrected so final timeout status takes precedence over incidental worker-level memory-limit messages.
