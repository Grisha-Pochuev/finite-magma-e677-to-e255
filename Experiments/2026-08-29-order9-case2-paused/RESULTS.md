# Results: order-9 three-Bad form-2 paused continuation

Status: smoke gate passed; five leaves closed; one leaf sent to the full bounded check.

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

Both independent engines returned the same exact split:

```text
CaDiCaL195: 5 UNSAT, 1 UNKNOWN, 0 SAT;
Glucose42:  5 UNSAT, 1 UNKNOWN, 0 SAT.
```

The five independently excluded leaves are

```text
(a,k)=(2,1),(4,1),(4,3),(4,4),(4,5).
```

The sole shared bounded residue is

```text
(a,k)=(0,1),
so 0*3=0 and 3*1=2.
```

CaDiCaL reached its smoke boundary at `1,001` conflicts.  Glucose reached its
two-second boundary after `45,405` conflicts.  UNSAT is exact even in a smoke
run; UNKNOWN only says the resource boundary was reached.

## Full bounded run

```text
run id:   pending
head SHA: pending
CaDiCaL195: pending
Glucose42:  pending
```

The full run keeps the same six-leaf wrapper but gives the common residue a
much larger boundary.  Since the other five leaves are already exact UNSAT,
they are retained as consistency checks rather than new search targets.

## Mathematical interpretation

The paused continuation has been reduced from six leaves to one exact leaf:

```text
Bad={0,1,2}; D:0->1->2->0;
0*0=1; 1*0=2; 2*0=1;
0*2=3 Good; 0*3=0; 3*1=2.
```

This is a strict reduction of top form 2.  It is not a counterexample, does
not yet close top form 2, and does not address the other eight unresolved
three-Bad forms, larger Bad cardinalities, or HIT.
