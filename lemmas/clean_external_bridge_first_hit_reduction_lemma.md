# Clean External-Bridge First-Hit Reduction Lemma

Date: 2026-06-18.

Status:

```text
proved reduction / exact residual split, not final contradiction
```

## Purpose

This combines the recent connector work into one usable reduction for the
proper bad-target crossed-fan clean external bridge.

It replaces the too-strong old wording:

```text
right-b orbit repeat returns directly to branch relay.
```

The correct statement is more precise:

```text
right-b orbit and row-b predecessor towers force one of several exact
first-hit roles; only the listed residuals remain.
```

## Starting Residual

Work in the clean external-bridge residual:

```text
h!=k,
{c,d} ∩ {u,v}=empty,
t=a*b,
k -> t is a real H_b edge,
k,t not in {a,c,d,u,v},
t not in {b,h,k}.
```

The second certificate gives:

```text
ell=t*a=pred_b(k),
b*ell=k,
ell!=h.
```

Start the right-`b` orbit:

```text
x_0=a,
x_1=t,
x_{i+1}=x_i*b,
A_i=pred_{x_i}(b),
H_i=pred_b(A_i)=x_{i+1}*x_i.
```

Then:

```text
x_i*A_i=b,
x_i*b=x_{i+1},
b*H_i=A_i.
```

## Step 1: Generated H_b Footprint

The generated `H_b` edge at index `i` is:

```text
A_i -> x_{i+1}.
```

By:

```text
ported_cycle_hb_footprint_trichotomy_lemma.md
```

the first nonclean event in this generated footprint is one of:

```text
1. A_i=A_j:
   outgoing fan in H_b;

2. x_{i+1}=x_{j+1}:
   incoming fan in H_b;

3. A_i=x_{j+1}:
   actual H_b path concatenation;

4. visible-footprint hit:
   direct attachment to the crossed-fan/core footprint.
```

If none occurs, the generated `H_b` footprint is a clean matching:

```text
A_i -> x_{i+1}.
```

## Step 2: Row-b Predecessor Layer

In the clean matching case, the remaining coupling is:

```text
H_i --row b--> A_i --H_b/source x_i--> x_{i+1}.
```

By:

```text
clean_ported_matching_predecessor_layer_boundary.md
```

if the `A_i` are pairwise distinct, then the `H_i` are pairwise distinct:

```text
H_i=H_j <=> A_i=A_j.
```

The first hit of the row-`b` predecessor layer is classified by:

```text
row_b_predecessor_tower_dichotomy_boundary.md
row_b_tower_first_hit_role_map.md
```

It is one of:

```text
1. H_i=A_j:
   row-b tower cross-hit H_j -> A_j -> A_i;

2. H_i=x_j:
   X-layer hit / two-target bridge between rows b and x_j;

3. H_i visible:
   core attachment;

4. H_i=A_i:
   row-b fixed point boundary;

5. no hit:
   extend the row-b predecessor tower backward.
```

## Step 3: Finite Tower Boundary

If the tower keeps extending backward, finiteness of row `b` gives a first
nonfresh event.  By the same role map, the first event is:

```text
1. A-layer hit;
2. X-layer hit;
3. visible hit;
4. row-b fixed point;
5. or closure of a row-b cycle disjoint from the watched set.
```

The A-layer-only branch is recorded in:

```text
row_b_a_layer_cycle_boundary.md
```

It closes as a row-`b` cycle on generated inputs:

```text
A_{i_0} -> A_{i_1} -> ... -> A_{i_m} -> A_{i_0}
```

with the matching edges:

```text
A_i -> x_{i+1}
```

still attached.

The X-layer branch is recorded in:

```text
row_b_x_layer_hit_target_bridge_boundary.md
```

It creates the two-target corner:

```text
row b:   x_j -> A_i
row x_j: A_j -> b -> x_{j+1}
```

and must be routed by target-swap/bridge-pair transport.

## Final Reduction

Therefore the clean external bridge is reduced to the following exact
alternatives:

```text
A. generated H_b outgoing fan;
B. generated H_b incoming fan;
C. generated H_b path concatenation;
D. visible crossed-fan/core attachment;
E. row-b fixed point boundary;
F. row-b A-layer cycle boundary;
G. X-layer two-target bridge boundary;
H. independent row-b predecessor cycle disjoint from the watched set.
```

Cases A-D return to the known branch-relay / core-attachment frontier.

Case E is a row-`b` fixed point boundary, not a bad-target right fixer.

Cases F-H are the remaining exact residuals.  They are strictly sharper than
the previous vague "clean external bridge" obstruction.

## Next Work

The next useful mathematical target is:

```text
route G, the X-layer two-target bridge boundary.
```

If G relays to a known crossed-fan/target-swap form, then the remaining
clean-external-bridge obstruction is only the row-`b` independent cycle
boundary F/H.
