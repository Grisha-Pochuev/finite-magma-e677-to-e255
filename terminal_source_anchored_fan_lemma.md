# Terminal-Source Anchored Fan Lemma

Date: 2026-06-08.

Status:

```text
general proved / anchors the three-source fan to the old bad tail
```

## Setup

Let the bad row-`0` cycle have length `m`:

```text
b_0=0
0*b_j=b_{j-1}.
```

Write:

```text
P=b_2
A=0*0.
```

Since row `0` sends:

```text
0 -> A,
```

we have:

```text
A=b_{m-1}.
```

## Universal Terminal Source

Apply E677 with:

```text
x=0
y=0.
```

It gives:

```text
0=0*(0*((0*0)*0)).
```

Write:

```text
A=0*0
R=A*0.
```

Then:

```text
0*(0*R)=0.
```

The unique preimage of `0` in row `0` is `b_1`, so:

```text
0*R=b_1.
```

The unique preimage of `b_1` in row `0` is `b_2=P`, hence:

```text
R=P.
```

Therefore:

```text
A*0=P.
```

So the terminal bad-cycle point `A=b_{m-1}` is always a source of:

```text
0 -> P.
```

## Anchored Backward Foot

The bad-cycle predecessor ladder in row:

```text
A=b_{m-1}
```

gives:

```text
A*r_{m-2}=b_m=0.
```

Together with:

```text
A*0=P,
```

row `A` contains:

```text
r_{m-2} -> 0 -> P.
```

The two-sided fan defines:

```text
alpha_A=0*(P*A)
A*alpha_A=0.
```

Row `A` has a unique preimage of `0`, so:

```text
alpha_A=r_{m-2}.
```

Equivalently:

```text
0*(P*A)=r_{m-2}.
```

## Self-Source Comparison

Assume:

```text
P*0=P.
```

The self-source backward foot is:

```text
alpha_P=0*(P*P)=h
P*h=0.
```

Backward feet in the common-edge fan are pairwise distinct, so:

```text
h!=r_{m-2}.
```

Thus rows `P` and `A` contain:

```text
row P:
  h -> 0 -> P

row A:
  r_{m-2} -> 0 -> P.
```

## Three-Source Form

If:

```text
B*0=P,
```

define:

```text
alpha_B=0*(P*B).
```

Then:

```text
B*alpha_B=0
```

and:

```text
alpha_B notin {h,r_{m-2}}.
```

The three-source fan therefore creates three pairwise distinct zero
predecessors:

```text
P*h=0
A*r_{m-2}=0
B*alpha_B=0,
```

while all three rows share:

```text
0 -> P.
```

## Significance

The fan-tip bridge recursion is anchored to the old bad cycle:

```text
self source P
  -> backward foot h;

terminal source A=0*0
  -> backward foot r_{m-2};

third source B
  -> a third distinct backward foot.
```

One of the two-sided fan intervals already contains the old tail
`r_{m-2}`.

