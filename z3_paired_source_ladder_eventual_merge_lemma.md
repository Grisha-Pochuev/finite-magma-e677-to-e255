# Z3 Paired Source-Ladder Eventual Merge Lemma

Date: 2026-06-19.

Status:

```text
proved reduction / clean paired source ladders must reach a first merge event
```

## Purpose

This continues:

```text
clean_external_bridge_ninth_stage_reduction_lemma.md
fixed_target_source_orbit_ladder_lemma.md
fixed_target_source_orbit_first_merge_boundary.md
```

The clean paired four-edge shell should not be expanded as an infinite fresh
tree.  It is two deterministic forward source ladders in the same finite
target graph `H_{A_j}`.  Therefore a first merge/repeat event must occur.

## Setup

Fix:

```text
T=A_j.
```

Define the two source-successor ladders:

```text
r_0=p,     r_{n+1}=r_n*T,
s_0=x_j,   s_{n+1}=s_n*T.
```

The first known values are:

```text
r_1=S,
r_2=V=S*T,

s_1=b,
s_2=D_j=b*T.
```

For each source row define the `H_T` edge:

```text
I_n=pred_{r_n}(T),   row r_n: I_n -> r_{n+1},
J_n=pred_{s_n}(T),   row s_n: J_n -> s_{n+1}.
```

The ladder predecessor formula is:

```text
I_{n+1}=(r_n*r_{n+1})*r_n,
J_{n+1}=(s_n*s_{n+1})*s_n.
```

## Eventual First Event

Because the magma is finite, the combined finite list of source rows:

```text
r_0,r_1,r_2,...,
s_0,s_1,s_2,...
```

cannot remain pairwise fresh forever.

So there is a first source-row event of one of the following forms:

```text
1. r_n=r_m with n>m;
2. s_n=s_m with n>m;
3. r_n=s_m.
```

Before that source event, there may be an earlier endpoint event among the
`H_T` edges:

```text
I_n=I_m, I_n=J_m, J_n=J_m,
r_{n+1}=r_{m+1}, r_{n+1}=s_{m+1}, s_{n+1}=s_{m+1},
I_n=r_{m+1}, I_n=s_{m+1}, J_n=r_{m+1}, J_n=s_{m+1}.
```

Take the earliest event among source-row hits and edge-endpoint hits.

## Routing Of First Endpoint Events

The involved edges all lie in the same fixed target graph:

```text
H_T=H_{A_j}.
```

Therefore:

```text
same input       -> outgoing fan in H_T;
same output      -> incoming fan in H_T;
same full edge   -> full ported interval, hence source-row collision;
input-output hit -> directed path in H_T.
```

These roles are exactly:

```text
same_target_pair_collision_trichotomy_lemma.md
```

applied to the two edges where the first endpoint event occurs.

## Routing Of First Source Events

If:

```text
r_n=s_m,
```

then the two ladders have reached the same source row in the same target graph
`H_T`.  The corresponding full ported interval is determined by that source
row and target, so this is a cross-ladder ported-interval repeat unless an
endpoint event was earlier.

If:

```text
r_n=r_m
or
s_n=s_m,
```

then one ladder has repeated a source row.  This is a fixed-target source
recurrence boundary.  If the two occurrences are in independent branch roles,
ported-interval reconstruction gives a source collision; if they are in one
self-ladder, it is a same-row recurrence boundary.

## Consequence

The clean paired four-edge shell cannot remain an open-ended fresh residual.
It reduces to:

```text
1. an H_{A_j} fan/path/full-interval collision;
2. a cross-ladder source hit;
3. a same-ladder source recurrence boundary;
4. a watched visible/generated hit if the first event lands in the watched
   footprint.
```

Thus the only non-routed outcome of the Z3 paired ladder is a same-row or
same-ladder recurrence boundary.  This belongs with:

```text
N1. same-row recurrence boundaries.
```

