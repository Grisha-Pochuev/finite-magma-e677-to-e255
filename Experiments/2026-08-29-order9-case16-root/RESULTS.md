# Results: order-9 three-Bad top form 16

Status: **top form 16 is exactly excluded**.

This closes one normalized no-HIT three-Bad form only.  It does not close all
of order 9 and does not prove the size-independent implication.

## Fixed form

```text
Bad={0,2,3};
1 is Good;
D: 0->2->3->0;
0*0=1; 1*0=2; 2*0=2.
```

## Exact exhaustive leaves

```text
canonical roots: (0,2), (0,3);
products per root: Good / row 0 / third Bad;
Good representatives: 0*2=4 and 0*3=4.
```

The six aggregate leaves are exhaustive.  Each aggregate Good leaf has one
representative because the unnamed Good labels are still freely relabelled.

## Runs

```text
smoke run: 33269622554
smoke head: 013a99437f1c4d5877a7236f9be96e3e6311c4c6

full run:  33269852847
full head: 5b0e8765b40fac638d1e09ba15908a9e01f3b347
```

Both runs used the unchanged checker at Git blob

```text
efe356acd0047eef8ae5645b2cb04ac2a493632d.
```

## Full-run results

| Split | Solver | Result | Time in leaves | Conflicts |
| --- | --- | --- | ---: | ---: |
| six canonical root outcomes | Glucose42 | `6/6 UNSAT` | 59.265 s | 695,660 |
| six canonical root outcomes | CaDiCaL195 | `5/6 UNSAT`, one aggregate Good UNKNOWN | 54.165 s | 707,198 |
| two exact Good representatives | Glucose42 | `2/2 UNSAT` | 10.179 s | 177,651 |
| two exact Good representatives | CaDiCaL195 | `2/2 UNSAT` | 17.161 s | 261,332 |

The sole aggregate UNKNOWN was

```text
root=(0,2), product=Good.
```

Residual Good relabelling turns this whole aggregate leaf into the single
exact representative

```text
0*2=4.
```

That representative is UNSAT in both engines.  The other aggregate Good leaf,
`root=(0,3), product=Good`, is already directly UNSAT in both engines and its
representative `0*3=4` is also `2/2`-certificate input.

Therefore every one of the six canonical root outcomes is excluded.  Form 16
is UNSAT.

## Semantic audit

The checker encodes:

- all nine rows as permutations;
- all 81 instances of E677;
- exact Good/Bad colour through absence or presence of a left fixer;
- exact `D` values;
- exact Bad cardinality three;
- `D(Bad) subset Bad` (no HIT);
- the exact normalized form and root assumptions.

Any SAT answer would be decoded as a full `9 x 9` table and rechecked against
all those conditions.  No SAT answer occurred.  In particular, there is no
partial table being presented as a counterexample.

## Consequence

The order-nine three-Bad count improves from

```text
17/24 closed
```

to

```text
18/24 closed.
```

The remaining normalized three-Bad forms are

```text
11, 15, 18, 21, 23, 24.
```

Order 9 remains open because these six forms, the no-HIT cases with more Bad
points, and the HIT branch have not all been excluded.
