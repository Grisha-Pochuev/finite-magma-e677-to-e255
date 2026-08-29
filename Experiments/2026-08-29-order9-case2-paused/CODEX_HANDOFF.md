# Codex handoff: order-9 three-Bad form 2

The exact paused residue from
`lemmas/e677_order9_three_bad_root_and_case2_reduction.md` has been isolated
as six SAT leaves.

Fixed context:

```text
Bad={0,1,2}; D:0->1->2->0;
0*0=1; 1*0=2; 2*0=1;
selected extra root=(0,2); 0*2=3 Good.
```

Put `a=0*3`, `k=a*0`; E677 gives `3*k=2`.  The exhaustive residual leaves
are

```text
(a,k)=(0,1),(2,1),(4,1),(4,3),(4,4),(4,5).
```

`run_case2_paused.py` pins the audited base checker by Git blob and adds only
these assumptions in memory.  Any SAT model is still decoded and checked by
the base verifier against all 81 E677 substitutions, exact colours, exact
D-map, and no HIT.

After the run, use the per-leaf conflict/time profile to choose the next move:

- `6/6 UNSAT` in both engines closes top form 2 completely;
- a small common UNKNOWN set is the next exact structural target;
- a verified SAT table is a full order-nine no-HIT counterexample and must be
  audited independently before any broader claim.

This experiment does not address the other unresolved top forms, larger Bad
cardinalities, or HIT.
