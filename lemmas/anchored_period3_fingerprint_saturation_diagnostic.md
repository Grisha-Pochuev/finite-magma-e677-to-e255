# Anchored Period-3 Fingerprint Saturation Diagnostic

Date: 2026-06-27.

Status:

```text
diagnostic / anchored db fingerprints do not locally close period-3
```

## Purpose

The strict period-3 db examples have universal identities that reconnect the
period-3 zipper to the original anchored-X3 layer:

```text
p*c=T,
q*c=S,
U*z=Ib,
W*z=Ib.
```

Here:

```text
p*b=q*b=z,
p*z=U,
q*z=W,
U*p=W*q=h,
U*h=T,
W*h=S,
z*h=b,
b*h=c,
c*h=z.
```

The question was whether these identities follow from the local anchored
period-3 E677 template, or at least close the template when assumed.

## Script

```text
tools/anchored_period3_saturation.js
```

It encodes:

```text
E677,
left cancellation,
edge predecessor formula,
fixed-target source-successor formula,
anchored-X3 false branch,
period-3 z-orbit,
period-3 zipper formulas.
```

It tests the db fingerprints:

```text
p*c=T,
q*c=S,
U*z=Ib,
W*z=Ib,
U*z=W*z.
```

It also tests the local routed-hit conditions for the shifted-window bridge:

```text
H_b: h -> ZB=z*b,
H_c: h -> BC=b*c,
```

and then for the full period-3 target-advanced triangle:

```text
H_z: h -> CZ=c*z,
H_b: h -> ZB=z*b,
H_c: h -> BC=b*c.
```

It also tests the target-lift triangle in `H_h`:

```text
alpha -> b,
Ib    -> c,
Ic    -> z.
```

The checked hits are:

```text
ZB=BC,
ZB=CZ,
BC=CZ,
h in {ZB,BC,CZ},
alpha/Ib/Ic input hits,
input-output cross hits among alpha->b, Ib->c, Ic->z,
ZB,BC,CZ hitting one of z,b,c.
```

## Runs

Base run:

```text
tools\node-portable\node.exe tools\anchored_period3_saturation.js 4 12 500000
```

Result:

```text
clean-consistent-in-closure: true
p*c=T: false
q*c=S: false
U*z=Ib: false
W*z=Ib: false
U*z=W*z: false
shifted bridge output hit ZB=BC: false
triangle output hit ZB=CZ: false
triangle output hit BC=CZ: false
shifted bridge input-output hit h=ZB: false
shifted bridge input-output hit h=BC: false
triangle input-output hit h=CZ: false
lift input hit alpha=Ib: false
lift input hit alpha=Ic: false
lift input hit Ib=Ic: false
lift cross hit alpha=c: false
lift cross hit Ib=b: false
other lift/source and lift cross hits: false
ZB/BC/CZ hits source z/b/c: false
E255(b): false
E255(z): false
E255(c): false
E255(h): false
```

Fingerprint-package run:

```text
tools\node-portable\node.exe tools\anchored_period3_saturation.js 4 12 500000 --assume=pcT,qcS,UzIb,WzIb
```

Result:

```text
clean-consistent-in-closure: true
p*c=T: true
q*c=S: true
U*z=Ib: true
W*z=Ib: true
U*z=W*z: true
shifted bridge output hit ZB=BC: false
triangle output hit ZB=CZ: false
triangle output hit BC=CZ: false
shifted bridge input-output hit h=ZB: false
shifted bridge input-output hit h=BC: false
triangle input-output hit h=CZ: false
lift input hit alpha=Ib: false
lift input hit alpha=Ic: false
lift input hit Ib=Ic: false
lift cross hit alpha=c: false
lift cross hit Ib=b: false
other lift/source and lift cross hits: false
ZB/BC/CZ hits source z/b/c: false
E255(b): false
E255(z): false
E255(c): false
E255(h): false
```

No forbidden clean collapse was derived in either run:

```text
T=S,
b=z,
b=c,
z=c,
h in {z,b,c},
alpha/Ib/Ic input collapse,
ZB/BC/CZ output collapse.
```

## Interpretation

The anchored size-77 fingerprints are not local E677 consequences of the
anchored period-3 template at this bounded depth.  Even if they are assumed
together, they do not locally force:

```text
T=S,
E255(b),
or a visible clean endpoint collapse.
```

So the db pattern:

```text
p*c=T,
q*c=S,
U*z=W*z=Ib
```

is useful evidence of extra structure in the public models, but it should not
be treated as a direct local closure route.

The sharper shifted-window and full-triangle tests also stay clean.  In
particular the bridge

```text
H_b: h -> z*b,
H_c: h -> b*c
```

and the full triangle

```text
H_z: h -> c*z,
H_b: h -> z*b,
H_c: h -> b*c
```

do not locally collapse by same output, input-output hit, lift-triangle hit,
or visible source hit, even after the db fingerprints are assumed.  This
supports the interpretation that the remaining obstruction is genuinely the
global admissibility/measure issue, not a missing one-step local collision.

The active proof target remains:

```text
admissibility of the shifted-window V3 bridge H_b,H_c under the global
minimality/relay measure.
```
