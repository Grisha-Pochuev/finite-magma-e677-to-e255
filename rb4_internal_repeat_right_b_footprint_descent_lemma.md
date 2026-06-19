# R-b4 Internal Repeat Right-b Footprint Descent Lemma

Date: 2026-06-19.

Status:

```text
proved conditional descent / internal R-b4 repeat gives smaller right-b footprint
```

## Purpose

This strengthens:

```text
rb4_first_repeat_target_swap_relay_lemma.md
clean_external_bridge_to_relay_recurrence_frontier.md
```

It gives the concrete minimality measure for the R-b4 row-b recurrence:

```text
right-b orbit footprint before the first repeat.
```

## Setup

Use:

```text
x_0=a,
x_{n+1}=x_n*b.
```

Let the first repeat be:

```text
x_i=x_j=v,
0 <= i < j,
```

with all:

```text
x_0,x_1,...,x_{j-1}
```

pairwise distinct.

The old right-`b` footprint up to first repeat is:

```text
F_old={x_0,x_1,...,x_{j-1}}.
```

## Case i=0

If:

```text
i=0,
```

then the right-`b` orbit returns to the original crossed-fan vertex:

```text
x_j=x_0=a.
```

By:

```text
right_b_orbit_first_repeat_fan_lemma.md
```

this either enlarges the original incoming fan at `a` or hits one of the
visible selected source rows.  It is therefore a visible/core attachment
case, not a clean independent recurrence.

## Case i>0

If:

```text
i>0,
```

then the closed right-`b` cycle is:

```text
C={x_i,x_{i+1},...,x_{j-1}},
```

with:

```text
x_{j}=x_i.
```

This cycle is a proper subset of the old footprint:

```text
C proper-subset F_old,
```

because:

```text
x_0,...,x_{i-1}
```

are nonempty and cannot lie in `C` by firstness of the repeat.

Thus an internal R-b4 repeat has a strictly smaller right-`b` footprint:

```text
|C|=j-i < j=|F_old|.
```

## Relay Interpretation

The repeated vertex:

```text
v=x_i
```

creates an incoming merge in `H_b`, and:

```text
rb4_first_repeat_target_swap_relay_lemma.md
```

turns it into a standard target-swap relay.

The relayed junction is attached to the smaller cycle footprint `C`, not to
the entire old preperiod-plus-cycle footprint `F_old`.

## Consequence

In a minimal clean external-bridge relay loop chosen to minimize:

```text
the right-b first-repeat footprint length,
```

an internal R-b4 repeat cannot be the first unresolved clean recurrence unless
one of the following already happened:

```text
1. visible/core attachment;
2. independent full ported-interval collision;
3. the relayed junction is not admissible as a new clean external bridge;
4. the recurrence is the global same-row relay obstruction rather than a
   fresh clean external-bridge branch.
```

So R-b4 provides a real descent measure for the clean external bridge route.
What remains is to integrate this measure with the global relay-cycle
minimality used in:

```text
minimal_relay_cycle_dichotomy_candidate.md
```

