# Clean External-Bridge Second-Stage Reduction Lemma

Date: 2026-06-18.

Status:

```text
proved reduction / exact second-stage residual split, not final contradiction
```

## Purpose

This updates:

```text
clean_external_bridge_first_hit_reduction_lemma.md
```

after routing:

```text
G: X-layer two-target bridge,
Beta_i=A_j: same-input split,
Beta_i=x_j: beta-X target bridge.
```

The result is a sharper list of what remains after all visible/generated hits
are routed.

## Starting Point

Use the clean external-bridge residual and generated notation:

```text
x_{i+1}=x_i*b,
A_i=pred_{x_i}(b),
H_i=pred_b(A_i),
Beta_i=pred_{x_i}(A_i).
```

So:

```text
b*H_i=A_i,
x_i*Beta_i=A_i,
x_i*A_i=b,
x_i*b=x_{i+1}.
```

The first-stage reduction leaves:

```text
A-D: generated H_b fan/path or visible core attachment;
E: row-b fixed point boundary;
F: row-b A-layer cycle boundary;
G: X-layer two-target bridge boundary;
H: independent row-b predecessor cycle disjoint from the watched set.
```

## G Branch After Routing

If:

```text
H_i=x_j,
```

then:

```text
b*x_j=A_i,
x_j*A_j=b.
```

Define:

```text
alpha=x_j*(A_i*b),
gamma=A_j*A_i=Beta_j.
```

By:

```text
x_layer_two_target_bridge_reduction_lemma.md
same_input_split_target_lift_lemma.md
```

G reduces to:

```text
1. visible/generated-layer hit by alpha or gamma;
2. row-b swap x_j <-> A_i;
3. adjacent recurrence A_j=x_{j+1};
4. beta-coupled same-input lift when alpha=A_j;
5. fresh reversible two-target square.
```

The beta-coupled lift is explicit:

```text
H_{A_j}:  H_j    -> x_j,
          Beta_j -> b.
```

The fresh reversible square is:

```text
(A_i, x_j, b*A_i) <-> (x_j, alpha, A_i),
(b, A_j, x_{j+1}) <-> (A_j, Beta_j, b).
```

Thus G is no longer an open target-swap tower.

## Beta Layer After Routing

For the independent row-`b` cycle boundary F/H, each generated input `A_i`
also has beta pressure:

```text
Beta_i=pred_{x_i}(A_i).
```

By:

```text
beta_layer_reduction_lemma.md
```

the beta layer reduces to:

```text
1. Beta_i=H_i:
   shared-edge divergence of rows b and x_i at H_i -> A_i;

2. Beta_i=A_j:
   beta-coupled same-target pair in H_{A_j};

3. Beta_i=x_j:
   beta-X reversible two-target square;

4. visible hit:
   attachment to the crossed-fan/core footprint;

5. fresh Beta_i:
   a genuine new predecessor layer in row x_i.
```

The beta-A same-target pair is:

```text
H_{A_j}:  E_{i,j} -> A_i,
          Beta_j  -> b,
```

where:

```text
E_{i,j}=A_j*(A_i*x_i).
```

The beta-X reversible square is:

```text
(A_i, x_j, b)      <-> (x_j, delta, A_i),
(b, A_j, x_{j+1}) <-> (A_j, Beta_j, b),
```

where:

```text
delta=x_j*(A_i*x_i).
```

## Second-Stage Residual List

After all immediate visible/generated hits are routed, the clean external
bridge is reduced to these exact remaining forms:

```text
R1. same-row recurrence:
    row-b fixed point or row-b swap boundary;

R2. row-b independent predecessor cycle:
    but now with beta pressure at every generated A_i;

R3. beta-coupled fresh same-target pair:
    E_{i,j}->A_i and Beta_j->b in H_{A_j};

R4. fresh reversible two-target square:
    either from G or from Beta_i=x_j;

R5. genuinely fresh beta-layer extension:
    pred_{x_i}(Beta_i) begins a new row-x_i predecessor layer.
```

This is strictly sharper than the previous residual list F/G/H.

By:

```text
fresh_reversible_square_beta_anchor_lemma.md
```

R4 is not independent from R5.  Every fresh reversible square contains the
ported interval:

```text
(A_j, Beta_j, b),
```

so if `Beta_j` does not route by the beta first-hit split, it is a fresh
beta-layer anchor.

The compressed residual list is therefore:

```text
S1. same-row recurrence boundaries;
S2. row-b independent predecessor cycle with beta pressure;
S3. beta-coupled fresh same-target pair;
S4. fresh beta-layer extension, possibly carrying a reversible square.
```

## Next Useful Target

The next proof step should not re-route G from scratch.

The useful target is now to attack the fresh beta-layer extension itself.

The desired new lemma would say that a minimal clean beta extension cannot
stay indefinitely disjoint from the visible crossed-fan footprint; it must
produce either a watched-layer hit, an outgoing fan in some H-target, or a
cross-role full ported interval collision.
