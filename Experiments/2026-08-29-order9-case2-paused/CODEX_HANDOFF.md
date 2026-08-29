# Codex handoff: order-9 three-Bad form 2 closed

The exact paused residue from
`lemmas/e677_order9_three_bad_root_and_case2_reduction.md` is now completely
excluded.

Fixed context:

```text
Bad={0,1,2}; D:0->1->2->0;
0*0=1; 1*0=2; 2*0=1;
selected extra root=(0,2); 0*2=3 Good.
```

Put `a=0*3`, `k=a*0`; E677 gives `3*k=2`.  The exhaustive residual leaves
were

```text
(a,k)=(0,1),(2,1),(4,1),(4,3),(4,4),(4,5).
```

All six are UNSAT in both CaDiCaL195 and Glucose42.  The sole difficult leaf
`(a,k)=(0,1)` was independently closed in about 3.5 seconds and about 63,000
conflicts in each engine.  No SAT model or partial counterexample exists in
this experiment.

Exact record:

```text
smoke run: 33267460851
full run:  33267614227
base checker Git blob: efe356acd0047eef8ae5645b2cb04ac2a493632d
```

Therefore top form 2 is fully excluded, and the three-Bad top-form count is
now

```text
16/24 closed.
```

The unresolved indices are

```text
3, 11, 15, 16, 18, 21, 23, 24.
```

The most natural finite continuation is form 3: it has the same three-cycle
D-pattern as form 2 and differs only in the first-column chain
`1*0=3, 3*0=1`.  Reuse the canonical-root and companion-word mechanism, but
do not rerun the old unsplit top-form cube unchanged.

This result does not address larger Bad cardinalities or HIT.
