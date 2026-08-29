# Results: order-9 three-Bad top form 3

Status: complete; normalized top form 3 is independently UNSAT.

## Fixed form

```text
Bad={0,1,2};
D:0->1->2->0;
0*0=1; 1*0=3; 3*0=1.
```

## Six exhaustive root outcomes

The canonical root pairs are `(0,1)` and `(0,2)`.  For each pair, the strict
root product is exhaustively Good, the row value `0`, or the third Bad point:

```text
root=(0,1): product Good / row 0 / third Bad 2;
root=(0,2): product Good / row 0 / third Bad 1.
```

## Smoke run

```text
run id:   33268344813
head SHA: a308a3fce1d067166d5dc815d8566cc4bc29201a
CaDiCaL artifact SHA256: 224acaeba1ffe47019ac02f970abdc31a947cef3eedf6b2c0d497c60ecc56bc8
Glucose artifact SHA256: 84ef5a2d3f0a9b57c3bad1a546c47b058111be8025583452fddcad62b9481cb6
technical result: PASS
```

At the short boundary:

```text
CaDiCaL195: 2 UNSAT, 4 UNKNOWN, 0 SAT;
Glucose42:  4 UNSAT, 2 UNKNOWN, 0 SAT.
```

Both engines left only Good-product outcomes in common.  The additional two
CaDiCaL UNKNOWN leaves were merely the smaller 5,000-conflict boundary.

## Full exact run

```text
run id:   33268434711
head SHA: ffe689639271d827ed67b9407bedafbda4f3ff0d
base checker Git blob: efe356acd0047eef8ae5645b2cb04ac2a493632d
formula: 3151 variables, 55911 clauses
technical failures: 0
verified counterexamples: 0
```

The six exhaustive root outcomes were all UNSAT in both engines:

```text
CaDiCaL195: 6/6 UNSAT, 0 UNKNOWN, 0 SAT;
Glucose42:  6/6 UNSAT, 0 UNKNOWN, 0 SAT.
```

Artifact digests:

```text
root outcomes / CaDiCaL195:
5b57d7ff3f87614b588531d97b8106956ddb227a9e6f5f84dda41697d856916b

root outcomes / Glucose42:
dd6de793f04908921f1480b5fe199e24b31cb9b4a141302efe88c12855ae7cbd
```

The two nontrivial aggregate Good outcomes were:

```text
root=(0,1), product Good:
  CaDiCaL195 UNSAT in 24.654s with 385,240 conflicts;
  Glucose42  UNSAT in 28.652s with 368,640 conflicts.

root=(0,2), product Good:
  CaDiCaL195 UNSAT in 15.930s with 173,409 conflicts;
  Glucose42  UNSAT in 18.221s with 162,049 conflicts.
```

For an independent finer check, residual Good relabelling splits the two Good
outcomes into exactly four representatives:

```text
root=(0,1), product Good 3 or new Good 4;
root=(0,2), product Good 3 or new Good 4.
```

All four were also UNSAT in both engines:

```text
CaDiCaL195: 4/4 UNSAT;
Glucose42:  4/4 UNSAT.
```

Artifact digests:

```text
Good representatives / CaDiCaL195:
b4569d7962911315dcf0c466f6f96faabca6a82e424d42500fa94b34f71574f2

Good representatives / Glucose42:
bf33d2872da5ce941c1242ab284df88692c51395846583d8952295ebf2d3e73b
```

## Mathematical conclusion

Every order-nine no-HIT E677 model with exactly three Bad points and
normalized top form 3 must realize one of the six canonical root outcomes.
All six are UNSAT.  Therefore

```text
normalized three-Bad top form 3 is impossible.
```

The exact three-Bad count consequently improves from

```text
16/24 closed
```

to

```text
17/24 closed.
```

The unresolved indices are now

```text
11, 15, 16, 18, 21, 23, 24.
```

No partial table, SAT skeleton, or learned clause has been treated as a
counterexample.  No SAT model was returned.  This result does not address the
seven remaining three-Bad forms, larger Bad cardinalities, HIT, or the full
order-nine implication.
