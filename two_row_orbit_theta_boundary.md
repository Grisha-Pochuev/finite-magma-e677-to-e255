# Two-Row Orbit Theta Boundary

Date: 2026-06-20.

Status:

```text
boundary / graph normal form for separated period >= 3 windows
```

## Purpose

This is the next narrowing after:

```text
target_advance_same_row_period_lemma.md
two_row_target_advance_window_separation_lemma.md
minimal_g12_loop_normal_form_boundary.md
```

It translates the remaining local separated-window shape into a global
two-row orbit question.

## Setup

Let two distinct rows `p,q` share one target-advance step:

```text
p*b=z,
q*b=z,
p!=q.
```

Write the two row orbits through this shared step as:

```text
... -> x_{-1} -> x_0=b -> x_1=z -> x_2 -> ...
... -> y_{-1} -> y_0=b -> y_1=z -> y_2 -> ...
```

where:

```text
x_{i+1}=p*x_i,
y_{i+1}=q*y_i.
```

Assume the active same-row target-advance components have period at least `3`.

By:

```text
two_row_target_advance_window_separation_lemma.md
```

the windows are separated around the shared step:

```text
x_{-1} != y_{-1},
x_2 != y_2.
```

## First Extra Intersection Split

There are two possibilities.

### 1. The two row cycles meet again

If:

```text
x_i=y_j
```

for some vertex outside the shared pair `{b,z}`, choose the first such
intersection on the two return arcs after the shared edge.

This is a genuine cross-orbit contact.  It is not the already used shared
step, and it is not a local neighboring-port equality around `b -> z`.

This first extra intersection is the next place where the relay proof must
decide between:

```text
independent full ported-interval collision,
side/return attachment giving a smaller relay object,
or a new first-merge relay.
```

It is routed more precisely by:

```text
two_row_first_extra_intersection_routing_lemma.md
```

to full interval collision, fan/path attachment, or the already familiar
clean same-input two-target bridge form.

### 2. The two row cycles do not meet again

If the cycles have no common vertex outside:

```text
{b,z},
```

then their union has the following undirected shape:

```text
common edge b--z,
p-row return path z ... b,
q-row return path z ... b.
```

That is a theta graph in the target-advance state space with endpoints `b`
and `z`.

The period `>= 3` assumption makes both return paths nontrivial, so this is
not a fixed point or swap loop.

## Consequence For G12

The remaining separated period `>= 3` G12 residue splits into:

```text
1. first extra intersection of the two row cycles;
2. clean two-row orbit theta in the target-advance state space.
```

The first branch should produce a smaller relay, a side/return attachment, or
an independent full interval collision; its clean matching subcase becomes a
same-input two-target bridge after target advance.

The second branch is the clean shape that must be compared to:

```text
strict_clean_theta_exclusion_lemma.md
```

## Remaining Translation Gap

This file does not prove that a clean two-row orbit theta is already the same
object as the strict clean mixed theta inside a fixed `H_b`.

It isolates the exact translation still needed:

```text
show that a clean target-advance orbit theta either becomes the strict clean
theta already excluded, or yields an independent repeated full ported
interval when translated back to active relay states.
```
