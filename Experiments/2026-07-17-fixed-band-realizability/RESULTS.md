# Results

Status: 30-minute pilot completed and reviewed.

## Launch record

- GitHub Actions run: https://github.com/Grisha-Pochuev/finite-magma-e677-to-e255/actions/runs/29538663524
- head SHA: `2a9db307d4824d9d0701487b0509f252bf41e06c`
- validation and four-profile end-to-end gate: passed
- matrix jobs: 20/20 completed
- collected summaries: 20/20 valid

## Mathematical outcome

No target was decided.

- proofs: **0**
- models or satisfiable results: **0**
- E prover time limits: **5**
- Vampire final timeouts: **15**
- memory guards: **0**
- technical failures: **0**

Every target timed out in every profile:

| Target | E | Vampire 4x2500 | Vampire 2x5000 | Vampire SAT |
|---|---|---|---|---|
| length-2 band collapse | timeout | timeout | timeout | timeout |
| length-3 band collapse | timeout | timeout | timeout | timeout |
| length-2 band bridge | timeout | timeout | timeout | timeout |
| length-3 band bridge | timeout | timeout | timeout | timeout |
| two-position bridge | timeout | timeout | timeout | timeout |

This does not prove realizability of the band. It shows that direct unguided ATP remains broad even after encoding the complete length-2 and length-3 objects. Do not extend the same matrix to 5h50 without a new structural lemma or a materially guided encoding.

## Resource outcome

- maximum process-tree RSS: **7915.8 MiB**
- lowest observed MemAvailable: **7057.4 MiB**
- maximum swap used: **0 MiB**
- tree guard activations: **0**
- OOM or runner shutdowns: **0**

Worker-level Vampire memory messages occurred, but every final Vampire status was `SZS status Timeout`; these are reviewed timeouts, not machine OOM.

The exact per-slot record is in `run-29538663524-summary.csv`.
