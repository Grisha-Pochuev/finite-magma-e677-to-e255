# Anchored-M7 First-Event Routing Lemma

Date: 2026-06-21.

Status:

```text
proved reduction / first events before clean self-repeat are routed
```

## Purpose

This file upgrades:

```text
anchored_m7_first_merge_target.md
anchored_x3_source_orbit_boundary.md
fixed_target_source_orbit_first_merge_boundary.md
same_target_pair_collision_trichotomy_lemma.md
```

from a target statement to the exact routed part of the anchored-M7
classification.

It records that the first finite event among the three anchored right-`h`
source-successor orbits is not a new residual unless it is a clean self-repeat
inside one orbit.

## Setup

Use the anchored-X3 false branch:

```text
p*b=q*b=z,
U=p*z,
W=q*z,
h=U*p=W*q,
z*h=b,
alpha=pred_z(h),
T=U*h,
S=W*h,
T!=S.
```

The three displayed edges in `H_h` are:

```text
row U: p     -> T,
row W: q     -> S,
row z: alpha -> b.
```

Define the three right-`h` source-successor orbits:

```text
R_U^0=U,  R_U^{n+1}=R_U^n*h,
R_W^0=W,  R_W^{n+1}=R_W^n*h,
R_z^0=z,  R_z^{n+1}=R_z^n*h.
```

For each source row `r=R_A^n`, row `r` gives an edge in `H_h`:

```text
I_A^n -> R_A^{n+1},
r*I_A^n=h.
```

The predecessor formula gives:

```text
I_A^n=h*(R_A^{n+1}*R_A^n).
```

## Routed First Events

### 1. Cross-Orbit Source Hit

If:

```text
R_A^i=R_B^j,
A!=B,
```

then the same source row appears in the same fixed target graph `H_h`.
Therefore it carries the same full ported interval:

```text
(h,I_A^i,R_A^{i+1})=(h,I_B^j,R_B^{j+1}).
```

By `ported_interval_state_lemma.md`, this is a same-source recurrence.  In a
genuine cross-role occurrence it is an independent full ported-interval
collision.  If it is not cross-role, it has collapsed to the same-orbit
recurrence boundary.

So a cross-orbit source hit is routed.

### 2. Cross-Orbit Output Merge

If:

```text
R_A^{i+1}=R_B^{j+1},
R_A^i!=R_B^j,
```

then two different rows in `H_h` have the same output:

```text
I_A^i -> R_A^{i+1},
I_B^j -> R_A^{i+1}.
```

If the inputs are different, this is an incoming fan in `H_h`.

If the inputs also agree, the two edges are the same full ported interval,
which returns to the previous source-collision route.

Thus an output merge is routed by:

```text
same_target_pair_collision_trichotomy_lemma.md
```

### 3. Input-Output Cross Hit

If an input of one active `H_h` edge equals the output of another, for example:

```text
I_A^i=R_B^{j+1}
```

or symmetrically, then the two edges concatenate into an actual directed path
inside the fixed target graph `H_h`.

This is a path attachment, not a fresh disjoint source-orbit residual.

### 4. Watched/Core Hit

If any active source, input, or output hits the displayed anchored footprint:

```text
U,W,z,T,S,b,p,q,alpha,h
```

or an older core/corridor footprint of the global G12 loop, then the anchored
branch is no longer clean.  It is routed as a visible attachment or return to
the existing relay/core machinery.

This includes the short visible repeats already separated in:

```text
anchored_x3_visible_short_repeat_lemma.md
```

## Clean Residual

After the routed first events are excluded, the only live finite event is:

```text
clean self-repeat inside one right-h source-successor orbit
```

meaning:

```text
R_A^m=R_A^n,
0 <= m < n,
```

and before this event there is:

```text
no cross-orbit source hit,
no output merge,
no input-output cross hit,
no watched/core hit,
no earlier self-repeat.
```

This is exactly the normal form recorded in:

```text
anchored_x3_clean_self_repeat_normal_form.md
```

## Consequence For M7

The anchored-M7 measure should no longer spend cases on first-event types
1-4.  The only remaining proof obligation is:

```text
clean same-orbit right-h self-repeat
```

and it must be attacked as a cycle with a chosen start, predecessor, end, and
next-to-last row.  This is the part not yet closed.

The most useful next formulation is a cycle-end template:

```text
r_0*h=r_1,
r_{n-1}*h=r_0,
r_{n-2}*h=r_{n-1},
```

together with the attached `H_h` predecessor edges:

```text
I_i=h*(r_{i+1}*r_i),
I_i -> r_{i+1} in H_h.
```

This mirrors the small `cycle-sen.p` idea from the external `eq677` repository:
do not only model the first fresh layer; also model the end and next-to-last
positions of the self-repeat cycle.
