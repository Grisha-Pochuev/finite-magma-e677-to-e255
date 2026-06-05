# First-Return Row-Pressure Lemma

Date: 2026-06-04.

Status:

```text
candidate / symbolic pressure lemma
```

Purpose:

```text
Make the "first return to the occupied bad-cycle block" useful: a return to
b_j creates a new forced edge in row b_j, where the bad-cycle ladder already
has a forced edge.
```

This continues:

```text
offset_source_orbit_first_return_lemma.md
main_bad_cycle_no_free_tail_lemma.md
```

## Setup

Let:

```text
s=b_3
c_{i+1}=s*c_i
```

be the source orbit from the offset edge:

```text
c_0=r_2=b_t
c_1=b_4.
```

The source-orbit relay says:

```text
c_i*(c_{i+1}*s)=c_{i-1}
```

for every `i>=1`.

Now suppose the orbit first returns to a bad-cycle element:

```text
c_i=b_j.
```

Then the relay gives:

```text
b_j*(c_{i+1}*s)=c_{i-1}.
```

But independently, the bad-cycle predecessor ladder already gives:

```text
b_j*r_{j-1}=b_{j+1}.
```

So row `b_j` has two forced edges:

```text
b_j*r_{j-1}=b_{j+1}
b_j*(c_{i+1}*s)=c_{i-1}.
```

This is the row-pressure created by first return.

## Immediate Consequences

Because row `b_j` is injective:

If:

```text
c_{i-1}=b_{j+1}
```

then the two columns must be equal:

```text
c_{i+1}*s=r_{j-1}.
```

This is a descent to an older bad-cycle parameter.

If:

```text
c_{i-1}!=b_{j+1},
```

then row `b_j` is now occupied by two distinct forced outputs.  Any later
attempt to send a third known column to one of these outputs must collide by
injectivity.

Thus a first return is never neutral:

```text
first return to b_j
=> descent to r_{j-1} OR extra occupied edge in row b_j.
```

## True First Return Gives Fresh Output

If `c_i=b_j` is the first return to the occupied bad-cycle block and `i>1`,
then:

```text
c_{i-1}
```

is not in that occupied block.  In particular, if the occupied block contains
all bad-cycle elements, then:

```text
c_{i-1}!=b_{j+1}.
```

So the first return usually does not immediately identify:

```text
c_{i+1}*s=r_{j-1}.
```

Instead it creates a genuinely new occupied edge in row `b_j`:

```text
b_j*(c_{i+1}*s)=c_{i-1}
```

whose output is fresh relative to the bad-cycle block.

Therefore the first-return mechanism has two stages:

```text
first return:
  creates row-pressure in row b_j;

later pressure/collision:
  must either reuse an occupied output and force descent,
  or keep adding fresh occupied outputs in finitely many rows.
```

The next proof obligation is exactly to rule out the second possibility as an
indefinite process.

## Special Case: Return To 0

If:

```text
c_i=0
```

then the relay is:

```text
0*(c_{i+1}*s)=c_{i-1}.
```

Since row `0` is the known bad-cycle row:

```text
c_{i+1}*s=pred0(c_{i-1}).
```

This is the zero-hit role already used throughout the local closures.

## Special Case: Return To `b_4`

A return to `b_4` before returning to `c_0=r_2` is impossible.

Reason:

```text
s*c_0=b_4.
```

Since row `s` is injective, the unique predecessor of `b_4` in row `s` is
`c_0`.  Therefore if:

```text
s*c_{i-1}=b_4,
```

then:

```text
c_{i-1}=c_0.
```

So the orbit has already returned to its start.

## Special Case: Immediate Hit Of `s`

If:

```text
c_2=s,
```

then:

```text
s*c_0=b_4
s*b_4=s.
```

So row `s` is a bridge row for the offset:

```text
a=s.
```

Therefore this case is excluded in the no-bridge branch.

## Candidate Termination Form

The first-return part of the No-Free-Tail Lemma can now be stated as:

```text
The offset source orbit
  c_0=r_2, c_1=b_4, c_{i+1}=b_3*c_i
cannot first return to the bad-cycle block without creating either
  (1) a pred0 zero-hit descent,
  (2) a descent to an older r_{j-1},
  (3) an occupied-row pressure in row b_j, or
  (4) a bridge/self-return case already split off.
```

The remaining proof obligation is to show that repeated occupied-row pressure
cannot persist indefinitely without causing a collision in a finite magma.
