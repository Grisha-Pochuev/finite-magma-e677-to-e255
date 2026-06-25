# R-b5 Beta-Necklace Reduction Candidate

Date: 2026-06-19.

Status:

```text
candidate / R-b5 start-return necklace should fold into beta-layer reductions
```

## Purpose

This is the next candidate after:

```text
rb5_start_return_a_cycle_beta_pair_boundary.md
```

The remaining R-b5 start-return cycle carries, at every generated A-vertex, a
lifted beta-anchor pair:

```text
H_i    -> next A,
Beta_i -> b
```

in the target graph `H_{A_i}`.

The candidate is that a clean cyclic necklace of these pairs cannot be a new
residual, because each beta anchor is already governed by:

```text
beta_layer_reduction_lemma.md
clean_external_bridge_tenth_stage_reduction_lemma.md
```

## Local Necklace Cell

At one A-cycle vertex:

```text
b*A_i=A_{next},
x_i*A_i=b,
x_i*b=x_{i+1}.
```

The beta pressure gives:

```text
Beta_i=pred_{x_i}(A_i),
x_i*Beta_i=A_i.
```

The lifted pair in `H_{A_i}` is:

```text
H_i    -> A_{next},
Beta_i -> b.
```

This is exactly a beta-anchor row-b partner pair.

## Known Reduction Applied Cellwise

For each cell, the previous reductions say:

```text
Beta_i=H_i
  -> shared-edge divergence, folded into base row-b/generated bridge;

Beta_i=A_j
  -> same-input split lifted to a same-target pair;

Beta_i=x_j
  -> beta-X reversible square, beta-anchored;

Beta_i visible
  -> core attachment;

Beta_i fresh
  -> beta predecessor zipper, which eventually hits generated X-layer.
```

The fresh beta extension is no longer independent:

```text
fresh_beta_extension_eventual_x_hit_lemma.md
deep_beta_x_hit_reduction_lemma.md
```

route it to watched hits, row-`x_i` recurrence, beta first-hit routing, or a
beta-anchored square.

## Candidate Conclusion

Therefore a clean R-b5 beta necklace should reduce to:

```text
1. visible/core attachment;
2. same-target fan/path/full-interval collision;
3. base row-b/generated bridge already covered;
4. Z3 paired ladder already reduced to E11;
5. or a same-row recurrence already in the global recurrence inventory.
```

If this candidate is proved, the R-b5 start-return minimal A-cycle is not a
new obstruction.  It is another presentation of the already reduced beta/Z3
route.

## Missing Formal Step

The missing step is coverage:

```text
Show that applying beta_layer_reduction_lemma.md at every vertex of the
minimal A-cycle cannot leave a clean necklace whose first beta/X/Z hit only
returns to the same A-cycle without triggering the tenth-stage Z3 reduction or
a same-row recurrence already inventoried.
```

This is a finite first-hit argument around the A-cycle, not a new broad search.
