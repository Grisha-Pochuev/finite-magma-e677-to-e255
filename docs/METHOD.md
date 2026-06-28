# Method

This repository uses a mixed mathematical and computational workflow.

## 1. Structural reasoning

The primary activity is deriving consequences of

```text
E677: x = y * (x * ((y * x) * y)).
```

The project tries to explain why finite counterexamples should be impossible,
not merely to enumerate many cases.

## 2. Bad-element analysis

Assume a finite counterexample exists.  Choose a bad element `0` for which
`E255` fails.  The notation

```text
b_j = L_0^{-j}(0)
r_j = b_j*0
```

is used to study the local structure forced around that bad element.

The central target is to show:

```text
r_2=b_2*0 must be 0.
```

That is exactly the `E255` condition for the chosen element.

## 3. Forced-edge expansion

A typical local step starts from an edge

```text
a*z=c
```

and uses `E677` to force predecessor or triangle identities around `a`, `z`,
and `c`.

These local expansions are then organized into:

```text
bad-cycle ladders
source-orbit ladders
zipper patterns
pressure diamonds
double interval pressure
```

## 4. Bounded computation

Computation is used only when a finite branch or structural role is already
bounded enough to have a clear interpretation.

The current public reproducible checkpoint is the size-8 closure:

```powershell
.\verify_size8_closed.ps1
```

## 5. Formalization direction

Lean formalization is planned, but the present repository is not yet a Lean
proof.  The first useful Lean targets are local consequences of `E677`, not the
whole theorem.

See:

```text
formal/lean/README.md
```
