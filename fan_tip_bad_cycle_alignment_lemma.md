# Fan-Tip Bad-Cycle Alignment Lemma

Date: 2026-06-08.

Status:

```text
general proved / exact descent for the aligned occupied-tip role
```

## Setup

Use the fan-spine notation:

```text
P*0=P
C=P*P
h=0*C
q*0=P
T=q*P
T*q=h.
```

Assume both the central tip and another fan tip lie on the bad row-0 cycle:

```text
C=b_j
T=b_k.
```

Then:

```text
h=b_{j-1}.
```

## Aligned Case

Suppose:

```text
k=j-2.
```

Then:

```text
h=b_{j-1}=b_{k+1}.
```

The fan return gives:

```text
b_k*q=b_{k+1}.
```

The bad-cycle predecessor ladder gives:

```text
b_k*r_{k-1}=b_{k+1}.
```

Row `b_k` is injective, so:

```text
q=r_{k-1}.
```

Therefore:

```text
C=b_{k+2}
T_q=b_k
=>
q=r_{k-1}.
```

The fan source is not fresh: it is exactly an older bad-cycle tail.

## Non-Aligned Case

If:

```text
k!=j-2,
```

then:

```text
h=b_{j-1}!=b_{k+1}.
```

Row `b_k` contains two distinct occupied edges:

```text
b_k*q=b_{j-1}
b_k*r_{k-1}=b_{k+1}.
```

This is genuine occupied-row pressure, but not yet a contradiction.

Thus every bad-cycle fan-tip hit has the exact split:

```text
aligned index k=j-2 -> old-tail descent q=r_{k-1};
other index          -> two distinct forced edges in row b_k.
```

## Significance

The phrase:

```text
a fan tip hits the bad cycle
```

is too coarse. The controlling marker is the relative index between the tip
`T=b_k` and the central tip `C=b_j`.

The aligned difference of two closes symbolically. Future work should address
only the non-aligned occupied-row pressure.

