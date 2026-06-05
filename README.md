# The Open Mathematics Project

## Finite magmas: E677 -> E255

This repository publishes an open research project about the finite-magma
implication

```text
E677: x = y * (x * ((y * x) * y))
```

and whether it forces

```text
E255: x = ((x * x) * x) * x.
```

The current project focuses on one concrete problem: proving or refuting
`E677 -> E255` for finite magmas.  The broader long-term umbrella is **The
Open Mathematics Project**: a public, reproducible workflow for attacking
open mathematical problems with human mathematical direction, AI-assisted
reasoning, and independently checkable computation.

## Current status

This is active research, not a finished proof.

Current recorded status:

- finite sizes `5`, `6`, `7`, and `8` are closed;
- size `8` has a reproducibility script and a recorded verification log;
- in size `9`, cases `1-33` are recorded as closed;
- in `case45`, the branch `7*0=4` is recorded as fully closed;
- the active mathematical frontier is the no-free-tail / double-interval
  pressure mechanism described in `docs/CURRENT_FRONTIER.md`.

See:

- `docs/CLOSED_CASES.md` for the compact status table;
- `docs/LEMMA_STATUS.md` for the current lemma map;
- `docs/RESULTS_INDEX.md` for navigation through the research files;
- `docs/CURRENT_FRONTIER.md` for where the next proof attempt starts.
- `docs/METHOD.md` for the research method.

## What is in this repository

```text
docs/          Human-readable project status, summaries, and navigation.
lemmas/        Working lemma files and candidate structural arguments.
tools/         JavaScript search and diagnostic scripts.
logs/          Historical research logs and verification outputs.
formal/lean/   Lean formalization notes and current formalization boundary.
```

`logs/research_log.md` is only a public English placeholder for the longer
internal historical log.  It should not be read as the current status.  Start
with `docs/CURRENT_FRONTIER.md` and `docs/LEMMA_STATUS.md`.

## Reproducibility

The main reproducible computational checkpoint included here is the size-8
closure:

```powershell
.\verify_smoke.ps1
```

then:

```powershell
.\verify_size8_closed.ps1
```

On Windows, the `.cmd` launchers can be used if PowerShell blocks direct script
execution:

```text
verify_smoke.cmd
verify_size8_closed.cmd
```

On a normal machine with Node.js installed, this script reruns the structural
split used for the size-8 result and writes
`logs/size8_rerun_<timestamp>.txt`.

The repository also includes the recorded verification output:

```text
logs/size8_verified_split_log.txt
```

More details are in `docs/REPRODUCIBILITY.md`.

## Lean status

Lean formalization is planned but not yet the source of truth for this
repository.  The present results are recorded as mathematical notes plus
targeted model-search scripts and logs.

See `formal/lean/README.md` for what should be formalized first.

## Research style

The project is deliberately not a blind brute-force search.  The working rule
is:

1. derive algebraic consequences of `E677`;
2. isolate structural obstructions to finite counterexamples;
3. use computation only for bounded, interpretable checks;
4. translate computational closures back into human-readable lemmas.

## License

The repository is published under the MIT License.  This applies to the code,
notes, and reproducibility material unless a future file states otherwise.

## Contributing and citation

See:

- `CONTRIBUTING.md`
- `CITATION.cff`
