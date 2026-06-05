# Contributing

This repository is an open research project, not a finished theorem library.
Contributions are welcome when they make the mathematical status clearer,
more reproducible, or easier to formalize.

## Useful contributions

Good contributions include:

- checking a lemma file for a missing `E677` justification;
- reproducing the size-8 verification script and reporting the result;
- simplifying or documenting the JavaScript search tools;
- translating a working note into a cleaner formal statement;
- proposing a Lean formalization of a small local lemma;
- identifying a gap, ambiguity, or unsupported closure claim.

## Evidence standards

Please distinguish clearly between:

```text
proved local consequence
bounded computational result
diagnostic observation
candidate lemma
```

Do not upgrade a diagnostic observation into a proof step unless the exact
`E677` derivation or reproducible computation is given.

## Preferred style

When proposing a mathematical change, include:

1. the exact statement;
2. the notation used;
3. the `E677` edge or substitution that justifies each new forced value;
4. whether the claim is proved, computationally checked, or still a candidate.

## Reproducibility

For computational claims, include:

```text
command
time limit
machine or environment if relevant
result
log or output excerpt
```

The current reproducibility guide is:

```text
docs/REPRODUCIBILITY.md
```

