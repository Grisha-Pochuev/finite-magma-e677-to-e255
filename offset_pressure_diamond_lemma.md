# Offset Pressure Diamond Lemma

Date: 2026-06-04.

Status:

```text
proved pressure identities / candidate main-lemma framework
```

Purpose:

```text
Package the two defining edges around a nonzero offset r_2 into a four-row
pressure diamond.
```

This combines:

```text
r2_row_pressure_lemma.md
offset_relay_template_for_main_lemma.md
edge_predecessor_triangle_lemma.md
```

## Setup

Let:

```text
t=r_2=b_2*0
s=b_3
s*t=b_4.
```

The two defining edges are:

```text
b_2*0=t
s*t=b_4.
```

## Triangle Of The Origin Edge

Apply the edge predecessor triangle to:

```text
b_2*0=t.
```

It gives:

```text
b_2*(0*(t*b_2))=0
t*((b_2*t)*b_2)=0.
```

Define:

```text
u_2=0*(t*b_2)
z_t=(b_2*t)*b_2.
```

Then:

```text
b_2*0=t
b_2*u_2=0
t*z_t=0.
```

So:

```text
row b_2 has outputs t and 0;
row t has output 0.
```

Since `t!=0`, row `b_2` injectivity gives:

```text
u_2!=0.
```

## Triangle Of The Offset Edge

Apply the edge predecessor triangle to:

```text
s*t=b_4.
```

It gives:

```text
s*(t*(b_4*s))=t
b_4*((s*b_4)*s)=t.
```

Define:

```text
c_{-1}=t*(b_4*s)
p=(s*b_4)*s.
```

Then:

```text
s*t=b_4
s*c_{-1}=t
b_4*p=t.
```

So:

```text
row s=b_3 has outputs b_4 and t;
row b_4 has output t.
```

## The Pressure Diamond

The nonzero offset creates the following forced pattern:

```text
row b_2:
  0   -> t
  u_2 -> 0

row t=r_2:
  z_t -> 0
  b_4*s -> c_{-1}

row s=b_3:
  t      -> b_4
  c_{-1} -> t

row b_4:
  p -> t
```

Additionally, the bad-cycle ladder gives:

```text
b_4*r_3=b_5.
```

So row `b_4` actually has:

```text
b_4*p=t
b_4*r_3=b_5.
```

This is the offset pressure diamond.

## Immediate Collisions And Roles

If:

```text
c_{-1}=0,
```

then row `t` has:

```text
t*z_t=0
t*(b_4*s)=0,
```

so:

```text
b_4*s=z_t.
```

This is the backward-zero trap.

If:

```text
c_{-1}=b_4,
```

then:

```text
s*c_{-1}=s*b_4=t,
```

so row `s` swaps:

```text
t <-> b_4.
```

This is the self-swap role.

If:

```text
p=r_3,
```

then row `b_4` sends the same column to:

```text
t
b_5.
```

Thus:

```text
p=r_3 => t=b_5.
```

So unless the offset is exactly `b_5`, the columns `p` and `r_3` must be
distinct.

Conversely, if:

```text
t=b_5,
```

then row `0` is a bridge:

```text
0*b_5=b_4
0*b_4=s.
```

The bridge transfer gives:

```text
s*0=p.
```

But:

```text
r_3=s*0.
```

Therefore:

```text
t=b_5 => p=r_3.
```

So the row-`b_4` column coincidence is exactly the special bridge offset:

```text
p=r_3 <=> t=b_5.
```

outside that special offset, row `b_4` has two distinct occupied columns.

## Candidate Main-Lemma Form

A nonzero offset `r_2=t` cannot be a single free choice.  It immediately
creates a pressure diamond in four rows:

```text
b_2, t, b_3, b_4.
```

The current no-free-tail target can be restated as:

```text
No finite E677 magma can extend this pressure diamond into a fully fresh
two-sided row-b_3 interval without eventually triggering:
  backward-zero trap;
  self-swap;
  row-b_4 collision/descent;
  row-t zero collision;
  or a bad-cycle first-return pressure.
```
