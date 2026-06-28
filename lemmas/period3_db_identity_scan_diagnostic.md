# Period-3 db Identity Scan Diagnostic

Date: 2026-06-27.

Status:

```text
diagnostic / db identities are hints, not local E677 consequences
```

## Purpose

This follows the sharpened period-3 residual:

```text
z*h=b,
b*h=c,
c*h=z.
```

The question was whether the public `eq677` db period-3 examples have short
universal identities around the early bridge:

```text
H_b: h -> z*b,
H_c: h -> b*c.
```

If such identities were also derivable from the local E677 period-3 template,
they would be candidate lemmas.  If they only hold in the external db models,
they are hints but not proof steps.

## Script

```text
tools/period3_db_identity_scan.js
```

The script filters to the same strict residual as:

```text
tools/eq677_db_shared_step_scan.js
```

namely clean first source-orbit self-repeat cases with signature:

```text
z:3->0
```

and clean period-3 target advance.

## Result

Run:

```text
tools\node-portable\node.exe tools\period3_db_identity_scan.js
```

Result:

```text
totalPeriod3Clean: 6240
77/65: 1560
77/71: 1560
77/72: 1560
77/73: 1560
```

All strict clean period-3 examples are in the four non-idempotent size-77
models.

## Universal db Identities

The db examples have several universal short identities beyond the defining
zipper equations.  The most interesting ones are:

```text
h*h = z*b
h*alpha = b
h*Ib = c*z
alpha*(z*b) = h
b*(c*z) = Ic
(b*c)*z = c
(c*z)*Ic = z*b
Ib*c = z
Ib*h = c
Ic*z = Ib
z*Ib = Ic
```

There are also universal idempotent hits for some displayed derived values:

```text
(c*z)*(c*z)=c*z
T*T=T
S*S=S
```

and, as expected for the external `eq677` db, E255 holds for all displayed
named values in these examples.

## Local Closure Check

The same candidate identities were added to:

```text
tools/period3_zipper_saturation.js
```

and checked by:

```text
tools\node-portable\node.exe tools\period3_zipper_saturation.js 5 12 1000000
```

None of the db-only identities above were derived by the local period-3 E677
closure.  In particular, depth 5 still does not derive:

```text
h*h=z*b,
h*alpha=b,
h*Ib=c*z,
alpha*(z*b)=h,
z*Ib=Ic.
```

The same script now accepts extra assumptions:

```text
--assume=hhZB
--assume=hAlphaB
--assume=hIbCZ
...
```

Each single db fingerprint was tested as an added local hypothesis at depth 4.
No single fingerprint caused:

```text
clean forbidden collapse,
E255(z), E255(b), E255(c), E255(h),
or displayed idempotence.
```

The full size-77 fingerprint package was also tested:

```text
--assume=hhZB,hAlphaB,hIbCZ,alphaZBH,bCZIc,BCzc,CZIcZB,IbcZ,Ibhc,IczIb,zIbIc
```

At depth 4 this package is still locally clean-consistent and still does not
derive:

```text
E255(z), E255(b), E255(c), E255(h),
z*z=z, b*b=b, c*c=c, h*h=h.
```

## Interpretation

These short identities are useful model fingerprints, but they should not be
promoted to E677 lemmas without an extra hypothesis.  They may be consequences
of the fact that the public db models already satisfy E255, or of additional
global structure absent from the local period-3 template.

Even taken as an added fingerprint package, they do not give an immediate
local period-3 closure in the bounded saturation.  So the next proof target
should not be "prove one db fingerprint and then close locally" unless a new
argument shows why that fingerprint interacts with the global relay measure.

The next proof step should therefore stay on the measure/admissibility route:

```text
prove the shifted-window bridge H_b,H_c is admissible as a smaller relay/V3
object, or identify the missing global hypothesis that forces one of the db
fingerprint identities.
```
