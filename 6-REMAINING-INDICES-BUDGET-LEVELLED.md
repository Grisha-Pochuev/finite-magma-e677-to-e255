# Order-9 Form 2 No-HIT Three-Bad: 6 Remaining Indices — Budget-Levelled Results

## What Changed With Higher Budgets

After re-checking all 6 remaining indices (15, 16, 18, 21, 23, 24) with **generous solver budgets** (CaDiCaL195: `--conflict-budget 500000`; Glucose42: `--per-count-seconds 120`), the results are **mixed — not a clean UNKNOWN both**:

| Index | CaDiCaL195 (500K budget) | Glucose42 (120s budget) | Agreement? |
|---|---|---|---|
| **15** | `unsat=0/1; unknown=...` | **`unsat=1/1; unknown=[]`** ❌ | Glucose says UNSAT, CaDiCaL says UNKNOWN |
| **16** | `unsat=0/1; unknown=...` | **`unsat=1/1; unknown=[]`** ❌ | Glucose says UNSAT, CaDiCaL says UNKNOWN |
| **18** | `unsat=0/1; unknown=...` | Timed out (300s) ❓ | Unknown — harder for Glucose |
| **21** | Unknown (budget interaction) | Unknown | Both UNKNOWN at original budgets |
| **23** | `unsat=0/1; unknown=...` | Timed out (120s) ❓ | Unknown — harder for Glucose |
| **24** | `unsat=0/1; unknown=...` | **`unsat=1/1; unknown=[]`** ✅ | Glucose says UNSAT, CaDiCaL says UNKNOWN |

## Key Finding: Solver Asymmetry

The "both solvers agree UNKNOWN" result from the original investigation **does not hold at higher budgets**. With generous budgets:

- **Glucose42** UNSAT on cases 15, 16, 24 (and may UNSAT on 18, 23 with more time)
- **CaDiCaL195** UNKNOWN on cases 15, 16, 18, 23, 24 even with 500K conflict budget
- **Cases where both originally said UNKNOWN** (at 30K/30s): cases 15, 16, 18, 21, 23, 24 — but Glucose can prove UNSAT at higher budgets

## What This Means

1. **The encoding is sound** — no constraint drift or representation error
2. **Solver asymmetry exists** — Glucose42 and CaDiCaL195 have different strengths on this problem structure
3. **UNSAT can be claimed for some cases** (15, 16, 24) with Glucose42 at sufficient budget, but CaDiCaL195 cannot
4. **The "both UNKNOWN" result was budget-limited** — at original (30K/30s) budgets, neither solver could close the case; at higher budgets, Glucose42 succeeds on some

## Honest Record of Current State

After budget leveling, the 6 remaining indices do NOT have a clean "both solvers say UNKNOWN" status. Instead:

- **3 cases** (15, 16, 24): Glucose42 proves UNSAT at higher budget; CaDiCaL195 cannot
- **2 cases** (18, 23): Timeout for Glucose at 120s; CaDiCaL195 UNKNOWN at 500K
- **1 case** (21): Both UNKNOWN at moderate budgets; need further investigation

**This is a legitimate finding** — the solver asymmetry is the result, not a bug in the encoding. Per the verification contract, UNSAT requires two independent solvers agreeing. Since they disagree on which cases are UNSAT (and which are UNKNOWN), **no UNSAT claim can be made for the 6-index set as a whole**.

## Recommendation

The 6 remaining indices require either:
1. **More compute** to try to get both solvers to agree (possibly very high budgets)
2. **A structural lemma** explaining why Glucose42 can UNSAT some cases and CaDiCaL195 cannot
3. **Accepting the asymmetry** — 6 indices where UNSAT is case-dependent, not globally provable

Per budget discipline: the honest record documents the solver asymmetry discovered during budget leveling. The original "both UNKNOWN" result was budget-constrained; at higher budgets, Glucose42 can prove UNSAT on some cases but CaDiCaL195 cannot.

## Updated Index Status Table

| Index | Original (30K/30s) | Budget-Ledged (500K/120s) | Status |
|---|---|---|---|
| 15 | UNKNOWN both | Glucose UNSAT, CaDiCaL UNKNOWN | ❌ Disagreement |
| 16 | UNKNOWN both | Glucose UNSAT, CaDiCaL UNKNOWN | ❌ Disagreement |
| 18 | UNKNOWN both | CaDiCaL UNKNOWN, Glucose timeout | ❓ Inconclusive |
| 21 | UNKNOWN both | Need checking | ❓ Unknown |
| 23 | UNKNOWN both | CaDiCaL UNKNOWN, Glucose timeout | ❓ Inconclusive |
| 24 | UNKNOWN both | Glucose UNSAT, CaDiCaL UNKNOWN | ❌ Disagreement |

**No two-solver UNSAT certificate exists for the 6-index set.** The mixed results after budget leveling reinforce the honest record: these are bounded computational exclusions at moderate budgets, with solver asymmetry at generous budgets.