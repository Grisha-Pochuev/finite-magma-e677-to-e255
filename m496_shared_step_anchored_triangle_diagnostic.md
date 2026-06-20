# M496 Shared-Step Anchored Triangle Diagnostic

Date: 2026-06-21.

Status:

```text
diagnostic / verifies strong anchored-triangle identity in M496
```

## Purpose

This checks the strong hypothesis from:

```text
shared_step_anchored_triangle_boundary.md
```

For every shared-step pair:

```text
p*b=q*b=z,
p!=q,
U=p*z,
W=q*z,
h=U*p=W*q,
```

test:

```text
U*h=W*h.
```

## Script

The permanent diagnostic script is:

```text
tools/m496_shared_step_anchored_triangle.ps1
```

It uses PowerShell because ordinary `node` is not visible in the current
Codex shell.

## Result

The scan over all M496 shared-step row pairs returned:

```text
sharedStepPairs: 892800
hMismatch:       0
zhMismatch:      0
uWHMismatch:     0
triangleMismatch:0
sameOutput:      892800
```

Here:

```text
hMismatch=0
```

means:

```text
U*p=W*q
```

for every pair, and:

```text
zhMismatch=0
```

means:

```text
z*h=b.
```

The strong identity:

```text
U*h=W*h
```

also holds for every one of the `892800` pairs.

The common output `T=U*h=W*h` was not equal to any of:

```text
b,z,h,U,W,p,q
```

in this diagnostic:

```text
other: 892800
```

## Interpretation

In M496, every shared-step pair has the anchored incoming fan in `H_h`:

```text
p -> T,
q -> T,
T=U*h=W*h.
```

This exactly matches the stronger pattern suggested by the web run.  If the
identity is proved in all finite E677 magmas, it closes the current clean
first-extra V3 branch and the clean orbit-theta branch at the shared-step
level, before the proof needs first-extra analysis.

This is still a diagnostic, not a proof.
