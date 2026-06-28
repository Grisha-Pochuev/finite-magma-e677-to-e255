# eq677 Repository Idea Notes

Date: 2026-06-25.

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
src/db.rs
src/autom_search.rs
src/load.rs
atp/cycle-sen.p
atp/no-self-producing-2-cycle.p
atp/no-self-producing-3-cycle.p
db/ directory listing
```

The repository was not cloned or imported wholesale.

Update 2026-06-25: refreshed after a narrower re-read of the same sources plus
`db.rs`, because the earlier M496 d-term hint is now known to be mostly an
idempotent-model artifact.

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

For the current `G12 / shared-step anchored triangle`, the useful translation
is not "search all one-generated magmas".  It is:

```text
fix the anchored equations
p*b=q*b=z,
U=p*z,
W=q*z,
h=U*p=W*q,
z*h=b,

then ask whether the one-generated bad-target component can keep
U*h != W*h without forcing a smaller V3 bridge or watched/core hit.
```

This is a narrowing template for the bad target `b`, not a replacement for the
current V3 admissibility proof.

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

However, M496 is idempotent:

```text
x*x=x,
d(x)=x.
```

So universal M496 relations such as `d(h)=h`, `d(z)=z`, or `d(U)*h=d(W)*h`
are not anchored-specific evidence.  They should be used only as a filter:
if a `d`-term identity also holds in non-idempotent `db` models, then it is
worth promoting to a proof target.

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

### 4. Database models and families

The `db/` directory includes many model sizes, including `496`.  In `db.rs`
the known models are also grouped into useful families:

```text
AFFINE_MODELS_13_3
GLUE5_MODELS
LINEAR_EXTENSIONS
TINV
```

This can support diagnostics, but it should not become broad model scraping.
The useful current check is narrow and family-aware:

```text
verify the shared-step anchored triangle / U*h=W*h / first-extra V3 roles
on the available db models,
then report whether failures or absences cluster by family:
affine, glue5, linear-extension, tinv, or the remaining interesting models.
```

This is stronger than checking only M496, because M496 is highly symmetric and
idempotent.  It is also cheaper than blind search, because it reuses existing
finite models as witnesses for or against candidate local identities.

### 5. Automorphism search

`autom_search.rs` computes automorphism groups of db models and uses them to
restrict later searches.

For our current residual this suggests a conservative optimization:

```text
when scanning all db models, quotient shared-step pairs by automorphisms
before checking anchored triangle roles.
```

This does not prove a lemma, but it can make the "all db models" check less
wasteful and may expose whether the anchored pattern is orbit-invariant rather
than an accident of chosen element names.

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

Those first d-term hints are now downgraded: in M496 they are explained by
global idempotence.  The better next use of the external repository is:

```text
build a small local db scanner, inspired by analysis.rs/db.rs, that checks
the shared-step anchored triangle and clean V3 roles across db families.
```

The first question for that scanner was:

```text
Does U*h=W*h hold in every available db model with shared-step pairs?
```

Result, recorded in `eq677_db_shared_step_scan_diagnostic.md`:

```text
No.  The full public db has 18348 false shared-step pairs,
including 17040 where all named terms b,z,p,q,U,W,h,T,S are distinct.
```

The false cases were also classified as anchored-X3 triples:

```text
17040 clean triples p,q,alpha -> T,S,b,
1308 visible routed triples.
```

So the unrestricted strong shared-step hypothesis is false.  The useful next
layer is no longer to prove it globally, but to ask:

```text
For every first failure branch forced syntactically by U*h!=W*h, does the
same db scan always route to same-output fan / generated input / watched hit?
```

Equivalently: can the extra bad-target/minimal-clean assumptions eliminate the
all-distinct db failures, or is anchored-X3/V3 admissibility genuinely needed?
