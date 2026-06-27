# R-b4 First-Repeat Target-Swap Relay Lemma

Date: 2026-06-19.

Status:

```text
proved reduction / R-b4 recurrence relays by first-merge target swap
```

## Purpose

This attacks the first item from:

```text
same_row_recurrence_inventory.md
clean_external_bridge_to_relay_recurrence_frontier.md
```

namely:

```text
R-b4. closed right-b cycle / first repeat of the right-b orbit.
```

The point is that the first repeat is not merely a same-row recurrence.  It is
a genuine first merge in `H_b` with an automatic outgoing continuation, so it
relays by:

```text
first_merge_target_swap_junction_dichotomy.md
```

## Setup

Use the right-`b` orbit:

```text
x_{n+1}=x_n*b,
A_n=pred_{x_n}(b),
x_n*A_n=b.
```

Assume the first repeat is:

```text
x_i=x_j=v,
0<i<j,
```

and set:

```text
y=x_{i-1},
z=x_{j-1}.
```

Then:

```text
y*b=v,
z*b=v.
```

By firstness of the repeat:

```text
y!=z.
```

Thus rows `y` and `z` give a genuine incoming merge at `v` in `H_b`:

```text
A_{i-1} -> v,
A_{j-1} -> v.
```

The two inputs are distinct; otherwise the ordered two-step interval:

```text
A_{i-1} -> b -> v
```

would reconstruct the same source row and force:

```text
y=z.
```

This is the fan already recorded in:

```text
right_b_orbit_first_repeat_fan_lemma.md
```

## Automatic Outgoing Continuation At v

Since:

```text
v=x_i,
A_i=pred_v(b),
```

we have:

```text
v*A_i=b.
```

Therefore row `A_i` contributes an `H_b` edge starting at `v`:

```text
v -> m,
```

where:

```text
m=A_i*b.
```

So the first repeat is not a pure incoming sink.  It is a first merge with an
outgoing continuation.

If:

```text
A_i=v,
```

then this is the self-source/fixed local repeat boundary already listed in:

```text
right_b_orbit_local_repeat_roles.md
```

So the clean R-b4 branch may assume:

```text
A_i!=v.
```

## Target-Swap Relay

Apply:

```text
first_merge_target_swap_junction_dichotomy.md
```

to the first merge:

```text
y*b=v,
z*b=v,
```

with outgoing continuation:

```text
A_i*v=b,
A_i*b=m.
```

After swapping target:

```text
b -> v,
```

the two merging rows become an outgoing fan at `b` in `H_v`:

```text
b -> y*v,
b -> z*v,
```

with distinct tips.

The continuation row `A_i` gives:

```text
target v,
source A_i.
```

If:

```text
m!=v,
```

the swapped object is a mixed `2+1` junction.

If:

```text
m=v,
```

the continuation is a loop and the swapped object is an outgoing triple fan at
`b` in `H_v`.

## Consequence

R-b4 is not an independent recurrence obstruction.

It relays to one of the standard local junction types:

```text
mixed 2+1 junction,
or outgoing triple fan,
```

after target swap from `b` to the repeated vertex `v`.

The only remaining global issue is the usual relay-termination question:

```text
does this relayed junction attach to the old visible core, repeat a full
ported interval in an independent role, or produce a smaller clean external
bridge?
```

Thus R-b4 should be treated as part of the global No-Free-Tail recurrence
frontier, not as a separate clean external-bridge residual.
