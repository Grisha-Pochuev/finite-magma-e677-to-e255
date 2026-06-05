# Source-Orbit Zipper Lemma

Date: 2026-06-04.

Status:

```text
proved consequence of the source-orbit ladder / candidate termination tool
```

Purpose:

```text
Package a zero-avoiding source-orbit prefix as a forward orbit plus a backward
relay zipper.  This is the current best form of compact prefix-collapse.
```

This refines:

```text
source_orbit_ladder_lemma.md
offset_source_orbit_first_return_lemma.md
first_return_row_pressure_lemma.md
```

## General Zipper

Let row `s` have a source-orbit prefix:

```text
c_0 -> c_1 -> c_2 -> ... -> c_n
```

meaning:

```text
s*c_i=c_{i+1}
```

for `0<=i<n`.

For every interior point `c_i`, with `1<=i<n`, the source-orbit ladder gives:

```text
c_i*(c_{i+1}*s)=c_{i-1}.
```

So the forward source orbit automatically creates a backward relay zipper:

```text
c_1*(c_2*s)=c_0
c_2*(c_3*s)=c_1
c_3*(c_4*s)=c_2
...
c_{n-1}*(c_n*s)=c_{n-2}.
```

This is a direct consequence of finite E677 through the inverse-edge chain.

## Offset Zipper

For the offset orbit:

```text
s=b_3
c_0=r_2=b_t
c_1=b_4
c_{i+1}=s*c_i
```

the first zipper edge is:

```text
b_4*(c_2*s)=r_2.
```

With:

```text
c_2=b_3*b_4
p=c_2*b_3,
```

this is exactly:

```text
b_4*p=r_2.
```

Thus the old offset relay is the first tooth of the zipper.

## First-Return Zipper

Suppose the offset orbit first returns to the occupied block at:

```text
c_n=b_j.
```

If the prefix is a true first return, then:

```text
c_2, c_3, ..., c_{n-1}
```

are fresh relative to the occupied block.

The zipper gives:

```text
c_{n-1}*(b_j*s)=c_{n-2}
b_j*((s*b_j)*s)=c_{n-1}
```

where the second edge is the row-pressure edge from
`first_return_row_pressure_lemma.md`.

More generally, the whole fresh prefix is not free.  It is pinned backwards by
the relay columns:

```text
c_{i+1}*s.
```

## Role Split For A Zipped Prefix

A zero-avoiding zipped prefix can fail to remain free in four ways:

```text
1. It hits 0:
   the final zipper edge lands in row 0 and gives a pred0 value.

2. It repeats an earlier c_k:
   the forward orbit has a short source cycle, and the zipper gives reverse
   edges around the cycle.

3. It hits a bad-cycle element b_j:
   row b_j gets pressure in addition to b_j*r_{j-1}=b_{j+1}.

4. One zipper column c_{i+1}*s hits an already occupied column:
   injectivity in row c_i forces a collision or identifies the column with an
   older bad-cycle parameter.
```

The fourth role is the new point: even if the forward orbit values are fresh,
the backward zipper columns may not be fresh.

## Candidate Compact-Collapse Statement

The compact prefix-collapse needed for the main No-Free-Tail Lemma can now be
phrased as:

```text
In a no-bridge offset branch, a zero-avoiding source-orbit prefix cannot have
both:
  all forward values c_i fresh relative to the occupied bad-cycle block, and
  all zipper columns c_{i+1}*s fresh relative to the already occupied columns,
until the row-s orbit closes.
```

If this statement is proved, then every no-bridge orbit prefix terminates by:

```text
zero-hit;
short source cycle;
row-pressure descent;
or zipper-column collision.
```

This is the current sharpest form of the missing no-free-tail termination
lemma.

## Edge-Triangle Upgrade

Update 2026-06-04:

```text
edge_predecessor_triangle_lemma.md
```

Every known edge:

```text
a*z=c
```

also forces:

```text
a*(z*(c*a))=z
c*((a*c)*a)=z.
```

Apply this to a zipper tooth:

```text
c_i*d_i=c_{i-1}
d_i=c_{i+1}*s.
```

It gives:

```text
c_i*(d_i*(c_{i-1}*c_i))=d_i
c_{i-1}*((c_i*c_{i-1})*c_i)=d_i.
```

So every zipper tooth creates two more forced edges in adjacent rows.

The compact-collapse target is therefore stronger:

```text
A no-bridge prefix cannot keep fresh all of:
  forward values c_i;
  zipper columns d_i=c_{i+1}*s;
  second-predecessor columns d_i*(c_{i-1}*c_i);
  triangle columns (c_i*c_{i-1})*c_i.
```

This is the current strongest pressure-expansion form of the no-free-tail
mechanism.
