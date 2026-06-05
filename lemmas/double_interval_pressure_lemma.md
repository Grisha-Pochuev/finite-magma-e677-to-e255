# Double Interval Pressure Lemma

Date: 2026-06-05.

Status:

```text
candidate / next main frontier
```

Purpose:

```text
Record the sharpened form of the pressure-diamond obstruction.
```

## Setup

Assume the main no-free-tail contradiction setup:

```text
t=r_2=b_2*0
t!=0
s=b_3
s*t=b_4.
```

The edge-triangle expansion of the origin edge gives:

```text
u_2=0*(t*b_2)
b_2*u_2=0
b_2*0=t
```

So row `b_2` contains the two-sided segment:

```text
u_2 -> 0 -> t.
```

The edge-triangle expansion of the offset edge gives:

```text
c_{-1}=t*(b_4*b_3)
b_3*c_{-1}=t
b_3*t=b_4
```

So row `b_3` contains the two-sided segment:

```text
c_{-1} -> t -> b_4.
```

## Main Observation

The nonzero value `t=r_2` is not a free tail point.  It is the common pivot of
two forced adjacent intervals:

```text
row b_2:  u_2     -> 0 -> t
row b_3:  c_{-1} -> t -> b_4
```

Together with row-`t` pressure:

```text
z_t=(b_2*t)*b_2
t*z_t=0
t*(b_4*b_3)=c_{-1}
```

and row-`b_4` pressure:

```text
p=(b_3*b_4)*b_3
b_4*p=t
b_4*r_3=b_5
```

this is stronger than the earlier one-sided or single-row orbit picture.

## Immediate Roles

The origin predecessor cannot be zero:

```text
u_2!=0
```

because row `b_2` sends:

```text
0 -> t
u_2 -> 0
```

and `t!=0`.

If:

```text
u_2=t,
```

then row `b_2` swaps:

```text
0 <-> t.
```

This is the origin self-swap role.

If:

```text
c_{-1}=0,
```

then row `t` has two zero outputs, so:

```text
b_4*b_3=z_t.
```

This is the backward-zero trap.

If:

```text
c_{-1}=b_4,
```

then row `b_3` swaps:

```text
t <-> b_4.
```

This is the offset self-swap role.

If:

```text
p=r_3,
```

then exactly:

```text
t=b_5.
```

So outside the special bridge offset `r_2=b_5`, row `b_4` has two distinct
occupied columns.

## Candidate Lemma

Proposed next main lemma:

```text
In a finite E677 magma, the double interval

  row b_2:  u_2     -> 0 -> t
  row b_3:  c_{-1} -> t -> b_4

cannot be extended with both predecessors staying completely fresh, while also
avoiding the row-t zero pressure and the row-b_4 occupied-column pressure.
```

If this is proved, the no-free-tail route becomes:

```text
t!=0
=> pressure diamond
=> double interval pressure
=> zero trap / self-swap / row collision / bad-cycle descent
=> contradiction
=> r_2=0
=> E255 for 0.
```

## Next Work

Do not start a broad finite search from this file.

The next useful step is symbolic:

```text
Classify the occupied roles of u_2:
  u_2=t      -> origin self-swap;
  u_2=b_j    -> row-b_j pressure/descent;
  u_2 fresh  -> a second fresh interval must be tracked together with c_{-1}.
```

The first computational check, if needed later, should test only a fixed role,
not the full open search.
