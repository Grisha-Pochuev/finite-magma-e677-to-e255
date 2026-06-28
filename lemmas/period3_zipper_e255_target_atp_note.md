# Period-3 Zipper E255 Target ATP Note

Date: 2026-06-27.

Status:

```text
ATP target prepared / prover not available in current PATH
```

## Purpose

The db period-3 examples satisfy:

```text
E255(z), E255(b), E255(c), E255(h).
```

The bounded local saturation does not derive these identities.  The next
natural proof target is therefore the direct theorem:

```text
clean period-3 fixed-target zipper => E255(b)
```

or a refutation of that theorem under only the local assumptions.

## ATP Template

The TPTP template is:

```text
atp/period3_zipper_e255_target.p
```

It encodes:

```text
E677,
left cancellation,
edge predecessor formula,
fixed-target source-successor formula,
period-3 cycle z*h=b, b*h=c, c*h=z,
H_h zipper inputs alpha, Ib, Ic,
zipper formulas,
clean endpoint exclusions.
```

The default conjecture is only:

```text
z=z
```

so the file loads.  Replace the conjecture block with one of:

```text
f(f(f(b,b),b),b) = b
f(f(f(z,z),z),z) = z
f(h,h) = z*b
f(h,alpha) = b
```

when running an ATP prover.

## Environment Check

Command:

```text
powershell -ExecutionPolicy Bypass -File atp/check_atp_environment.ps1
```

Result:

```text
No ATP prover found in PATH.
```

This is not a mathematical negative result.  It only means the current local
environment cannot run the ATP target yet.

## Interpretation

The period-3 branch now has a precise theorem-proving target.  Until an ATP
prover or a stronger hand proof is available, do not treat:

```text
period-3 => E255(b)
```

as proved.  The active proof route remains the global admissibility of the
shifted-window bridge:

```text
H_b: h -> z*b,
H_c: h -> b*c.
```

