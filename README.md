# The Open Mathematics Project

## Popular introduction

This repository is about a stubborn problem in abstract algebra.

The object studied here is called a **magma**. A magma is one of the most minimal algebraic structures: just a set of symbols and one operation, written as `*`. This operation is not ordinary multiplication. The symbols are not numbers. There is no built-in addition, order, distance, geometry, or hidden meaning. We only know that if we combine two symbols, the operation gives us a third symbol.

This makes the problem very abstract. We are not asking what happens with familiar numbers. We are asking what must follow from one formal rule if that rule is imposed on every possible finite operation table.

The concrete question is whether the law

```text
E677: x = y * (x * ((y * x) * y))
```

forces the law

```text
E255: x = ((x * x) * x) * x
```

in every finite magma.

This is not just an isolated puzzle. In the [final report of the Equational Theories Project](https://terrytao.wordpress.com/2025/12/09/the-equational-theories-project-advancing-collaborative-mathematical-research-at-scale/), Terence Tao reported that, among 22,028,942 finite-magma implications considered by the project, E677 -> E255 and its dual were the only unresolved pair. The project had been unable to settle them even after months of effort. This places the question on a genuine collaborative research frontier rather than in a toy corner of algebra.

This repository is my open attempt to push this specific finite problem further. It records computational checks, proof logs, reduced cases, failed paths, and candidate structural lemmas. The current work has closed several small finite sizes, narrowed the active frontier, and shifted the search from blind brute force toward a more structured proof mechanism. The precise verified claims are listed in the status sections below.

This repository is also part of my broader initiative, **The Open Mathematics Project**. I want to use it as a working model for open mathematical research: a place where not only final theorems are published, but also logs, checks, failed attempts, reduced cases, continuation points, and candidate lemmas. If this finite-magma problem can be brought to a complete solution, my goal is to continue with other difficult problems closer to the mathematical research frontier, using the same open and reproducible workflow.

The guiding idea is simple: AI may be useful in mathematics not because it magically replaces mathematicians, but because it can patiently handle a lot of technical "dirty work" -- checking many small branches, keeping long context, comparing repeated patterns, and turning computational dead ends into possible lemmas.

This repository is therefore a small open laboratory around one stubborn finite-magma problem.

## Technical overview and repository guide

### Finite magmas: E677 -> E255

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

### Current status

This is active research, not a finished proof.

Current recorded status:

- finite sizes `5`, `6`, `7`, and `8` are closed;
- size `8` has a reproducibility script and a recorded verification log;
- in size `9`, cases `1-33` are recorded as closed;
- in `case45`, the branch `7*0=4` is recorded as fully closed;
- the normalized size-9 role `u=b_3` is now recorded as closed;
- the latest general progress proves recursive common-edge fan, bridge, and
  zipper mechanisms;
- the active frontier is the three-source pressure problem described in
  `docs/CURRENT_FRONTIER.md`.

See:

- `docs/CLOSED_CASES.md` for the compact status table;
- `docs/LEMMA_STATUS.md` for the current lemma map;
- `docs/RESULTS_INDEX.md` for navigation through the research files;
- `docs/CURRENT_FRONTIER.md` for where the next proof attempt starts.
- `docs/METHOD.md` for the research method.
- `docs/RESEARCH_UPDATE_2026-06-08.md` for the latest research update.

### What is in this repository

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

### Reproducibility

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

### Lean status

Lean formalization is planned but not yet the source of truth for this
repository.  The present results are recorded as mathematical notes plus
targeted model-search scripts and logs.

See `formal/lean/README.md` for what should be formalized first.

### Research style

The project is deliberately not a blind brute-force search.  The working rule
is:

1. derive algebraic consequences of `E677`;
2. isolate structural obstructions to finite counterexamples;
3. use computation only for bounded, interpretable checks;
4. translate computational closures back into human-readable lemmas.

### License

The repository is published under the MIT License.  This applies to the code,
notes, and reproducibility material unless a future file states otherwise.

### Contributing and citation

See:

- `CONTRIBUTING.md`
- `CITATION.cff`
