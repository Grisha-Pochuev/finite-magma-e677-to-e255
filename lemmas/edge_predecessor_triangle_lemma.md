# Edge Predecessor Triangle Lemma

Date: 2026-06-04.

Status:

```text
proved E677 consequence / candidate pressure-expansion tool
```

Purpose:

```text
Show that every known edge creates two adjacent forced predecessor edges.
This strengthens the source-orbit zipper into a pressure-expansion mechanism.
```

## Statement

In a finite E677 magma, suppose:

```text
a*z=c.
```

Then E677 gives two forced predecessor edges.

First, using E677 with:

```text
x=z
y=a
```

we get:

```text
z = a*(z*((a*z)*a)).
```

Since:

```text
a*z=c,
```

this becomes:

```text
z = a*(z*(c*a)).
```

So row `a` has:

```text
a*(z*(c*a))=z.
```

Second, using E677 with:

```text
x=c
y=a
```

we get:

```text
c = a*(c*((a*c)*a)).
```

But row `a` is injective and:

```text
a*z=c.
```

Therefore:

```text
z = c*((a*c)*a).
```

So row `c` has:

```text
c*((a*c)*a)=z.
```

Thus every edge:

```text
a*z=c
```

creates the triangle:

```text
a*z=c
a*(z*(c*a))=z
c*((a*c)*a)=z.
```

## Noncollision Consequence

If:

```text
z != c,
```

then:

```text
z*(c*a) != z.
```

Otherwise row `a` would send the same column `z` to both:

```text
c
z.
```

So a nontrivial edge forces a genuinely different predecessor column in row
`a`.

There is also a useful three-role split for:

```text
h=z*(c*a).
```

Since:

```text
a*h=z
a*z=c,
```

we have:

```text
h=z:
  impossible when z!=c;

h=c:
  row a swaps z and c:
    a*z=c
    a*c=z;

h fresh:
  row a now has a longer predecessor chain
    h -> z -> c.
```

So every nontrivial edge immediately becomes either:

```text
forbidden;
self-swap;
or pressure-expanding.
```

This mirrors the old local split between immediate contradiction, self-loop /
self-swap boundary, and longer relay tail.

## Source-Orbit Interpretation

For a source orbit:

```text
s*c_i=c_{i+1},
```

the first predecessor edge is:

```text
s*(c_i*(c_{i+1}*s))=c_i.
```

Since row `s` already sends:

```text
c_{i-1} -> c_i,
```

injectivity gives the usual zipper:

```text
c_i*(c_{i+1}*s)=c_{i-1}.
```

The second predecessor edge is:

```text
c_{i+1}*((s*c_{i+1})*s)=c_i,
```

which is the next zipper tooth:

```text
c_{i+1}*(c_{i+2}*s)=c_i.
```

So the source-orbit zipper is just repeated edge-triangle propagation along
the row `s` orbit.

## Zipper-Tooth Expansion

Now apply the same triangle to one zipper tooth:

```text
c_i*d_i=c_{i-1},
```

where:

```text
d_i=c_{i+1}*s.
```

The triangle gives:

```text
c_i*(d_i*(c_{i-1}*c_i))=d_i
c_{i-1}*((c_i*c_{i-1})*c_i)=d_i.
```

So a single zipper tooth forces two more edges:

```text
row c_i sends a new predecessor column to d_i;
row c_{i-1} sends a triangle column to d_i.
```

This is stronger than the basic zipper.  A free prefix must now keep fresh:

```text
forward values c_i;
zipper columns d_i=c_{i+1}*s;
second-predecessor columns d_i*(c_{i-1}*c_i);
triangle columns (c_i*c_{i-1})*c_i.
```

## Candidate Pressure-Expansion Form

The No-Free-Tail proof can aim for the following sharper statement:

```text
A no-bridge offset prefix cannot keep the whole edge-triangle expansion fresh.
Every nontrivial zipper tooth creates new row pressure in two adjacent rows.
In a finite bad-cycle normalization, this expansion must eventually collide
with an occupied row/column or descend to an older bad-cycle parameter.
```

This is not yet a termination proof, but it is the strongest local expansion
mechanism currently extracted from E677.
