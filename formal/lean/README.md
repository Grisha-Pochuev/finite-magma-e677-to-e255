# Lean formalization plan

Lean is not yet the source of truth for this repository.

The present project state is:

- mathematical notes in Markdown;
- targeted JavaScript search scripts;
- recorded verification logs;
- candidate structural lemmas under active development.

## Why Lean is not added as a fake result

The project should be reproducible and honest.  Adding a superficial Lean file
that only states the theorem without proving the key lemmas would make the
repository look more formal than it really is.

Instead, this folder records the intended formalization boundary.

## First Lean targets

The first useful Lean formalization should avoid the full hard theorem and
formalize local consequences of `E677`.

Good first targets:

1. Define a finite magma as a type with a binary operation.
2. State `E677`.
3. State `E255`.
4. Prove the local edge-predecessor expansion:

```text
if a*z=c, then E677 gives forced predecessor identities around a, z, c.
```

5. Formalize the bad-cycle notation used in the Markdown lemmas.

## Current theorem boundary

The full statement

```text
E677 implies E255 for all finite magmas
```

is not yet proved in this repository, either informally or in Lean.
