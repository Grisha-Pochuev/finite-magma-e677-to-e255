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

This is active research.  There is currently neither a proof of the finite
implication nor a complete finite counterexample.

To state the present reduction, define

```text
sigma(x) = (x*x)*x,
D(x)     = sigma(x)*x.
```

Call `x` **Good** if `D(x)=x`, and **Bad** otherwise.  Proving E255 is exactly
the same as proving that there are no Bad elements.  Starting from a Bad
element and repeatedly applying `D` has only two possible behaviours in a
finite magma: it eventually reaches a Good element, or it remains Bad and
eventually enters a cycle.

The current size-independent argument proves the following.

1. A completely closed periodic configuration cannot keep reusing all of its
   predecessor cells internally: it must produce a boundary cell outside the
   periodic part.
2. In the remaining equality case, the Bad set `B` carries an auxiliary
   operation

   ```text
   r o u = r*u  if r != u,
   r o r = r,
   ```

   and `(B,o)` is proved to be an idempotent Latin quasigroup satisfying E677.
   This auxiliary operation is called the **Bad shadow** in the working notes;
   it is not asserted to be a submagma of the original magma.
3. For each Bad `q`, put

   ```text
   e = D(q),  t = sigma(q),  h = e\q,  z = t*e,
   ```

   where `a\b` denotes the unique input sent to `b` by the row of `a`.  The
   companion equations force exactly one of two explicit alternatives:

   ```text
   z=h and t=h\h;                 or
   z is Good and z*t=h is Bad.
   ```

The unresolved step is global: prove that all cells of the second kind, taken
together, force a shorter Bad orbit or a Good element, or else use them to
construct a complete counterexample.  The local counting argument alone is not
enough.

The smallest symmetric completion test for the first alternative is UNSAT at
order 15 in two independent SAT engines.  The identical partial shell is SAT
when E677 is disabled, so the contradiction genuinely uses the mixed E677
equations.  This is a bounded computational result, not a general theorem.

There is also a separate finite-order checkpoint.  Orders `5` through `8`
are recorded as closed; order `9` is not yet closed.  For order `9`, the
no-HIT branch has the following reproducible reductions:

- terminal root equality is excluded;
- exactly two Bad elements are excluded;
- exactly three Bad elements reduce to 24 normalized forms, 15 of which are
  already UNSAT in the first exact scan;
- in normalized three-Bad form 2, eight of nine canonical root leaves are
  independently UNSAT, leaving one explicitly stated companion case.

The last statement and its exact restart point are in the
[order-9 three-Bad reduction](lemmas/e677_order9_three_bad_root_and_case2_reduction.md).
These are finite reductions only: the HIT branch and the remaining no-HIT
forms still prevent a complete order-9 certificate.

Progress numbers are deliberately scoped:

```text
complete proof or checked counterexample:              no (0%)
periodic-reuse subproblem:                         1/1 (100%)
terminal Bad-set structural reduction:              2/3 (67%)
global crossing-network outcomes proved:              0/3 (0%)
```

The `67%` figure refers only to this last three-part reduction.  It is not an
estimate that the original open problem is 67% solved.

## Terminology used in the working notes

Several capitalized words in the research files are short search labels, not
standard mathematical terminology and not claims that new kinds of objects
have been discovered.  They can always be replaced by the stated equations or
orbit behaviour.

| Working label | Meaning |
| --- | --- |
| `HIT` | a Bad `D`-orbit reaches a Good element |
| `CYCLE` | a `D`-orbit remains Bad and enters a cycle |
| `ZERO root` | a state with no predecessor in a particular transport graph; it is not a zero element of the magma |
| `SHORT` | a Bad segment of length one in a multiplication row |
| `ZIPPER` | the first displayed alternative: `t*e=h` and `t=h\h` |
| `G-CROSS` | the second alternative: a Good row and Good input produce the Bad value `h` |
| `K5 shell` | a symmetric five-Bad-point partial multiplication pattern used in a bounded completion test |

For a first mathematical audit, read the
[ZERO-root reduction](lemmas/e677_zero_root_reuse_shadow_quasigroup_boundary.md),
then its [computational certificate](lemmas/e677_zero_root_reuse_computational_certificate.md).
The [active frontier](docs/ACTIVE_FRONTIER_MIN.md) is a dense continuation
record for contributors, not the recommended introduction for a new reader.

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

The current order-9 finite checkpoints are reproduced, one process at a time,
by:

```powershell
.\verify_order9_terminal_zero.ps1
.\verify_order9_two_bad_no_hit.ps1
.\verify_order9_three_bad_case2.ps1
```

The third command is the short newest certificate: it checks the same eight
three-Bad leaves independently with CaDiCaL195 and Glucose42.

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

## Follow the project

Research updates and discussion are published on the
[project author's Telegram channel](https://t.me/let_people_dance).
