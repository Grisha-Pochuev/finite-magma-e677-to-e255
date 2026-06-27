# M496 Shared-Step Relation Scan Diagnostic

Date: 2026-06-21.

Status:

```text
diagnostic / nearby relation scan for anchored identity
```

## Purpose

After the strong anchored identity:

```text
U*h=W*h
```

was verified in M496, this scan checks whether there is another short
universal relation around the common value:

```text
T=U*h=W*h.
```

The goal is to avoid guessing the next proof target blindly.

## Script

The permanent diagnostic script is:

```text
tools/m496_shared_step_relation_scan.js
```

It scans all M496 shared-step pairs:

```text
p*b=q*b=z,
U=p*z,
W=q*z,
h=U*p=W*q,
T=U*h=W*h.
```

## Result

The scan returned:

```text
pairs: 892800
h*(T*U)=p: 892800
h*(T*W)=q: 892800
T*U=T*W: 0
p*U=q*W: 0
U*T=W*T: 0
h*p=h*q: 0
z*T=b: 0
T*b=z: 0
T*h=b: 0
p*U=T: 0
q*W=T: 0
U*T=h: 0
W*T=h: 0
```

## Interpretation

The back-projection formulas:

```text
h*(T*U)=p,
h*(T*W)=q
```

are universal in M496 and already follow algebraically from E677 once
`T=U*h=W*h` is named.

No checked neighboring equality is also universal in M496.  In particular,
the next proof target should not be a short equality such as:

```text
p*U=q*W
U*T=W*T
z*T=b
```

The likely remaining route is structural: prove that the negated branch
cannot support a clean anchored back-projected shared step, or measure that
residual as a smaller relay object.
