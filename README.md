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

This is active research, not a finished proof or a counterexample.  The final
certificate is therefore still `0%`: no size-independent proof and no complete
finite Bad table has been obtained.

The current direct-proof route has completely resolved the periodic-reuse
subgate inside the CYCLE branch.  At the remaining terminal ZERO-root boundary,
two of three structural gates are proved:

- exact root equality produces an idempotent Latin E677 shadow on the Bad set;
- every canonical Bad `D`-cell routes to exactly `ZIPPER` or a marked
  Good-row `G-CROSS`;
- the global simultaneous `G-CROSS` network is still open.

Thus the scoped ZERO-reuse gate is `2/3 (67%)`, not an estimate that the whole
theorem is 67% solved.  The smallest symmetric pure-ZIPPER K5 shell is excluded
exactly at order 15, with a satisfiable control shell when E677 is disabled.
This is a bounded diagnostic, not a general proof.

Start with `docs/ACTIVE_FRONTIER_MIN.md`.  The exact ZERO-root argument and its
bounded computational boundary are in
`lemmas/e677_zero_root_reuse_shadow_quasigroup_boundary.md`; the reproducibility
audit is in `lemmas/e677_zero_root_reuse_computational_certificate.md`.

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

The current ZERO-root/ZIPPER checkpoint is reproduced locally, sequentially,
by:

```powershell
.\verify_zero_root_zipper.ps1
```

The optional longer order-10 recheck is:

```powershell
.\verify_zero_root_zipper.ps1 -IncludeOrder10
```

The wrapper verifies the satisfiable control shell and reruns the order-15
UNSAT result with both Glucose and CaDiCaL.  It requires Python 3 and
`python-sat==1.9.dev7`; see `tools/requirements-e677-sat.txt`.  Checks are run
one at a time, and no GitHub Actions job is needed.

The older size-8 checkpoint remains available:

```powershell
.\verify_size8_closed.ps1
```

On Windows, the `.cmd` launchers can be used if PowerShell blocks direct script
execution:

```text
verify_size8_closed.cmd
verify_zero_root_zipper.cmd
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
