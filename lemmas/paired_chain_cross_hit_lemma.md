# Paired Chain Cross-Hit Lemma

Date: 2026-06-05.

Status:

```text
proved pressure consequence / paired recursion role
```

Purpose:

```text
Classify what happens when the two paired predecessor chains meet at a fresh
point.
```

## Setup

Use the paired predecessor chains:

```text
b_2*A_i=A_{i+1}
b_3*B_m=B_{m+1}.
```

The zipper identities are:

```text
A_i*(A_{i+1}*b_2)=A_{i-1}
B_m*(B_{m+1}*b_3)=B_{m-1}.
```

## Cross-Hit

Suppose the two chains meet:

```text
A_i=B_m=x.
```

Then substituting into the two zipper identities gives two forced edges in
row `x`:

```text
x*(A_{i+1}*b_2)=A_{i-1}
x*(B_{m+1}*b_3)=B_{m-1}.
```

Therefore the cross-hit is not neutral.

If:

```text
A_{i-1}=B_{m-1},
```

then injectivity of row `x` gives the column coupling:

```text
A_{i+1}*b_2 = B_{m+1}*b_3.
```

If:

```text
A_{i-1}!=B_{m-1},
```

then row `x` has two distinct occupied outputs:

```text
x*(A_{i+1}*b_2)=A_{i-1}
x*(B_{m+1}*b_3)=B_{m-1}.
```

This is extra pressure in the fresh meeting row.

## Consequence

A first cross-hit of the paired chains gives:

```text
column coupling
OR extra pressure in the meeting row.
```

## Strengthening 2026-06-07

The general two-step source reconstruction theorem proves that a cross-hit
cannot have both neighboring points aligned:

```text
A_{i-1}=B_{m-1}
and
A_{i+1}=B_{m+1}
```

would make rows `b_2` and `b_3` contain the same interval:

```text
A_{i-1} -> x -> A_{i+1},
```

and therefore force:

```text
b_2=b_3.
```

See:

```text
paired_chain_aligned_overlap_lemma.md
```

Thus every cross-hit has a genuine mismatch on at least one side.  If the
predecessors agree, the successors are distinct and satisfy a cross-column
coupling.  If the successors agree, the predecessors are distinct and row `x`
has two distinct forced outputs.

Further propagation is recorded in:

```text
shared_edge_divergence_lemma.md
```

Any common incoming or outgoing edge at the cross-hit creates a complete
divergence diamond: distinct next outputs, a common return value, and a return
edge in the shared middle row.

Thus the hard branch must avoid not only bad-cycle hits but also cross-hits
between the two chains.  Otherwise the local configuration is replaced by a
new row-pressure problem with an explicit row `x`.

## Remaining Hard Branch

After this role split, the only still-unclassified fresh branch is:

```text
the A chain stays fresh;
the B chain stays fresh;
neither chain hits the bad-cycle block;
the two chains do not meet;
no row-t or row-b_4 pressure column is hit;
no same-chain repeat has occurred yet.
```

In a finite magma, this branch can persist only until at least one chain
repeats inside itself.  That is the next role to classify.
