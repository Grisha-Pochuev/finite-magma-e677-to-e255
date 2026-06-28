# Paired Chain First Obstruction Lemma

Date: 2026-06-05.

Status:

```text
candidate map / corrected finite boundary
```

Purpose:

```text
Combine the paired-chain role lemmas into one finite obstruction statement.
```

## Setup

Assume the nonzero-offset setup:

```text
t=r_2=b_2*0
t!=0
b_3*t=b_4.
```

Use the paired predecessor chains:

```text
A_1=t
A_0=0
A_{i-1}=A_i*(A_{i+1}*b_2)
b_2*A_{i-1}=A_i
```

and:

```text
B_1=b_4
B_0=t
B_{i-1}=B_i*(B_{i+1}*b_3)
b_3*B_{i-1}=B_i.
```

These chains start from the double interval:

```text
row b_2:
  ... -> A_{-1}=u_2 -> A_0=0 -> A_1=t

row b_3:
  ... -> B_{-1}=c_{-1} -> B_0=t -> B_1=b_4.
```

## Finite First Obstruction

Because the magma is finite and rows `b_2` and `b_3` are permutations, the two
backward chains cannot keep producing pairwise new elements forever.

Therefore, moving backward from:

```text
A_0=0, A_1=t
B_0=t, B_1=b_4,
```

there is a first obstruction of one of the following types:

```text
1. A new chain point hits the bad-cycle block.
2. A new A-chain point equals a B-chain point.
3. A new point repeats inside the A chain.
4. A new point repeats inside the B chain.
5. A new point hits an already listed pressure column:
   z_t, b_4*b_3, p, r_3, or a previously created zipper column.
```

The first four are structural and already classified.

## Role Classification

Bad-cycle hit:

```text
paired_chain_bad_cycle_hit_lemma.md
```

gives:

```text
bad-cycle descent
OR extra row-b_j pressure.
```

Cross-hit:

```text
paired_chain_cross_hit_lemma.md
paired_chain_aligned_overlap_lemma.md
```

gives:

```text
cross-column coupling between distinct successors
OR extra pressure in the meeting row;
two aligned consecutive common edges are impossible.
```

Same-chain repeat:

```text
same_chain_repeat_pressure_lemma.md
```

gives:

```text
exact closure of the corresponding source-row cycle.
```

Occupied origin predecessor:

```text
occupied_u2_lift_lemma.md
```

gives:

```text
row-t zero collision
OR origin/offset predecessor coupling
OR bad-cycle descent
OR extra row-t pressure.
```

## Result

The paired-chain fresh branch cannot produce new points forever, but finiteness
alone only guarantees closure of the two permutation cycles.

It has the following forced form:

```text
fresh extension continues only until the first obstruction;
the first obstruction is one of:
  descent;
  self-loop/self-swap;
  column coupling;
  row-t collision;
  row-b_4 collision;
  extra occupied row pressure;
  or ordinary closure of one source-row cycle.
```

Therefore the earlier wording:

```text
Any first obstruction must immediately contradict injectivity or descend.
```

was too strong.  A same-chain repeat may simply close a cycle of row `b_2` or
row `b_3`.

The corrected remaining bridge is now narrower:

```text
Use the row-t and row-b_4 fans to force either:
  two aligned common edges between the closed cycles;
  or one of the unequal-neighbor cross-hit pressure roles.
```

That bridge, if proved, gives:

```text
t=r_2 cannot be nonzero
=> r_2=0
=> E255 for 0.
```

## Next Work

The next symbolic target should be one of these, not a broad search:

```text
1. Derive a cross-relation between the complete A and B cycles.
2. Use the row-t and row-b_4 pressure edges to force a cross-hit.
3. Show that independent closure of both cycles violates an E677 triangle.
```

Any computation should test only one of these bridge roles in a bounded
representative.
