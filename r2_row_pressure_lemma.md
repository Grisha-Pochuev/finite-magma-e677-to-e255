# R2 Row-Pressure Lemma

Date: 2026-06-04.

Status:

```text
proved pressure identities / candidate no-free-tail tool
```

Purpose:

```text
Use the fact that r_2 is not just an offset value.  It is itself produced by
the bad-cycle edge b_2*0=r_2, so row r_2 already has a forced zero edge.
The backward offset point adds a second forced edge in the same row.
```

This continues:

```text
two_sided_offset_orbit_lemma.md
edge_predecessor_triangle_lemma.md
```

## Setup

Let:

```text
t=r_2=b_2*0
s=b_3
s*t=b_4.
```

The two-sided offset orbit gives:

```text
c_{-1}=t*(b_4*s)
s*c_{-1}=t.
```

## Row `t` Already Has A Zero Edge

Apply the edge predecessor triangle to:

```text
b_2*0=t.
```

The second predecessor edge is:

```text
t*((b_2*t)*b_2)=0.
```

Define:

```text
z_t=(b_2*t)*b_2.
```

Then:

```text
t*z_t=0.
```

So row `t=r_2` already has a forced zero output.

## Backward Offset Gives A Second Row-`t` Edge

The backward offset point is:

```text
c_{-1}=t*(b_4*s).
```

Define:

```text
q_t=b_4*s.
```

Then row `t` has:

```text
t*q_t=c_{-1}.
```

Thus row `t` has two forced edges:

```text
t*z_t=0
t*q_t=c_{-1}.
```

This is immediate row-pressure in the offset value itself.

## Consequences

If:

```text
c_{-1}=0,
```

then injectivity of row `t` gives:

```text
q_t=z_t.
```

This is the backward-zero case already identified as a source-row zero trap.

If:

```text
c_{-1}!=0,
```

then:

```text
q_t!=z_t.
```

So the backward offset point creates a genuinely second occupied output in row
`t`.

In particular, a completely fresh two-sided interval must keep:

```text
c_{-1} fresh and nonzero;
q_t=b_4*s distinct from z_t=(b_2*t)*b_2.
```

## Relation To The No-Free-Tail Target

The occupied edge:

```text
t -> b_4
```

in row `s=b_3` is now tied to row `t` by two independent pressures:

```text
bad-cycle origin:
  b_2*0=t
  => t*z_t=0

two-sided offset predecessor:
  c_{-1}=t*(b_4*s)
  => t*q_t=c_{-1}.
```

So a fresh two-sided interval around:

```text
t -> b_4
```

cannot be studied only inside row `s`.  It must also keep row `t` from
colliding with its already forced zero edge.

This is a stronger local obstruction to a free no-bridge tail.

