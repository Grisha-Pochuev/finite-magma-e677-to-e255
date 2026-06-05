# Senior Column Fallback Lemma

Date: 2026-05-25.

## Status

```text
candidate / relay fallback after no-bridge
```

Update 2026-05-25: this fallback has been generalized in:

```text
row6_orbit_relay_lemma.md
```

The senior-column formula is the first edge-pair in the row-6 orbit:

```text
6*8=m
6*m=r
=> m*(r*6)=8
```

The more general form is:

```text
6*z0=z1
6*z1=z2
=> z1*(z2*6)=z0
```

This file records the fallback mechanism after `marker_bridge_transfer_lemma.md`.

The bridge-transfer branch is conditional:

```text
a*t=5
a*5=6
=> 6*a=s*6
```

But pair-forbid diagnostics showed that no-bridge branches remain alive for
`t=2` and `t=3`.  In those branches, the next stable marker is:

```text
6*8 = 6*b1
```

## General Relay

In `case45`:

```text
b1=8
b3=6
```

Assume:

```text
6*8=m
```

Use the inverse edge chain:

```text
a*z=c  ==>  z = c*((a*c)*a)
```

with:

```text
a=6
z=8
c=m
```

Then:

```text
8 = m*((6*m)*6)
```

Define:

```text
r=6*m
h=r*6
```

Then:

```text
m*h=8
```

So the senior-column fallback transfers pressure from row `6` to row `m`:

```text
6*8=m
6*m=r
r*6=h
m*h=8
```

## Special Case `m=0`

If:

```text
6*8=0
```

then:

```text
8 = 0*((6*0)*6)
```

Since row `0` is the full 9-cycle:

```text
0*7=8
```

we get:

```text
(6*0)*6=7
```

Thus, if:

```text
r=6*0
```

then:

```text
r*6=7
```

This explains why fixing the extra marker `6*0=r` strongly compresses the
`m=0` residue.

## Diagnostic Check

In the no-bridge branch for `t=2`:

```text
7*0=2
6*2=5
6*6=6
6*5=2
no bridge
6*8=0
```

the row-6 domain is:

```text
54
```

After fixing one relay value:

```text
6*0=3
```

the tool forced:

```text
3*6=7
```

and row `6` compressed further:

```text
row6 domain: 18
```

This is consistent with the manual relay:

```text
(6*0)*6=7
```

## Nonzero Representative

The same relay form also works when `m` is not zero.

Representative:

```text
t=2
no bridge
6*8=1
```

Then:

```text
r=6*1
h=r*6
1*h=8
```

A concrete check fixed:

```text
6*1=0
```

Since row `0` has:

```text
0*6=7
```

the relay predicts:

```text
1*7=8
```

The tool forced exactly that:

```text
row 1 req=[0->7, 7->8]
row 6 domain: 18
```

So the fallback is not special to `m=0`.  It really transfers pressure from
row `6` into row `m`.

## Zero-Relay Sublayer

A particularly strong subcase occurs when:

```text
r=6*m=0
```

Then:

```text
h=r*6=0*6=7
```

and the senior-column relay gives:

```text
m*7=8
```

So:

```text
6*8=m
6*m=0
=> m*7=8
```

This is the clean explanation for the representative `m=1, r=0` above.

Additional zero-relay diagnostics in the `t=2` no-bridge branch:

```text
m=0 -> contradiction
m=8 -> contradiction
m=1 -> alive, forces 1*7=8
m=3 -> alive, forces 3*7=8
```

Representative `m=3`:

```text
6*8=3
6*3=0
=> 3*7=8
row6 domain: 18
```

The remaining `m=4,7` were not separately enumerated after the same pattern was
seen; they should be treated as sanity checks only if a final finite
certificate is needed.

## Current Meaning

This is not yet a full closure of the no-bridge branch.

It is a structural replacement for the failed question "is a bridge forced?"

Current split:

```text
bridge branch:
  use 6*a=s*6

no-bridge branch:
  set m=6*b1
  use m*((6*m)*b3)=b1
```

For `m=0`, the known row `0` turns this into an immediate row constraint.
For other `m`, the relay transfers activity to row `m`, which should be the
next object to study instead of enumerating all row-6 candidates.
