# Period-3 Clean Anchored Profile Diagnostic

Date: 2026-06-28.

Status:

```text
diagnostic / clean anchored-X3 input already forces the named profile in db
```

## Purpose

This sits between:

```text
period3_all_cycles_Ibc_scan_diagnostic.md
period3_m7_witness_named_profile_diagnostic.md
```

The all-cycles scan showed that a bare right-`h` period-3 cycle does not force:

```text
Ib*c=z.
```

The M7-witness scan showed that the full M7 residual does force it in all
cached db examples.  This diagnostic tests the intermediate question:

```text
is the clean shared-step / anchored-X3 input already enough?
```

## Script

```text
tools/period3_clean_triple_identity_scan.js
```

It scans every cached model for strict period-3 cycles:

```text
z*h=b,
b*h=c,
c*h=z,
```

which admit a clean anchored-X3 shared-step triple:

```text
p*b=q*b=z,
U=p*z,
W=q*z,
U*p=W*q=h,
U*h=T,
W*h=S,
T!=S,
```

with clean inputs and outputs in `H_h`:

```text
row U: p     -> T,
row W: q     -> S,
row z: alpha -> b.
```

## Result

Run:

```text
tools\node-portable\node.exe tools\period3_clean_triple_identity_scan.js
```

Summary:

```text
cleanTriples:      13200
cleanTripleCycles:   240
models: 77/65, 77/71, 77/72, 77/73
examplesWithoutAIbcz: []
```

All `13200` strict clean anchored-X3 period-3 triples have the full named
profile:

```text
Ib*c=z,
(Ib*c)*Ib=Ic,
c*((Ib*c)*Ib)=h,
Ib*h=c,
z*Ib=Ic.
```

Equivalently, with:

```text
A=Ib*c,
K=A*Ib,
L=c*K,
```

the universal named equalities are:

```text
A=z,
K=Ic,
L=h.
```

The scan also found universal anchored-layer fingerprints:

```text
p*c=T,
q*c=S,
U*z=Ib,
W*z=Ib.
```

These occur both in clean M7 witnesses and in clean triples whose first event
routes earlier.

## Contrapositive Shared-Step Check

The companion scan:

```text
tools/period3_shared_step_dirty_reason_scan.js
```

checks strict period-3 shared-step false-branch candidates before separating
clean and dirty anchored-X3 triples.

Run:

```text
tools\node-portable\node.exe tools\period3_shared_step_dirty_reason_scan.js
```

Result:

```text
candidates:              13200
clean:                   13200
dirty:                       0
candidatesWithoutAIbcz:      0
```

Thus, in the cached db, every strict period-3 shared-step false-branch
candidate is already clean and already has the named profile.  No candidate
with:

```text
Ib*c!=z
```

appears even before applying the clean-triple filter.

## Negative Local Check

The same candidate equalities were added to:

```text
tools/anchored_period3_saturation.js
```

Depth-4 and depth-5 local closure from the anchored period-3 equations did not
derive:

```text
Ib*c=z,
(Ib*c)*Ib=Ic,
c*((Ib*c)*Ib)=h,
Ib*h=c,
z*Ib=Ic.
```

The depth-4 checks also did not derive `Ib*c=z` after adding the single or
combined db fingerprints:

```text
U*z=Ib,
p*c=T,
U*z=Ib and W*z=Ib,
p*c=T, q*c=S, U*z=Ib, W*z=Ib.
```

So the profile is not currently visible as a short local term-rewrite
consequence of the displayed equations.

## Rawmodel Warning

A stronger raw-label diagnostic was attempted with distinct labels for:

```text
z,h,b,c,p,q,U,W,T,S,alpha,Ib,A
```

and constraints:

```text
p*b=q*b=z,
p*z=U,
q*z=W,
U*p=W*q=h,
z*h=b,
b*h=c,
c*h=z,
z*alpha=h,
U*h=T,
W*h=S,
b*Ib=h,
Ib*c=A,
A distinct from z.
```

Both size-13 `rawmodeldiagnose` and `rawclosure` attempts exhausted the Node
heap before producing a mathematical contradiction or a model.  This is not
evidence either way; it only says that the generic rawmodel route is currently
too expensive for this labelled template.

## Interpretation

The best new theorem target is stronger and cleaner than the previous
M7-only statement:

```text
strict period-3 cycle + shared-step anchored false branch
=> Ib*c=z, K=Ic, L=h, Ib*h=c, z*Ib=Ic.
```

This would immediately close the M7 residual, because `Ib*c=z` is a watched
output hit for the `c`-input V3 branch and `Ib*h=c` gives the named fan.

The proof should not try to prove the named profile from the bare period-3
zipper alone.  It must use the clean anchored-X3 input as a whole: the two
rows `U,W`, their shared target `h`, and the clean triple in `H_h`.

## Next Structural Question

Assume a strict period-3 cycle comes from a shared-step anchored false branch
and suppose:

```text
A=Ib*c != z.
```

Then the db says no cached example survives.  The proof should show that this
assumption forces one of the forbidden clean-triple events:

```text
input-output hit,
input repeat,
output merge,
source hit,
or a watched/core attachment.
```

The most promising concrete bridge is to derive one of:

```text
U*z=Ib,
W*z=Ib,
p*c=T,
q*c=S,
```

from the clean triple and then use the two-row structure, not a single local
fingerprint, to force the named period-3 profile.
