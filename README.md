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

The current project focuses on one concrete problem: proving or refuting
`E677 -> E255` for finite magmas. The broader long-term umbrella is **The
Open Mathematics Project**: a public, reproducible workflow for attacking open
mathematical problems with human mathematical direction, AI-assisted reasoning,
and independently checkable computation.

## Background

This problem is connected to the **Equational Theories Project** (ETP), a large
collaborative effort to classify implications between simple equational laws of
magmas. The ETP paper reports the completion of the implication graph between
4,694 simple magma laws, covering 22,028,942 implication edges, using a mixture
of human-generated arguments, automated methods, and Lean validation.

Fields Medalist Terence Tao was one of the central public figures of the
Equational Theories Project and kept a personal project log while working on
it. In that log, he wrote:

> "The notoriously stubborn 677=>255 implication for finite magmas remains unresolved."

The finite implication `E677 -> E255` was therefore one of the especially
difficult remaining finite-magma questions in the project. This repository is
an independent open research attempt focused on that single remaining crack:
either prove that every finite `E677` magma satisfies `E255`, or find a finite
counterexample.

References:

- Equational Theories Project paper: https://arxiv.org/abs/2512.07087
- Terence Tao's ETP blog post: https://terrytao.wordpress.com/2025/12/09/the-equational-theories-project-advancing-collaborative-mathematical-research-at-scale/
- Terence Tao's personal ETP log: https://github.com/teorth/equational_theories/wiki/Terence-Tao%27s-personal-log
- ETP repository: https://github.com/teorth/equational_theories

## Current status

This is active research, not a finished proof.

Recorded progress in this repository:

- finite sizes `5`, `6`, `7`, and `8` are recorded as closed;
- size `8` has a reproducibility script and a recorded verification log;
- size `9` is the active finite-search and proof-extraction zone;
- earlier work recorded progress through `case45`, including the branch
  `7*0=4` as fully closed;
- the proof search has moved beyond the older no-free-tail / double-interval
  pressure frontier into anchored, zipper, V3-admissibility, and period-3
  residual reductions;
- the latest internal frontier is concentrated around a period-3 zipper / named
  fan residual, rather than a broad blind search.

In plain language: the project has not solved the full problem yet, but it has
reduced the search to much more structured residual configurations. The current
work is trying to turn those residual configurations into a general proof, or
else expose the shape of a possible finite counterexample.

For the most current internal context, start with the active status and
navigation files. During the repository cleanup after a working snapshot upload,
some current files may still temporarily sit at the repository root until they
are moved back into `docs/`, `lemmas/`, and `logs/`.

See:

- `docs/NEXT_ACTION.md` for the next working step;
- `docs/CURRENT_FRONTIER.md` for the active frontier;
- `docs/LEMMA_STATUS.md` for the lemma map;
- `docs/RESULTS_INDEX.md` for navigation through the research files;
- `docs/REPOSITORY_CLEANUP_PLAN.md` for the current repository cleanup plan.

## What is in this repository

```text
docs/          Human-readable project status, summaries, and navigation.
lemmas/        Working lemma files and candidate structural arguments.
tools/         Search and diagnostic scripts.
logs/          Historical research logs and verification outputs.
atp/           Automated theorem prover inputs and notes.
formal/lean/   Lean formalization notes and current formalization boundary.
archive/       Historical or superseded working snapshots.
```

The public root of the repository is intended to stay small. Large collections
of lemma, boundary, candidate, diagnostic, reduction, frontier, and inventory
files belong in `lemmas/` or `docs/`, not at the top level.

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

On a normal machine with Node.js installed, the verification script reruns the
structural split used for the size-8 result and writes a timestamped log under
`logs/`.

More details should be kept in `docs/REPRODUCIBILITY.md` and `logs/`.

## Lean status

Lean formalization is planned but not yet the source of truth for this
repository. The present results are recorded as mathematical notes plus
targeted model-search scripts, automated-prover inputs, and logs.

A good future formalization target is not the whole research tree at once, but a
small verified spine: the exact formulation of `E677`, `E255`, the finite-magma
setting, and the first local structural lemmas that are stable enough to be
formalized.

## Research style

The project is deliberately not a blind brute-force search. The working rule is:

1. derive algebraic consequences of `E677`;
2. isolate structural obstructions to finite counterexamples;
3. use computation only for bounded, interpretable checks;
4. translate computational closures back into human-readable lemmas;
5. keep a reproducible trail so that future readers can distinguish proved
   reductions, bounded computations, diagnostics, and candidate ideas.

## Acknowledgements

This repository builds on the public mathematical context created by the
Equational Theories Project and its contributors. It is especially motivated by
the finite `E677 -> E255` question discussed in that project.

The repository itself is maintained by Grisha Pochuev as an open research log
and reproducible proof-search project.

## License

The repository is published under the MIT License. This applies to the code,
notes, and reproducibility material unless a future file states otherwise.

## Contributing and citation

See:

- `CONTRIBUTING.md`
- `CITATION.cff`
