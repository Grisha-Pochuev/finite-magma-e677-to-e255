# Anchored M7 Saturation Diagnostic

Date: 2026-06-21.

Status:

```text
diagnostic / bounded equality closure for clean anchored-X3 M7 template
```

## Purpose

This records a local bounded saturation run for:

```text
atp/anchored_x3_m7_self_repeat.p
anchored_x3_clean_self_repeat_normal_form.md
```

The goal was to check whether the first fresh right-`h` successors:

```text
T1=T*h,
S1=S*h,
B1=b*h
```

already satisfy a short forced equality or collapse a clean assumption.

## Script

The permanent script is:

```text
tools/anchored_m7_saturation.js
```

It uses the same named anchored-X3 data as the ATP template, plus:

```text
E677,
left cancellation by row,
edge-predecessor formula,
fixed-target source-successor formula,
shared-input collision consequence.
```

It is a bounded ground-congruence diagnostic, not a proof engine.

## Run

Command:

```text
tools/node-portable/node.exe tools/anchored_m7_saturation.js 4 12 250000
```

Result:

```text
terms: 21639
clean-consistent-in-closure: true

candidate equalities:
  T1=S1: false
  T1=B1: false
  S1=B1: false
  T1=T:  false
  S1=S:  false
  B1=b:  false
  T1=p:  false
  S1=q:  false
  B1=alpha: false
  T1*h=T: false
  S1*h=S: false
  B1*h=b: false
```

The forbidden clean collapses:

```text
T=S,
T=U,
S=W,
b=z,
T*h=U,
S*h=W,
b*h=z
```

were not derived in the bounded closure.

## Interpretation

The first fresh successor layer:

```text
T1,S1,B1
```

does not locally collapse by short equality closure.  In particular, this
supports the current normal form:

```text
clean later/fresh right-h source-successor cycle
```

as a real residual, not an immediate one-step equality problem.

The next mathematical target should be the first merge/repeat of the
right-`h` source orbits, not another guessed short equality among
`T1,S1,B1`.
