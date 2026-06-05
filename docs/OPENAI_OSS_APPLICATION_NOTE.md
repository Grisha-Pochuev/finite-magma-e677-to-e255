# OpenAI Codex for OSS application note

This is a short draft describing the project for an OSS application.

## Project

**The Open Mathematics Project** is an open, reproducible research workflow for
attacking concrete open mathematical problems with human direction,
AI-assisted reasoning, and checkable computation.

The current public repository focuses on one problem in finite algebra:
whether the identity

```text
x = y * (x * ((y * x) * y))
```

forces

```text
x = ((x * x) * x) * x
```

in all finite magmas.

## Why this can fit open source

The repository is not a conventional software library.  It is open-source
mathematical research:

- all working notes are public;
- bounded computational checks are included as scripts;
- verification logs are published;
- current gaps and candidate lemmas are stated explicitly;
- the long-term direction is formalization in Lean or a similar proof
  assistant.

## Maintainer role

Grisha Pochuev maintains the research direction and public record.  Codex is
used as a research assistant for algebraic derivation, case organization,
script creation, reproducibility packaging, and status summaries.

## Short application text

The Open Mathematics Project is a public research repository for reproducible
AI-assisted mathematics.  The current focus is the finite-magma implication
E677 -> E255.  The repository publishes working lemmas, bounded search scripts,
verification logs, closed finite-size cases, and the current proof frontier.
The goal is to make the research inspectable, reusable, and eventually
formalizable in Lean.

