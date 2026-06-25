# Clean External-Bridge Third-Stage Reduction Lemma

Date: 2026-06-18.

Status:

```text
proved reduction / removes fresh beta extension as independent residual
```

## Purpose

This updates the second-stage residual list after the fresh beta zipper work:

```text
beta_fresh_predecessor_zipper_ladder_lemma.md
beta_zipper_shifted_repeat_split_lemma.md
fresh_beta_extension_eventual_x_hit_lemma.md
deep_beta_x_hit_reduction_lemma.md
```

The main conclusion is:

```text
fresh beta-layer extension is not an independent residual.
```

It either creates a shifted same-input split or returns to the generated
X-layer and then routes through the existing beta-X/reversible-square
machinery.

## Fresh Beta Extension Split

Start with:

```text
Z_i^{-2}=x_{i+1},
Z_i^{-1}=b,
Z_i^0=A_i,
Z_i^1=Beta_i,
Z_i^{m+1}=pred_{x_i}(Z_i^m).
```

Every step gives:

```text
row x_i:       Z_i^{m+1} -> Z_i^m -> Z_i^{m-1},
row Z_i^{m-1}: T_i^m -> Z_i^m,
T_i^m=Z_i^{m-2}*x_i.
```

There are two meaningful clean events.

### 1. Shifted-column repeat first

If:

```text
T_i^r=T_i^s
```

before any main `Z` repeat, then:

```text
beta_zipper_shifted_repeat_split_lemma.md
```

gives a proper same-input split:

```text
row Z_i^{r-1}: T -> Z_i^r,
row Z_i^{s-1}: T -> Z_i^s.
```

This lifts to a same-target pair in `H_T`.

### 2. No shifted repeat first

If no shifted-column repeat occurs first, then by:

```text
fresh_beta_extension_eventual_x_hit_lemma.md
```

the row-`x_i` predecessor chain must eventually hit the generated X-layer:

```text
Z_i^m=x_j.
```

Then:

```text
deep_beta_x_hit_reduction_lemma.md
```

routes the hit to:

```text
watched-layer hit,
row-x_i recurrence,
beta first-hit routing at Beta_j,
or beta-anchored reversible square.
```

## Updated Residual List

After all immediate watched hits are routed, the clean external bridge is now
reduced to:

```text
U1. same-row recurrence boundaries:
    row b, row x_i, or another active source row;

U2. shared-edge divergence:
    Beta_i=H_i gives rows b and x_i sharing H_i -> A_i;

U3. beta-coupled same-target pair:
    for example E_{i,j}->A_i and Beta_j->b in H_{A_j};

U4. shifted-repeat same-input split:
    a beta zipper side-column repeat lifted to H_T;

U5. beta-anchored reversible square:
    from G, beta-X, or a deeper beta-X hit.
```

The former residual:

```text
fresh beta-layer extension
```

has been removed.

## Next Useful Target

The remaining hard cases are no longer one-dimensional growth cases.  They are
cross-role configurations:

```text
same-target pairs,
same-input splits,
shared-edge divergence,
beta-anchored reversible squares.
```

The next useful lemma should compare U3/U4/U5 and look for a common ported
interval collision or a return to the visible crossed-fan/core footprint.

The common local collision tool is:

```text
same_target_pair_collision_trichotomy_lemma.md
```

It applies to the same-target pairs inside U3 and U4, and to U5 whenever its
beta-anchored edge:

```text
Beta_j -> b in H_{A_j}
```

is compared with another edge of the same target.  If such a pair has a common
input, common output, full interval repeat, or input-output cross hit, it
routes to a fan, source collision, or path concatenation.  Only a clean
disjoint same-target matching remains.

For U3 specifically, the clean-disjoint matching is further sharpened by:

```text
beta_coupled_same_target_pair_advance_lemma.md
```

Target advance returns it to:

```text
H_{A_i}: A_j -> b,
H_b:     A_j -> x_{j+1}.
```

So U3 is a two-target bridge back to the generated matching, not a new
independent target layer.

For U4, the corresponding general transport is:

```text
same_input_lift_target_advance_lemma.md
```

It says that a clean lifted same-input pair in `H_T` target-advances back to a
two-target bridge sharing the original input `T`.  Thus U4 also is not a free
same-target matching.
