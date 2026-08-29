# Results: order-9 three-Bad form-2 paused continuation

Status: complete; all six paused leaves are independently UNSAT.

## Source state

```text
base main commit:  b8deaabab7b6aeda15022fc78ca9f257fb913020
working branch:    web/order9-case2-paused-2026-08-29
base checker blob: efe356acd0047eef8ae5645b2cb04ac2a493632d
```

## Exact six leaves

```text
root=(0,2), 0*2=3 Good,
a=0*3, k=a*0, 3*k=2,
(a,k)=(0,1),(2,1),(4,1),(4,3),(4,4),(4,5).
```

## Smoke run

```text
run id:   33267460851
head SHA: d64d23711bc7c6797caf37668ecdcf4fedd2e72b
artifact: order9-case2-paused-smoke
artifact SHA256: 540bcab76066e6fb0990d4ee62c4f3fc7950ff1ad6f8e9c1433741ac6bb23a5f
technical result: PASS
```

Both engines returned the same preliminary split:

```text
CaDiCaL195: 5 UNSAT, 1 UNKNOWN, 0 SAT;
Glucose42:  5 UNSAT, 1 UNKNOWN, 0 SAT.
```

The sole smoke residue was `(a,k)=(0,1)`, equivalently
`0*3=0, 3*1=2`.  This was only a resource-bounded UNKNOWN.

## Full exact run

```text
run id:   33267614227
head SHA: fa1d990ff1e499e279bd32cb4fe953854dc837d5
summary artifact: order9-case2-paused-full-summary
summary SHA256:   87abc29dd16faf80bfb435c92938c10e1b4e7881b8fbe933fb9a64695db952e5
CaDiCaL artifact SHA256: 9276a1ec60a40be07b4a9314508b70728dbd8226c5a54fb0ab9eda288134078b
Glucose artifact SHA256: 736e1d0ee73802ad0b78b208a7ed101ce4c0882280347a612c19113b70c0d205
technical failures: 0
missing summaries: 0
verified counterexamples: 0
```

The two independent engines agree:

```text
CaDiCaL195: 6/6 UNSAT, 0 UNKNOWN, 0 SAT;
Glucose42:  6/6 UNSAT, 0 UNKNOWN, 0 SAT.
```

The only nontrivial leaf was the smoke residue:

```text
(a,k)=(0,1):
CaDiCaL195 UNSAT in 3.501s with 63,138 conflicts;
Glucose42  UNSAT in 3.391s with 62,888 conflicts.
```

The other five leaves were already forced inconsistent by the clauses learned
while resolving the first leaf and were confirmed UNSAT under their own exact
assumptions.  Learned clauses are consequences of the shared base formula;
the same pattern occurred independently in both engines.

## Mathematical conclusion

The preceding lemma had reduced top form 2 to these six exhaustive leaves.
Since all six are UNSAT, top form 2 itself is now completely excluded:

```text
no order-nine no-HIT E677 magma with exactly three Bad points
can realize normalized top form 2.
```

Consequently the initial three-Bad classification improves from

```text
15/24 top forms closed
```

to

```text
16/24 top forms closed.
```

The remaining top-form indices are

```text
3, 11, 15, 16, 18, 21, 23, 24.
```

This is a strict finite order-nine result.  It does not close those eight
forms, larger Bad cardinalities, HIT, or the full order-nine implication.
No partial table or SAT core has been treated as a counterexample; no SAT
model was returned.
