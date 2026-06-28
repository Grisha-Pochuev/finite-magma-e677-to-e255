# Anchored-M7 Cycle-End Saturation Diagnostic

Date: 2026-06-25.

Status:

```text
diagnostic / cycle-end closure gives zipper equations, not direct collision
```

## Purpose

This records the bounded equality-closure check for:

```text
anchored_m7_cycle_end_template.md
anchored_m7_cycle_zipper_lemma.md
```

The question was whether the named cycle-end triple already forces an
`H_h` path/fan collision such as:

```text
im1=r1,
i0=rm1,
i0=im1.
```

## Script

```text
tools/anchored_m7_cycle_end_saturation.js
```

It uses:

```text
E677,
left cancellation,
edge predecessor formula,
fixed-target source-successor formula,
shared-input collision consequence,
anchored-X3 false branch data,
cycle-end equations.
```

## Run

Command:

```text
tools/node-portable/node.exe tools/anchored_m7_cycle_end_saturation.js 4 12 300000
```

Result:

```text
terms: 33811
closeRounds: 8
clean-consistent-in-closure: true
```

Forbidden clean collapses were not derived:

```text
T=S,
T=U,
S=W,
b=z,
r0=r1,
r0=rm1,
r0=rm2,
rm2=rm1,
i0=im1,
i0=im2,
im2=im1,
i0=rm1,
im1=r1.
```

Candidate direct collisions were not derived:

```text
im1=r1: false
i0=rm1: false
im2=r0: false
i0=im1: false
i0=im2: false
im2=im1: false
r0=rm1: false
r0=rm2: false
r1=rm1: false
r1=rm2: false
r0*r1=rm1*r0: false
```

Useful equalities derived:

```text
r0*i0=rm1*im1: true
i0=(rm1*r0)*rm1: true
im1=(rm2*rm1)*rm2: true
im2=h*(rm1*rm2): true
r1*((r0*r1)*r0)=h: true
r0*((rm1*r0)*rm1)=h: true
```

## Interpretation

The direct path/fan conjectures:

```text
im1=r1,
i0=rm1,
i0=im1
```

do not follow from the bounded local closure.

But the run confirms the useful zipper structure:

```text
i0 = h*(r1*r0) = (rm1*r0)*rm1,
im1 = h*(r0*rm1) = (rm2*rm1)*rm2.
```

This matches the general proof recorded in:

```text
anchored_m7_cycle_zipper_lemma.md
```

## Next Target

Do not repeat this check as another guessed direct equality among:

```text
i0, im2, im1, r0, r1, rm2, rm1.
```

The sharper residual is:

```text
clean cyclic zipper
```

with zipper certificates:

```text
Z_i=(r_{i-1}*r_i)*r_{i-1}=h*(r_{i+1}*r_i).
```

The next meaningful split is the first collision of these zipper
certificates, or a proof that a fully clean cyclic zipper creates strict clean
theta in `H_h`.
