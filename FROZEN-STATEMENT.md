# Frozen Statement: E677 ⇒ E255 for Finite Magmas — Order-9 Form 2 Reproduction

## Exact Proposition
We are verifying the claim that **no finite magma of order 9 with exactly 3 Bad elements satisfying E677 can exist**, specifically for normalized form 2 (the "no-HIT" branch with exactly three Bad elements). This is a bounded computational exclusion, not a general proof.

- **Problem**: E677: `x = y * (x * ((y * x) * y))` implies E255: `x = ((x * x) * x) * x`
- **Scope**: Finite magmas of order 9, exactly 3 Bad elements (where `D(x) = (x*x)*x` and `D(x) = x` means Good, otherwise Bad)
- **Branch**: no-HIT (no HIT = no certain obstruction pattern)
- **Normalized form**: Form 2 (one of 24 normalized forms, 17 closed, 7 remaining: 11, 15, 16, 18, 21, 23, 24)
- **Claim being reproduced**: The fourteen exhaustive leaves of normalized form 2 are UNSAT in both CaDiCaL195 and Glucose42 — i.e., no Bad element can exist in this case, so the form is "closed".

## What This Reproduction Verifies
If both solvers report `unsat=8/8` with marker `bad3 summary: unsat=8/8; unknown=[]`, the form-2 no-HIT-3-Bad case is computationally excluded, consistent with the repo's claim.

## Frozen Text — Do Not Modify
The exact text above defines the claim being reproduced. Any encoding or solver invocation must be checked against this statement. Drift from this text (different order, different Bad count, different branch, different form) invalidates the reproduction.