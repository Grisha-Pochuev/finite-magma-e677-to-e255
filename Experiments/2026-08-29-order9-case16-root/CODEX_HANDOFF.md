# Codex handoff — order-9 three-Bad form 16

Date: 2026-08-29.

## Exact target

The selected remaining normalized form is index `16`:

```text
Bad={0,2,3};
D: 0->2->3->0;
0*0=1;
1*0=2;
2*0=2.
```

Its canonical extra root is `(0,2)` or `(0,3)`.  For each root the exhaustive
product classes are Good, the row label `0`, and the third Bad label.  Thus the
first split has exactly six leaves.  In the two Good leaves residual Good-label
symmetry fixes the product to `4`, so the labelled Good refinement has exactly
two leaves.

## Reproduction

The unchanged checker is:

```text
tools/e677_order9_no_hit_bad_count_sat.py
Git blob: efe356acd0047eef8ae5645b2cb04ac2a493632d
```

The exact commands are recorded in `workflow-smoke.yml` and
`workflow-full.yml` in this folder.  Every SAT result from the checker is a
full `9 x 9` table and is independently verified against all 81 E677 pairs,
all permutation rows, the exact three-point Bad set, and no HIT.

## Status

Smoke and full-run results are pending.  Do not infer closure from a partial
assignment, an UNKNOWN leaf, or a technically green workflow.
