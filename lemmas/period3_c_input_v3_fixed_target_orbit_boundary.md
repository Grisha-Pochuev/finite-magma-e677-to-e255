# Period-3 c-Input V3 Fixed-Target Orbit Boundary

Date: 2026-06-28.

Status:

```text
boundary / clean c-input V3 reduces to two right-c source orbits
```

## Purpose

This specializes:

```text
clean_v3_fixed_target_source_orbit_reduction.md
```

to the new period-3 V3 bridge from:

```text
period3_row_b_Ib_c_input_v3_lemma.md
period3_c_input_v3_second_layer_boundary.md
```

The point is to give the next continuation a concrete object, not only the
generic phrase "use V3 admissibility".

## Setup

Use the period-3 data:

```text
z*h=b,
b*h=c,
c*h=z,
b*Ib=h.
```

Set:

```text
BC=b*c,
A=Ib*c,
K=A*Ib,
L=c*K.
```

Assume the immediate routes do not occur:

```text
A!=BC,
A not in watched/old data,
L!=h,
L not in watched/old data,
no input-output hit in H_c.
```

Then rows `b` and `Ib` form a clean same-input V3 bridge at common input:

```text
c.
```

Its target-lift in `H_c` is:

```text
row b:  h -> BC,
row Ib: L -> A.
```

## Two Right-c Source Orbits

For fixed target:

```text
c,
```

the V3 bridge starts two source-successor orbits:

```text
b  -> BC -> BC*c -> ...
Ib -> A  -> A*c  -> ...
```

The first two attached `H_c` layers are:

```text
row b:  h             -> BC
row Ib: L             -> A
row BC: (b*BC)*b      -> BC*c
row A:  (Ib*A)*Ib     -> A*c.
```

This is exactly the generic V3 four-edge matching with:

```text
p=b,
q=Ib,
z=c,
s=BC,
r=A.
```

## First-Event Split

Continue the two right-`c` source orbits.  The first event routes if it is:

```text
1. cross-orbit source hit;
2. output merge;
3. input repeat in H_c;
4. input-output cross hit in H_c;
5. watched/core hit against the period-3 or old relay footprint.
```

These are the standard roles from:

```text
fixed_target_source_orbit_first_merge_boundary.md
same_target_pair_collision_trichotomy_lemma.md
ported_interval_state_lemma.md
```

The only clean finite residual is:

```text
a same-orbit right-c self-repeat inside one of the two source orbits.
```

At that point the target-independent zipper machinery applies with:

```text
t=c.
```

Use:

```text
fixed_target_zipper_bridge_necklace_lemma.md
fixed_target_zipper_reduces_to_v3_admissibility.md
```

## Measure Interpretation

This branch is not the original period-3 right-`h` terminal return:

```text
c*h=z.
```

It is a V3-born fixed-target problem at the new target:

```text
c.
```

Therefore the right comparison is the unified V3/fixed-target measure:

```text
clean c-input V3
-> two right-c source orbits
-> first routed event or right-c self-repeat
-> fixed-target zipper/V3 necklace at target c.
```

If the unified V3 admissibility principle is proved, this fully clean branch
cannot remain as an independent period-3 obstruction.

## Next Use

The next direct attempts should be tried in this order:

```text
1. prove the watched hit A=Ib*c=z, as in the public db;
2. prove the fan-lift input L=h, equivalently (Ib*c)*Ib=Ic;
3. otherwise use this boundary to reduce the clean branch to the ordinary
   fixed-target V3 orbit machinery at target c.
```

Warning:

```text
period3_all_cycles_Ibc_scan_diagnostic.md
```

shows that `A=z` is not a consequence of a bare period-3 right-`h` cycle.
Fresh all-cycle examples can have:

```text
A fresh,
A*Ib=c,
L=c*c.
```

So route 1 must use the shared-step/G12 origin or global minimality/core data.
