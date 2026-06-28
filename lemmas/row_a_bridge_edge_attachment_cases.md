# Row-a Bridge Edge Attachment Cases

Date: 2026-06-18.

Status:

```text
general proved / local routing classification
```

## Setup

Fix a bad target `b` and a crossed-fan skeleton:

```text
p*a=b,  q*a=b,
p*b=c,  q*b=d,

r*b=a,  s*b=a,
r*a=u,  s*a=v.
```

Let:

```text
k=pred_a(b),
a*k=b,
t=a*b.
```

By:

```text
bad_target_crossed_fan_row_a_edge_lemma.md
bad_target_row_a_output_avoids_b_hub_lemma.md
row_a_bridge_loop_recurrence_boundary.md
```

row `a` gives a genuine `H_b` edge:

```text
k -> t,
```

with:

```text
k!=b,
t!=b.
```

Also:

```text
t!=h=pred_b(a).
```

If:

```text
t=k,
```

then row `a` gives the same-row recurrence loop:

```text
(b,k,k) -> (k,b,b) -> (b,k,k),
```

so this case is routed out of the clean external bridge branch.

## Classification

The edge `k -> t` has the following immediate local meanings.

### 1. `k=a`

Then:

```text
a*a=b.
```

So row `a` belongs to the outgoing fiber:

```text
F(a,b)={x:x*a=b}.
```

If row `a` is distinct from the already selected rows `p,q`, the outgoing fan
at `a` is enlarged to a triple fan.  If row `a` is one of `p,q`, this is a
same-source specialization rather than a new incidence.

### 2. `t=a`

Then:

```text
a*b=a.
```

So row `a` belongs to the incoming-side fiber:

```text
F(b,a)={x:x*b=a}.
```

If row `a` is distinct from `r,s`, the incoming side is enlarged to a triple
fan.  If row `a` is one of `r,s`, this is again a same-source specialization.

### 3. `k in {c,d}`

The row-`a` edge starts at one of the outgoing tips:

```text
c -> t
```

or:

```text
d -> t.
```

Thus it is a direct continuation/side incidence from the visible outgoing
fan footprint in `H_b`.

### 4. `t in {c,d}`

The row-`a` edge enters one of the outgoing tips:

```text
k -> c
```

or:

```text
k -> d.
```

This is a return into the visible outgoing fan footprint in `H_b`.

### 5. `k` or `t` in `{u,v}`

The row-`a` edge touches one of the target-swapped tips:

```text
u,v.
```

This is not automatically a local attachment inside the visible `H_b`
outgoing fan footprint, because `u,v` come from the opposite fan for the
swapped target pair:

```text
r*a=u,
s*a=v.
```

However, it is a two-target attachment.  Under the self-duality of the proper
crossed fan, `{u,v}` is the outgoing tip set on the swapped side.  Therefore
such a coincidence must be tracked in the two-target relay, not discarded as
unrelated.

### 6. None Of The Above

If:

```text
k,t not in {a,c,d,u,v},
```

then row `a` still supplies a real `H_b` edge, but this edge is external to the
immediate two-target fan footprint:

```text
a -> c,d
```

and:

```text
b -> u,v
```

on the swapped side.  It must be tracked as a genuinely external bridge edge.

## Boundary

This classification intentionally refers only to the immediately visible
outgoing fan footprint in `H_b`.

The incoming rows `r,s` are visible in `H_b` only through their actual `H_b`
inputs `A_b(r)` and `A_b(s)`, not through the target-swapped tips `u,v`.
Therefore coincidences with `u` or `v` are not automatically graph attachments
inside `H_b`; they are dual-footprint attachments in the two-target relay.

The value `t=h` is not a routing case: it is impossible for a bad target by
`bad_target_row_a_output_avoids_b_hub_lemma.md`.

The value `t=k` is also not part of the clean external bridge branch: it is
the same-row recurrence boundary recorded in
`row_a_bridge_loop_recurrence_boundary.md`.

## Diagnostic Note

Short bounded saturation checks with flags:

```text
k=a
k=c
k=d
ab=c
```

do not force a local collapse or a short right-fixer.  This supports the use
of the classification as routing information rather than as a direct closure.

By contrast, the flag:

```text
ab=h
```

does produce a short right-fixer of `b`, matching the proved exclusion
`a*b!=h`.
