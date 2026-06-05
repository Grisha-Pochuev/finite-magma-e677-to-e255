# Project Status

Date: 2026-06-05.

## Problem

The project studies finite magmas satisfying

```text
E677: x = y * (x * ((y * x) * y))
```

and asks whether this identity implies

```text
E255: x = ((x*x)*x)*x.
```

The project has not yet produced a complete proof.  It has produced a set of
closed finite regions, structural reductions, and a current proof frontier.

## Public status summary

```text
sizes 5, 6, 7, 8: closed
size 8: reproducible script and recorded log included
size 9, cases 1-33: recorded closed
case45, branch 7*0=4: recorded closed
current frontier: double interval pressure
```

See `docs/CLOSED_CASES.md` for the evidence table.

## Current proof strategy

The proof strategy is to assume a finite counterexample and study the local
structure around a bad element `0` for which `E255` fails.

The current notation is:

```text
b_j = L_0^{-j}(0)
r_j = b_j*0
```

The central target is to prove that `r_2` cannot be nonzero.

If `r_2=0`, then the bad element is no longer bad, because this is exactly the
`E255` condition for `0`.

## Current frontier

The latest active frontier is:

```text
lemmas/double_interval_pressure_lemma.md
```

It says that a nonzero `r_2=t` becomes a common pivot of two forced intervals:

```text
row b_2:
  u_2 -> 0 -> t

row b_3:
  c_{-1} -> t -> b_4
```

The next candidate lemma is that these intervals cannot both keep fresh
predecessors while avoiding the additional forced pressure in rows `t` and
`b_4`.

## How to read this repository

Recommended order:

1. `README.md`
2. `docs/CLOSED_CASES.md`
3. `docs/REPRODUCIBILITY.md`
4. `docs/LEMMA_STATUS.md`
5. `docs/CURRENT_FRONTIER.md`
6. `lemmas/double_interval_pressure_lemma.md`

The historical log is not the current status.  The current public state is the
combination of `docs/PROJECT_STATUS.md`, `docs/LEMMA_STATUS.md`, and
`docs/CURRENT_FRONTIER.md`.

