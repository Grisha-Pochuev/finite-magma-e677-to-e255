# ATP Templates

This folder contains small TPTP-style proof/search templates for the current
E677 -> E255 project.

They are not broad model searches and are not claimed as completed proofs.
Each file should encode one current residual tightly enough that an external
ATP run can test a specific proposed consequence.

Current file:

```text
anchored_x3_m7_self_repeat.p
```

It formalizes the clean anchored-X3/M7 source-orbit residual:

```text
p*b=q*b=z,
U=p*z,
W=q*z,
h=U*p=W*q,
z*h=b,
T=U*h,
S=W*h,
T!=S,
```

plus the first right-`h` source-successor layers and the exclusion of visible
period-1 and period-2 repeats.  The conjecture section is intentionally
modular: edit only that final block to test a proposed M7 consequence.

Environment helper:

```text
check_atp_environment.ps1
```

It checks whether common ATP tools are visible in `PATH` and confirms that the
template file exists.  At creation time no ATP prover was visible in the
current Codex shell, so the template has not been prover-checked.
