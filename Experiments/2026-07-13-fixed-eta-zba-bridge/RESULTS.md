# Results

Status: completed and archived.

## Final run

- GitHub Actions run: <https://github.com/Grisha-Pochuev/finite-magma-e677-to-e255/actions/runs/29212167864>
- workflow head commit: `9fd857118fbf6a7aafc73da53c3092b01a17c6d4`
- validation job: passed
- matrix jobs: 20/20 completed and uploaded artifacts
- useful search time: 350 minutes per matrix job
- aggregate matrix time: 116.67 runner-hours

## Mathematical outcome

No tested target was decided.

- proofs found: **0**
- satisfying models or countermodels found: **0**
- malformed inputs or fatal solver failures: **0**
- normalized outcome of every slot: **timeout without a decisive result**

Therefore this run does **not** prove or refute any of the five targets. It shows only that the selected E prover and Vampire profiles did not decide them within 5 h 50 min.

| Target | E auto | Vampire CASC 4x2500 | Vampire CASC 2x5000 | Vampire SAT 4x2500 |
|---|---|---|---|---|
| `ZB*A=Ib` | timeout | timeout | timeout | timeout |
| `(ZB*Ib)*ZB=c` | timeout | timeout | timeout | timeout |
| `b*(ZB*A)=h` | timeout | timeout | timeout | timeout |
| direct `A=z` | timeout | timeout | timeout | timeout |
| `ZB*A=Ib` plus bad-target condition | timeout | timeout | timeout | timeout |

The negative result is still useful: direct unrestricted ATP saturation of these five encodings is not an immediate closing route at this budget. The next mathematical step should use a stronger structural lemma, a smaller derived subproblem, or a better-guided encoding rather than simply repeating the same matrix.

## Resource outcome

The memory safety design worked.

- maximum tree RSS over all jobs: **9823.3 MiB** (9.593 GiB)
- lowest observed `MemAvailable`: **5214.5 MiB** (5.092 GiB)
- maximum swap used: **0.0 MiB**
- external 12 GiB tree guard activations: **0**
- system OOM / runner shutdowns observed: **0**

Some individual solver workers reached their own 2500 MB or 5000 MB limits. That is expected portfolio behavior and is not the same as exhausting the GitHub machine. The whole process tree remained below 9.7 GiB and at least about 5.1 GiB remained available to the system.

Average peak tree RSS by profile:

| Profile | Mean peak RSS | Range | Worst minimum `MemAvailable` |
|---|---:|---:|---:|
| `e-auto-4x2500` | 8456.5 MiB | 8141.0–8944.5 MiB | 6121.9 MiB |
| `vampire-casc-2x5000` | 9533.4 MiB | 9453.0–9592.9 MiB | 5457.6 MiB |
| `vampire-casc-4x2500` | 9316.0 MiB | 8793.0–9823.3 MiB | 5214.5 MiB |
| `vampire-sat-4x2500` | 2785.4 MiB | 2647.3–2924.0 MiB | 12026.3 MiB |

Runner CPUs were mixed but all AMD in this run:

- AMD EPYC 7763: 14 jobs
- AMD EPYC 9V74: 6 jobs

## Classification correction discovered during review

The stored `RESULT.txt` files label the 15 Vampire slots as `SOLVER_MEMORY_LIMIT`. This label is not the final mathematical/technical outcome. Every Vampire log ends with `SZS status Timeout` and `Proof not found in time`.

The wrapper checked the broad phrase `memory limit` before it checked the final timeout status. Portfolio worker messages therefore shadowed the final solver status. The committed wrapper is corrected so that final `SZS Timeout` / `Termination reason: Time limit` takes precedence, while true final resource exhaustion remains `SOLVER_MEMORY_LIMIT`.

The original artifact labels are preserved in `run-29212167864-summary.csv` as `artifact_result`; the reviewed outcome is stored separately as `normalized_result`. The CSV also records exact artifact IDs and SHA-256 digests, commands' resource outcomes, CPU models, exit codes and per-slot mathematical flags.

The full temporary GitHub artifacts contain the complete solver logs and two-second resource traces. They total roughly 23 MB uncompressed. The committed CSV and this report preserve the information needed to reproduce and interpret the run without adding repetitive sampling data to Git history.

## Launch history

Initial launch commit: `a130e97addde2060ea1596f757f180c0d20cdc92`.

The first attempt failed in the technical launch path. A concrete smoke-test classification defect was corrected in PR #9. Corrected retry commit: `9fd857118fbf6a7aafc73da53c3092b01a17c6d4`.
