# Period-3 Shared-Step Profile Candidate

Date: 2026-06-28.

Status:

```text
candidate theorem target
```

## Statement To Prove

Assume the strict period-3 shared-step anchored false branch:

```text
p*b=q*b=z,
U=p*z,
W=q*z,
h=U*p=W*q,
z*h=b,
b*h=c,
c*h=z,
U*h=T,
W*h=S,
T!=S.
```

Let:

```text
b*Ib=h,
c*Ic=h,
A=Ib*c,
K=A*Ib,
L=c*K.
```

Then the expected profile is:

```text
A=z,
K=Ic,
L=h,
Ib*h=c,
z*Ib=Ic.
```

In expanded form:

```text
Ib*c=z,
(Ib*c)*Ib=Ic,
c*((Ib*c)*Ib)=h,
Ib*h=c,
z*Ib=Ic.
```

## Why This Is Strong Enough

The first equality:

```text
Ib*c=z
```

is a watched output hit for the `c`-input V3 branch.  The equality:

```text
Ib*h=c
```

gives the named middle-target fan in `H_c`.  So proving this profile closes
the current period-3 M7 residual before the generic clean V3 branch is needed.

## Evidence

The diagnostic:

```text
period3_clean_anchored_profile_diagnostic.md
```

records:

```text
strict shared-step period-3 candidates: 13200
examples with Ib*c!=z:                    0
```

The companion dirty-reason scan found:

```text
dirty anchored-X3 triples: 0
```

so the db evidence says the full profile appears as soon as strict period-3
and the shared-step false branch coexist.

## Important Non-Route

Do not try to prove:

```text
bare period-3 cycle => Ib*c=z.
```

That is false in the cached db scan.  Also, depth-5 anchored local saturation
does not derive the profile from the displayed equations.  The proof must use
the shared-step structure, not only the zipper equations and not just a short
term-rewrite closure.

## Contradiction Target

Assume:

```text
A=Ib*c != z.
```

Under the strict period-3 shared-step equations, derive one of:

```text
1. the shared-step equations cannot all hold;
2. the anchored false branch collapses (`T=S` or equivalent);
3. a standard routed event appears immediately;
4. the period-3 zipper is not strict.
```

Useful db fingerprints to try to prove structurally are:

```text
p*c=T,
q*c=S,
U*z=Ib,
W*z=Ib.
```

But no single fingerprint, and not even the four-fingerprint package, currently
closes the local saturation by itself.  If these are used, they must be used as
part of a two-row shared-step argument.
