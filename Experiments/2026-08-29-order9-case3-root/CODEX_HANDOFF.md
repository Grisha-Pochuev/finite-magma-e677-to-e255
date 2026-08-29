# Codex handoff: order-9 three-Bad form 3 closed

Top form 3 is now completely excluded.

Fixed data:

```text
Bad={0,1,2};
D:0->1->2->0;
0*0=1; 1*0=3; 3*0=1.
```

Canonical strict extra roots are `(0,1)` and `(0,2)`.  For each root, the
product is exhaustively Good, row value `0`, or the third Bad point.  All six
aggregate outcomes are UNSAT in both CaDiCaL195 and Glucose42.

The two aggregate Good outcomes were independently refined by residual Good
relabelling to the four exact representatives with product `3` or new Good
`4`; all four are also UNSAT in both engines.

Exact record:

```text
smoke run: 33268344813
full run:  33268434711
base checker Git blob: efe356acd0047eef8ae5645b2cb04ac2a493632d
```

Consequently the order-nine no-HIT three-Bad count is now

```text
17/24 closed.
```

Remaining indices:

```text
11, 15, 16, 18, 21, 23, 24.
```

No SAT table was returned.  The full order-nine result remains open because
these seven forms, larger Bad cardinalities, and HIT remain.

For the next step, compare the seven remaining forms by the number of
canonical root pairs and Good-product representatives.  Prefer the smallest
exact orbit split rather than rerunning an unsplit top-form cube.
