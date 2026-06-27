# R-b5 A-Layer Footprint Descent Boundary

Date: 2026-06-19.

Status:

```text
boundary / A-layer row-b repeats have a finite footprint descent
```

## Purpose

This complements:

```text
rb5_a_layer_cycle_base_bridge_relay_lemma.md
rb4_internal_repeat_right_b_footprint_descent_lemma.md
```

R-b5 is a row-`b` recurrence on generated `A`-vertices.  This file records the
finite footprint split needed for a minimality argument.

## Setup

Consider a row-`b` chain on generated `A`-vertices:

```text
A_{i_0} -> A_{i_1} -> A_{i_2} -> ...
```

where every arrow means:

```text
b*A_{i_r}=A_{i_{r+1}}.
```

Equivalently, each step is a base bridge A-hit:

```text
D_{i_r}=A_{i_{r+1}}.
```

as recorded in:

```text
rb5_a_layer_cycle_base_bridge_relay_lemma.md
```

## First Repeat In The A-Layer

Because the generated A-layer under consideration is finite, the chain has a
first repeat:

```text
A_{i_m}=A_{i_n},
0 <= m < n.
```

with:

```text
A_{i_0},...,A_{i_{n-1}}
```

pairwise distinct.

If:

```text
m>0,
```

then the closed A-cycle:

```text
A_{i_m} -> A_{i_{m+1}} -> ... -> A_{i_{n-1}} -> A_{i_m}
```

has strictly smaller footprint than the old chain up to first repeat:

```text
n-m < n.
```

Thus an internal A-layer repeat gives a descent in A-layer footprint.

## Return To The Start

If:

```text
m=0,
```

then the selected chain is already a closed A-layer cycle:

```text
A_{i_0} -> ... -> A_{i_{n-1}} -> A_{i_0}.
```

This is the genuine R-b5 boundary: a closed chain of base row-b/generated
bridge A-hits.

Even here, the cycle is not fresh.  At every vertex:

```text
A_{i_r},
```

there is the same-input split:

```text
row b:       A_{i_r} -> A_{i_{r+1}},
row x_{i_r}: A_{i_r} -> b.
```

and the lifted pair in `H_{A_{i_r}}`:

```text
H_{i_r}    -> A_{i_{r+1}},
Beta_{i_r} -> b.
```

## Consequence

In a minimal clean external-bridge relay loop chosen to minimize the A-layer
base-bridge footprint, an internal R-b5 repeat is impossible as the first
unresolved recurrence because it gives a smaller A-layer cycle.

The remaining R-b5 obstruction is therefore the start-return case:

```text
m=0,
```

a minimal closed A-layer cycle of base-bridge A-hits.

The next proof step should compare the lifted beta-anchor pairs around this
minimal cycle.  A repeat of one lifted full ported interval in an independent
role would close by source reconstruction; otherwise the cycle must be merged
with the global minimal relay-cycle obstruction.
