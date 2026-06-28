# Paired-Chain Aligned-Overlap Lemma

Date: 2026-06-07.

Status:

```text
general proved application of two-step source reconstruction
```

Purpose:

```text
Give the paired predecessor chains a genuine cross-source obstruction.
```

## Setup

Use:

```text
b_2*A_i=A_{i+1}
b_3*B_m=B_{m+1}.
```

Recall:

```text
b_2!=b_3.
```

## No Common Aligned Two-Step Interval

Suppose the chains meet at:

```text
A_i=B_m=x.
```

If both neighboring points also agree:

```text
A_{i-1}=B_{m-1}=a
A_{i+1}=B_{m+1}=c,
```

then rows `b_2` and `b_3` both contain:

```text
a -> x -> c.
```

The two-step source reconstruction lemma forces:

```text
b_2=b_3,
```

which is impossible.

Therefore every cross-hit satisfies:

```text
A_{i-1}!=B_{m-1}
or
A_{i+1}!=B_{m+1}.
```

Equivalently, the two source cycles can share a point or even one directed
edge, but they cannot share two aligned consecutive directed edges.

## Sharpened Cross-Hit Roles

At a cross-hit:

```text
A_i=B_m=x,
```

the zipper gives:

```text
x*(A_{i+1}*b_2)=A_{i-1}
x*(B_{m+1}*b_3)=B_{m-1}.
```

There are now only three possible forms.

### Same predecessors

If:

```text
A_{i-1}=B_{m-1},
```

then the successors must differ:

```text
A_{i+1}!=B_{m+1}.
```

Row-`x` injectivity gives the genuine cross-column coupling:

```text
A_{i+1}*b_2=B_{m+1}*b_3.
```

Thus distinct successors are tied by different source columns.

### Same successors

If:

```text
A_{i+1}=B_{m+1},
```

then the predecessors must differ:

```text
A_{i-1}!=B_{m-1}.
```

Hence row `x` has two distinct forced outputs.

### Both sides differ

If both neighboring pairs differ, row `x` again carries two distinct forced
outputs, unless a separate column coupling occurs.

## Initial Pivot Consequence

At the initial common pivot:

```text
A_1=B_0=t,
```

the neighboring points are:

```text
A_0=0
A_2=b_2*t

B_{-1}=c_{-1}
B_1=b_4.
```

Therefore:

```text
c_{-1}=0
and
b_2*t=b_4
```

cannot hold simultaneously.

So:

```text
c_{-1}=0     => b_2*t!=b_4,
b_2*t=b_4    => c_{-1}!=0.
```

This is a new exact restriction inside the pivot fan.  It does not close either
role alone, but it prevents the two active source rows from merging into the
same interval around `t`.

## Significance

Finiteness alone allowed the row-`b_2` and row-`b_3` predecessor cycles to
close independently.  The reconstruction theorem now adds a real interaction:

```text
their closures cannot overlap with the same local orientation for two steps.
```

The remaining No-Free-Tail gap is narrower:

```text
show that the surrounding row-t and row-b_4 fans force such an aligned
two-edge overlap, or force one of the already classified unequal-neighbor
pressure roles.
```

The one-edge-overlap cases are now sharpened further in:

```text
shared_edge_divergence_lemma.md
```

A common directed edge forces distinct next outputs and a common return
column.  Thus even a one-edge overlap creates an explicit pressure diamond.
