# No-Bridge Orbit Tail Candidate

Date: 2026-06-04.

Status:

```text
candidate termination layer / local evidence, not global proof
```

Purpose:

```text
Continue offset_bridge_orbit_dichotomy_lemma.md by isolating the remaining
no-bridge gap.
```

## Setup

In the no-bridge branch of the offset split, the useful invariant is the
row-`b_3` orbit.

Write a source-orbit prefix:

```text
b_3*z0=z1
b_3*z1=z2
b_3*z2=z3
...
```

The inverse-edge chain gives the orbit relay:

```text
z1*(z2*b_3)=z0
z2*(z3*b_3)=z1
z3*(z4*b_3)=z2
...
```

So a zero-avoiding prefix is not free: every new source edge creates a return
edge in the previous source-row value.

## Zero-Hit Role

If the orbit reaches `0`:

```text
b_3*q=0
b_3*0=r
```

then the orbit relay gives:

```text
0*(r*b_3)=q.
```

Since row `0` is the bad-cycle row, this determines:

```text
r*b_3=pred0(q).
```

This is a real descent: the next edge is forced in row `r=b_3*0`, and its
target is the predecessor of `q` in the known row-0 cycle.

This role already appears in:

```text
row6_orbit_relay_lemma.md
source_orbit_ladder_lemma.md
special_branch_role_split_lemma.md
```

## Short-Cycle Role

If a zero-avoiding prefix closes a short cycle:

```text
z0 -> z1 -> z2 -> z0
```

then the relay gives a return edge:

```text
z1*(z2*b_3)=z0.
```

Local no-bridge diagnostics in case45 showed that these short source cycles
are killer layers, not live counterexample shapes:

```text
t=2: 8 -> 1 -> 3 -> 8 closed all row-b_3 shapes.
t=3: 8 -> 1 -> 2 -> 8 closed all row-b_3 shapes.
```

The important structural reading is:

```text
a short zero-avoiding source cycle already has enough return edges to collapse
the residual row.
```

## Longer Zero-Avoiding Prefix Role

The first longer zero-avoiding prefixes also did not create a new kind of
residual.

In the no-bridge self layer for numeric `t=2`, the prefix:

```text
8 -> 1 -> 3
```

had possible next roles:

```text
3 -> 0  early zero-hit
3 -> 8  short 3-cycle
3 -> 4  longer zero-avoiding
3 -> 7  longer zero-avoiding
```

All closed.

In the special branch role split, the same pattern reappeared:

```text
eventual zero-hit
short source-cycle
direct-killer sublayer
compact zero-avoiding prefix-collapse
```

So the current candidate is:

```text
Every zero-avoiding source-orbit prefix either reaches the zero-hit role,
forms a short return cycle, or adds enough return edges that the active row
collapses to a finite compact certificate.
```

## Why This Matters For The Main Lemma

Together with the bridge-orbit dichotomy:

```text
offset branch -> self-return OR unique bridge OR no-bridge orbit relay
```

this turns the main no-free-tail gap into one problem:

```text
Prove compact prefix-collapse for the no-bridge row-b_3 orbit.
```

The old local searches should not be resumed as arbitrary row enumeration.
The only meaningful next checks are role checks:

```text
zero-hit;
short source-cycle;
longer zero-avoiding prefix with its forced return edges.
```

## Remaining Gap

The candidate still needs a general proof that compact prefix-collapse must
terminate in every finite no-bridge orbit.

The strongest current formulation is:

```text
In a finite E677 magma, a no-bridge row-b_3 source orbit cannot be a free
zero-avoiding tail.  After each new edge b_3*z_i=z_{i+1}, the relay edge
z_i*(z_{i+1}*b_3)=z_{i-1} either hits the known row-0 predecessor structure,
creates a short source-cycle return, or occupies a lower source row.  Finiteness
then forbids an infinite succession of fresh roles.
```

This is not yet a proof; it is the next lemma target.

