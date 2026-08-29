# Order-9 three-Bad top form 3: canonical root split

Date: 2026-08-29.

## Exact form

Top form 3 is the closest unresolved successor of the now closed form 2:

```text
Bad={0,1,2};
D: 0->1->2->0;
0*0=1;
1*0=3;
3*0=1.
```

The D-map is the same directed three-cycle as in form 2.  The only change in
the normalized first-column data is the longer chain `1->3->1`.

After selecting an extra non-diagonal Omega-root before naming labels, the
canonical root pairs are exactly

```text
(0,1), (0,2).
```

For each pair `(0,h)`, a strict root product is exhaustively one of

```text
Good;
row value 0;
the third Bad point.
```

Thus the first exact split has six leaves.  This is the same certified
canonical-root mechanism used for form 2; it is not a rerun of the old
unsplit top-form cube.

## Checker

The run uses the unchanged audited checker

```text
tools/e677_order9_no_hit_bad_count_sat.py
```

at Git blob

```text
efe356acd0047eef8ae5645b2cb04ac2a493632d.
```

Every SAT answer must decode to a complete 9x9 table and pass the independent
checks of all nine permutation rows, all 81 E677 substitutions, the exact
three-point Bad set, the exact D-map, and no HIT.  A partial assignment or SAT
skeleton is never called a counterexample.

## First command

```text
python tools/e677_order9_no_hit_bad_count_sat.py \
  --min-bad 3 --max-bad 3 \
  --scan-bad3-structural --bad3-frontier-only --bad3-case 3 \
  --bad3-canonical-root-outcomes \
  --solver <cadical195|glucose42> \
  <bounded resource option>
```

The short two-engine gate decides whether to proceed to named Good-product
representatives or to a smaller surviving outcome set.
