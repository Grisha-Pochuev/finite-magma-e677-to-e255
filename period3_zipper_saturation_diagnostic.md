# Period-3 Zipper Saturation Diagnostic

Date: 2026-06-27.

Status:

```text
diagnostic / no short local collapse of clean period-3 zipper
```

## Purpose

This checks the sharpened period-3 residual from:

```text
fixed_target_period3_zipper_boundary.md
period3_zipper_triangle_self_renewal_lemma.md
```

The question was whether E677 plus the clean period-3 zipper equations already
forces a short visible collision, idempotence, or E255 for one of the displayed
vertices.

## Script

```text
tools/period3_zipper_saturation.js
```

It is a bounded ground-congruence diagnostic.  It is not a finite-model search
and not a proof.

The encoded period-3 residual is:

```text
z*h=b,
b*h=c,
c*h=z,

z*alpha=h,
b*Ib=h,
c*Ic=h,

alpha=h*(b*z),
Ib=h*(c*b),
Ic=h*(z*c),

z*b=ZB,
b*c=BC,
c*z=CZ.
```

It uses:

```text
E677,
left cancellation,
edge predecessor formula,
fixed-target source-successor formula,
shared-input collision consequence,
congruence for generated products.
```

## Runs

```text
tools\node-portable\node.exe tools\period3_zipper_saturation.js 4 12 250000
tools\node-portable\node.exe tools\period3_zipper_saturation.js 5 12 1000000
```

Depth 4:

```text
terms: 19364
closeRounds: 10
clean-consistent-in-closure: true
```

Depth 5:

```text
terms: 111878
closeRounds: 12
clean-consistent-in-closure: true
```

## Confirmed Zipper Equalities

Both runs derive the expected self-renewing zipper formulas:

```text
alpha=(c*z)*c,
Ib=(z*b)*z,
Ic=(b*c)*b,

b*((z*b)*z)=h,
c*((b*c)*b)=h,
z*((c*z)*c)=h.
```

These are exactly the cyclic shift recorded in:

```text
period3_zipper_triangle_self_renewal_lemma.md
```

## Non-Derived Local Closures

No clean forbidden collapse was derived among:

```text
z,b,c,h,
alpha,Ib,Ic,
ZB=z*b, BC=b*c, CZ=c*z.
```

In particular, the depth-5 run did not derive:

```text
ZB=BC, ZB=CZ, BC=CZ,
ZB in {z,b,c},
BC in {z,b,c},
CZ in {z,b,c}.
```

It also did not derive:

```text
E255(z), E255(b), E255(c), E255(h),
z*z=z, b*b=b, c*c=c, h*h=h.
```

After the db identity scan, several size-77 universal fingerprints were also
tested locally:

```text
h*h=z*b,
h*alpha=b,
h*Ib=c*z,
alpha*(z*b)=h,
z*Ib=Ic.
```

The depth-5 local closure did not derive any of these either.  See:

```text
period3_db_identity_scan_diagnostic.md
```

## Interpretation

The clean period-3 zipper is locally stable under the currently encoded short
E677 consequences.  The local pressure does not produce a short endpoint
collision, idempotence, or direct E255 proof.

So the next proof step should not be another guessed equality inside:

```text
z,b,c,h,alpha,Ib,Ic,ZB,BC,CZ.
```

The meaningful remaining exits are:

```text
1. prove the earlier adjacent bridge H_b,H_c is admissible as a smaller
   measured V3/relay object;
2. prove the clean self-renewing period-3 triangle is impossible in a minimal
   G12 loop for a global reason;
3. find a watched/core/full-interval attachment not visible in this local
   closure.
```
