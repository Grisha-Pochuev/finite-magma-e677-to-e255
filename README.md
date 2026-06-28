# The Open Mathematics Project

## Finite magmas: E677 -> E255

This repository publishes an open research project about the finite-magma implication

```text
E677: x = y * (x * ((y * x) * y))
```

and whether it forces

```text
E255: x = ((x * x) * x) * x.
```

The current project focuses on one concrete problem: proving or refuting `E677 -> E255` for finite magmas. The broader long-term umbrella is **The Open Mathematics Project**: a public, reproducible workflow for attacking open mathematical problems with human mathematical direction, AI-assisted reasoning, and independently checkable computation.

## Current status

This is active research, not a finished proof.

Current recorded status:

- finite sizes `5`, `6`, `7`, and `8` are closed;
- size `8` has a reproducibility script and a recorded verification log;
- size `9` is the active finite-search zone;
- the working frontier has moved through the no-free-tail / double-interval pressure line into anchored, zipper, and period-3 residual reductions;
- many files are working notes, candidates, diagnostics, and proof-search records rather than final theorem statements.

For the most current internal context, start with the active status and navigation files. During the repository cleanup after a working snapshot upload, some current files may still be at the repository root until they are moved back into `docs/`, `lemmas/`, and `logs/`.

## Intended repository layout

```text
docs/          Human-readable project status, summaries, and navigation.
lemmas/        Working lemma files and candidate structural arguments.
tools/         Search and diagnostic scripts.
logs/          Historical research logs and verification outputs.
atp/           Automated theorem prover inputs and notes.
formal/lean/   Lean formalization notes and current formalization boundary.
archive/       Historical or superseded working snapshots.
```

The public root of the repository should stay small. Large collections of lemma, boundary, candidate, diagnostic, reduction, frontier, and inventory files belong in `lemmas/` or `docs/`, not at the top level.

## Reproducibility

The main reproducible computational checkpoint included here is the size-8 closure:

```powershell
.\verify_smoke.ps1
```

then:

```powershell
.\verify_size8_closed.ps1
```

On Windows, the `.cmd` launchers can be used if PowerShell blocks direct script execution:

```text
verify_smoke.cmd
verify_size8_closed.cmd
```

The repository also includes recorded verification output and research logs when available. Reproducibility details should be kept in `docs/REPRODUCIBILITY.md` and `logs/`.

## Lean status

Lean formalization is planned but not yet the source of truth for this repository. The present results are recorded as mathematical notes plus targeted model-search scripts and logs.

## Research style

The project is deliberately not a blind brute-force search. The working rule is:

1. derive algebraic consequences of `E677`;
2. isolate structural obstructions to finite counterexamples;
3. use computation only for bounded, interpretable checks;
4. translate computational closures back into human-readable lemmas.

## License

The repository is intended to be published under the MIT License. This applies to the code, notes, and reproducibility material unless a future file states otherwise.

## Contributing and citation

See:

- `CONTRIBUTING.md`
- `CITATION.cff`
