# eq677 Repository Idea Notes

Date: 2026-06-21.

Source:

```text
https://github.com/memoryleak47/eq677
```

Status:

```text
external idea notes / not copied repo / not a proof
```

## What Was Inspected

Only the public repository metadata and small selected files were read:

```text
src/one_orbit.rs
src/one_orbit2.rs
src/analysis.rs
atp/cycle-sen.p
atp/no-self-producing-2-cycle.p
atp/no-self-producing-3-cycle.p
db/ directory listing
```

The repository was not cloned or imported wholesale.

## Useful Ideas

### 1. One-generated quotient search

`one_orbit.rs` and `one_orbit2.rs` search possible one-generated structures by
branching on compact term classes and checking consistency with Twee.

This is relevant to our bad target `b` only as a narrowing device:

```text
fix the one-generated right-h self-repeat cycle
and ask which term identifications are consistent with E677 and not-E255.
```

It is not yet a proof route by itself, because our current residual is not an
arbitrary one-generated magma; it has anchored rows `U,W,z,T,S,b` and fixed
target graph `H_h` data.

### 2. Model-wide short identity mining

`analysis.rs` converts a finite magma into an e-graph, intersects the
short-expression equalities over all substitutions of `X,Y`, and prints common
short identities.

The important detail is the unary operator:

```text
d(x)=((x*x)*x)
```

This is directly relevant because E255 is:

```text
d(x)*x=x.
```

Our earlier M496 scans around `U*h=W*h` checked mostly product-neighborhood
relations.  A next useful diagnostic should also scan short expressions
containing `d`, for example around:

```text
h,
U,
W,
z,
T=U*h,
S=W*h,
b=z*h.
```

The goal is not broad identity mining; it is to see whether the anchored
identity `U*h=W*h` has a shorter expression through `d` or through a
cycle-end term.

### 3. ATP self-producing cycle template

`atp/cycle-sen.p` models a self-producing row cycle by naming:

```text
start,
end,
next-to-last,
successor.
```

In its notation the shape is:

```text
a*a=s,
a*n=e,
a*e=a.
```

For our anchored-M7 residual, the analogous useful shape is:

```text
r_0*h=r_1,
r_{n-2}*h=r_{n-1},
r_{n-1}*h=r_0.
```

This is more promising than only testing the first fresh layer:

```text
T1=T*h,
S1=S*h,
B1=b*h.
```

because the residual is now a whole clean self-repeat cycle.

### 4. Database models

The `db/` directory includes many model sizes, including `496`.

This can support diagnostics, but it should not become broad model scraping.
The useful current check is narrow:

```text
verify the anchored-M7 self-repeat/cycle-end pattern on every available db
model that can be loaded cheaply,
then compare whether cycle-end terms force same-output fan, d-term collapse,
or watched/core hit.
```

## Action Taken

A permanent local diagnostic inspired by `analysis.rs` was created:

```text
tools/m496_anchored_d_term_scan.js
```

It scans the known M496 shared-step pairs and compares short expressions built
from:

```text
*, d(x)=((x*x)*x), and the named anchored terms
```

for the exact target:

```text
can U*h=W*h be explained by a shorter d-term or cycle-end identity?
```

The first result is recorded in:

```text
m496_anchored_d_term_scan_diagnostic.md
```

The strongest new hints are:

```text
d(h)=h,
h*h=h,
d(z)=z,
z*z=z,
z*d(h)=b,
d(z)*h=b.
```

Only after proving or rejecting these locally should we generalize from M496
to all `db/` models.
