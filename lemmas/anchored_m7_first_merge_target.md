# Anchored M7 First-Merge Target

Date: 2026-06-21.

Status:

```text
routed target / first-event target reduced to clean self-repeat
```

## Current State

The live anchored-X3 residual is:

```text
clean later/fresh right-h source-successor cycle
```

from:

```text
anchored_x3_clean_self_repeat_normal_form.md
anchored_m7_saturation_diagnostic.md
```

The first fresh layer:

```text
T1=T*h,
S1=S*h,
B1=b*h
```

does not short-collapse in bounded equality closure.

## Exact Next Target

Define the three right-`h` source-successor orbits:

```text
R_U^0=U,  R_U^{n+1}=R_U^n*h,
R_W^0=W,  R_W^{n+1}=R_W^n*h,
R_z^0=z,  R_z^{n+1}=R_z^n*h.
```

Each row `R^n` gives an edge in `H_h`:

```text
I^n -> R^{n+1},
R^n*I^n=h.
```

The first event among these three orbits is one of:

```text
1. cross-orbit source hit:       R_A^i = R_B^j;
2. cross-orbit output merge:     R_A^{i+1} = R_B^{j+1}, with R_A^i != R_B^j;
3. input-output cross hit between two active H_h edges;
4. watched/core hit;
5. self-repeat inside one orbit.
```

Cases 1-4 are now routed by:

```text
anchored_m7_first_event_routing_lemma.md
fixed_target_source_orbit_first_merge_boundary.md
same_target_pair_collision_trichotomy_lemma.md
anchored_x3_source_orbit_boundary.md
```

The only live case is:

```text
5. clean self-repeat inside one right-h source orbit before any cross-orbit
   event.
```

## Remaining Desired Lemma

Prove:

```text
In a minimal G12 loop, a clean self-repeat inside one anchored right-h source
orbit either:

1. creates strict clean theta;
2. repeats a full ported interval in an independent role;
3. regenerates anchored-X3 with smaller M7;
4. hits the old/core footprint.
```

Equivalently, a clean self-repeat cannot be terminal.

## Do Not Repeat

Do not keep testing one-step equalities among:

```text
T1,S1,B1.
```

The bounded diagnostic already found no short collapse there.  The useful
object is the first finite event of the three right-`h` source orbits.
