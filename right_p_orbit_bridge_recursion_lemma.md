# Right-P Orbit Bridge Recursion Lemma

Date: 2026-06-09.

Status:

```text
general proved / exact finite-state form of the bridge recursion
```

## Setup

Fix `P`. Start with:

```text
q_0*a_0=P.
```

Define:

```text
q_{i+1}=q_i*P.
```

For every `i`, let `a_i` be the unique preimage of `P` in row `q_i`:

```text
q_i*a_i=P.
```

## Explicit Predecessor Formula

The inverse edge chain gives:

```text
a_i=P*((q_i*P)*q_i)
   =P*(q_{i+1}*q_i).
```

Writing:

```text
d_i=q_{i+1}*q_i,
```

we have:

```text
P*d_i=a_i
d_i=pred_P(a_i).
```

## Bridge Step

Apply E677 with `x=P,y=q_i`:

```text
P=(q_i*P)*((q_i*(q_i*P))*q_i).
```

Since `q_{i+1}=q_i*P`, uniqueness of the preimage of `P` in row `q_{i+1}`
gives:

```text
a_{i+1}=(q_i*q_{i+1})*q_i
q_{i+1}*a_{i+1}=P.
```

Thus the fan-tip bridge from `q_i` is exactly `a_{i+1}`. It is not a separate
arbitrary value: it is the predecessor of `P` in the next right-orbit row.

## Coupled Double Interval

Define:

```text
beta_i=a_i*(P*q_i).
```

The edge-predecessor triangle applied to `q_i*a_i=P` gives:

```text
q_i*beta_i=a_i.
```

Therefore every state carries:

```text
row q_i:
  beta_i -> a_i -> P -> q_{i+1}

row P:
  d_i -> a_i

d_i=q_{i+1}*q_i.
```

The bridge process is a deterministic recursion of coupled double intervals.

## Source Return Criterion

Assume initially:

```text
q_0*0=P.
```

Then `a_0=0`, and for every `i`:

```text
a_i=0
<=>
q_i*0=P
<=>
q_i in F(0,P).
```

Hence:

```text
zero bridge
<=>
the right-P orbit has returned to the source fiber.
```

## Finite Orbit Dichotomy

Because the magma is finite, every right-`P` orbit eventually repeats.
For a source-started orbit, the structural outcomes are:

```text
1. source return:
   q_i enters F(0,P), hence a_i=0;

2. cycle-entry fan:
   at the first repeated orbit point, its two distinct predecessor rows share
   the edge P -> q_i and create a new two-sided common-edge fan.
```

Indeed, a tail entering a cycle always gives the second outcome at the entry
point. Thus an external cycle is not a third collision-free possibility.

## Exact No-Free-Tail Reformulation

The single-chain no-free-tail statement is now proved:

```text
an anchored source orbit cannot remain collision-free forever.
```

A finite bridge chain therefore cannot stay free. If it does not return to the
source fiber, its first repetition creates a new two-sided fan.

The remaining full No-Free-Tail theorem is the next recursive level: show that
successive cycle-entry fans cannot keep changing their common edge while
avoiding the original bad-cycle anchor.

## Good Six-Cycle Specialization

For:

```text
P*P=C
C*P=h
h*P=P,
```

the self-source right-`P` orbit is:

```text
P -> C -> h -> P.
```

It returns to `P in F(0,P)` and is not a free tail. Any free tail from the
terminal source `A` or the bad-tail source `B` must avoid:

```text
{P,C,h}.
```

Meeting any of these points forces a later return to the source `P`. If an
orbit avoids them, its first repetition creates a cycle-entry fan.
