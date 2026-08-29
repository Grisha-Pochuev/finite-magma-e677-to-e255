# ZERO-root reuse: reproducibility certificate

Date: 2026-08-29.

This file certifies a bounded diagnostic used in the E677 -> E255 research.
It is **not** a DRAT/LRAT proof, a proof of the full implication, or a finite
counterexample.  Its purpose is to make the exact order-10 and order-15 claims
independently rerunnable and to separate them from the size-free mathematics.

## Mathematical audit

The complete argument is in
`lemmas/e677_zero_root_reuse_shadow_quasigroup_boundary.md`.  The following
claims were rechecked from the displayed E677 consequences rather than inferred
from SAT output.

| Claim | Exact input | Audit result |
| --- | --- | --- |
| `s(x)=x*x` is Good for Bad `x` | off-diagonal Bad closure and `sigma(x)` Good | proved in equations (3)--(5) |
| every Bad row has one crossing in each direction | row permutation and equation (7) | proved in equations (8)--(10) |
| `N_B(u,v)=1` for distinct Bad `u,v` | root equality, tau indegree, row count | proved in equations (11)--(13) |
| the Bad shadow is an idempotent Latin E677 quasigroup | the previous multiplicity and a cell-by-cell E677 word audit | proved in equations (14)--(16) |
| every canonical Bad D-cell has two differently coloured carriers | the Latin multiplicity and canonical `sigma(q)` carrier | proved in (C1)--(C4) |
| the companion has exactly ZIPPER or G-CROSS form | companion identity and the unique Bad-row colour crossing | proved in (C5)--(C7) |

The auxiliary assumption `Good*Bad subset Good` appearing in an older source
lemma is not used.  The simultaneous global G-CROSS network remains open.

## Encoded order-15 claim

The checker fixes the K5 Bad shadow, an exact Bad D-cycle, the two Good layers,
the pure ZIPPER identities, terminal Bad/Good fixer constraints, no HIT, row
permutations, equivariance, and every E677 pair.  The control run disables only
the E677 pair selectors.

For every SAT model, the checker separately decodes the table and verifies all
permutation rows, fixed cells, terminal fixer conditions, no HIT, equivariance,
and the prescribed D-cycle.  For a full SAT model it would additionally check
every E677 pair and recompute the Bad set.

The sequential command is:

```powershell
.\verify_zero_root_zipper.ps1
```

Observed output on 2026-08-29:

```text
order 15 base shell / Glucose42: SAT VERIFIED, 0.134s
order 15 full E677 / Glucose42:  UNSAT, 0.809s
order 15 full E677 / CaDiCaL195: UNSAT, 1.621s
```

The satisfiable control distinguishes a genuine mixed-E677 contradiction from
an inconsistent fixed shell.  Agreement of two solver engines reduces the risk
of an engine-specific error; it is not a formal UNSAT proof certificate.

## Encoded order-10 claim

The optional longer check is:

```powershell
.\verify_zero_root_zipper.ps1 -IncludeOrder10
```

It fixes one K5 Bad shadow in order 10, makes the other five points terminal
Good, forbids HIT from the Bad layer, and enforces every row permutation and
every E677 pair.  Independent results are:

```text
Glucose42:  UNSAT, 191.684s
CaDiCaL195: UNSAT, 97.484s
```

The adjacent order-11 test and the order-20 four-layer test were UNKNOWN at
their recorded bounds.  UNKNOWN is used as evidence neither for SAT nor UNSAT,
and those runs must not be enlarged unchanged.

## Files and hashes

The verified environment used Python 3.12.13 and PySAT 1.9.dev7.  A clean
environment can install the pinned dependency from
`tools/requirements-e677-sat.txt`.

```text
tools/e677_k5_block_tree_completion_sat.py
  SHA256 52C25039720F9401244294339E4AB8F2E1517640E010E9B0C2C1DCAD8F7B4117
verify_zero_root_zipper.ps1
  SHA256 22BFCDFFFF6287E1ECEE4AB1DE9D75E7737ACCC90BF21C196EEBFD41771C53DF
verify_zero_root_zipper.cmd
  SHA256 A14BA69E31E7743185D0511BD8226FF75A50D8259F2467361C058090E969AE21
```

All certificate runs were local and sequential, with at most one SAT process
active.  No GitHub Actions job was started.
