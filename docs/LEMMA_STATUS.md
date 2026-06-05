# Lemma Status

Date: 2026-06-05.

This file separates proved or repeatedly verified structural facts from active
candidate lemmas.  The project is still active research and does not yet claim
a complete proof of `E677 -> E255` for all finite magmas.

## Main candidate

File:

```text
lemmas/main_bad_cycle_no_free_tail_lemma.md
```

Status:

```text
main candidate / not fully proved
```

Statement:

```text
In a finite E677 magma, a bad element 0 cannot have r_2=b_2*0 != 0.
Thus r_2=0, which is E255 for 0.
```

## Proved or stable structural ingredients

The following ingredients are treated as stable working facts in the current
research record:

```text
inverse edge chain
bad-cycle predecessor ladder
source-orbit ladder
source-row zero trap
edge-predecessor triangle expansion
```

Core files:

```text
lemmas/inverse_edge_chain.md
lemmas/source_orbit_ladder_lemma.md
lemmas/source_orbit_zipper_lemma.md
lemmas/edge_predecessor_triangle_lemma.md
```

## Bridge-orbit split

File:

```text
lemmas/offset_bridge_orbit_dichotomy_lemma.md
```

Status:

```text
structural progress / used by the current frontier
```

For `r_2=b_t`, set

```text
p = (b_3*b_4)*b_3.
```

If a bridge row exists with

```text
a*b_t=b_4
a*b_4=b_3
```

then

```text
b_3*a=p.
```

There is at most one bridge row.  This splits the proof attempt into a bridge
branch and a no-bridge orbit branch.

## No-bridge orbit frontier

Files:

```text
lemmas/no_bridge_orbit_tail_candidate.md
lemmas/offset_source_orbit_first_return_lemma.md
lemmas/first_return_row_pressure_lemma.md
lemmas/source_orbit_zipper_lemma.md
lemmas/edge_predecessor_triangle_lemma.md
```

Status:

```text
active structural proof target
```

The target is to show that a zero-avoiding orbit cannot keep creating a fresh
tail forever in a finite E677 magma.

## Pressure-diamond frontier

Files:

```text
lemmas/two_sided_offset_orbit_lemma.md
lemmas/r2_row_pressure_lemma.md
lemmas/offset_pressure_diamond_lemma.md
lemmas/double_interval_pressure_lemma.md
```

Status:

```text
current strongest frontier
```

This package turns the nonzero value `r_2=t` into a double interval pressure
configuration.  The next candidate lemma is that the two fresh predecessors
cannot both survive while row-`t` and row-`b_4` pressure is avoided.

## Closed computational regions

See:

```text
docs/CLOSED_CASES.md
```

Current public summary:

```text
sizes 5, 6, 7, 8: closed
size 8: reproducible script and recorded log included
size 9, cases 1-33: recorded closed
case45, branch 7*0=4: recorded closed
```

## Caveat

Files whose name contains `candidate`, `progress`, `plan`, or `audit` should be
read as working material unless this status file says otherwise.

