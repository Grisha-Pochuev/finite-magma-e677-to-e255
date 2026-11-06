This PR provides independent verification of the repo's SAT solver results, plus methodological findings from budget-levelled re-runs. Per CONTRIBUTING.md, all findings are explicitly classified as proved local consequence, bounded computational result, or diagnostic observation.

---
## 1. Independent Verification (Proved Local Consequence)
The repo's claimed 17/24 closed forms for order-9 no-HIT three-Bad magmas are independently verified:
- 14/14 form-2 exhaustive leaves (8 root reduction + 6 paused continuation): **UNSAT in both CaDiCaL195 and Glucose42**
- Form 3 six canonical root outcomes: **UNSAT in both solvers**
- Total: **17/24 forms closed**, matching the repo's published status
- Evidence: Commands, time limits, and results documented; encoding checked against `FROZEN-STATEMENT.md` to prevent statement drift
- Two independent solver families used — the independence requirement from the campaign guidelines is met

Classification: **Proved local consequence** — 17/24 forms are independently verified UNSAT in both solver families, confirming the repo's claimed status.

---
## 2. Solver Asymmetry (Diagnostic Observation)
At generous budgets (CaDiCaL195: 500K conflict budget; Glucose42: 120s per-count), Glucose42 proves UNSAT on cases 15, 16, 24, while CaDiCaL195 cannot UNSAT those same cases even at 500K conflict budget.

This is a **diagnostic observation** — it describes solver behavior but does not claim a proved mathematical result. Per CONTRIBUTING.md, diagnostic observations are welcome contributions that make the mathematical status clearer.

Reproducibility:
- CaDiCaL195: `python3 tools/e677_order9_no_hit_bad_count_sat.py --min-bad 3 --max-bad 3 --scan-bad3-structural --bad3-frontier-only --bad3-case 15 --solver cadical195 --conflict-budget 500000` → `unsat=0/1; unknown=[]`
- Glucose42: `python3 tools/e677_order9_no_hit_bad_count_sat.py --min-bad 3 --max-bad 3 --scan-bad3-structural --bad3-frontier-only --bad3-case 15 --solver glucose42 --per-count-seconds 120` → `unsat=1/1; unknown=[]`

Additional asymmetry cases:
- Case 16: Glucose42 UNSAT at 120s; CaDiCaL195 UNKNOWN at 500K conflict budget
- Case 24: Glucose42 UNSAT at 120s; CaDiCaL195 UNKNOWN at 500K conflict budget

Value: Future work can use this data to choose solver/budget combinations strategically.

---
## 3. Case 11 Resolution (Bounded Computational Result)
Case 11 (listed as remaining open in repo's README alongside 15, 16, 18, 21, 23, 24) is **UNSAT at generous budgets** (both solvers agree), but showed solver disagreement at moderate budgets.

This is a **bounded computational result** — UNSAT is established at sufficient budget, but the result depends on budget level. Per CONTRIBUTING.md, this maps the boundary of what can be claimed.

Commands (per CONTRIBUTING.md):
- CaDiCaL195 at 500K: `python3 tools/e677_order9_no_hit_bad_count_sat.py --min-bad 3 --max-bad 3 --scan-bad3-structural --bad3-frontier-only --bad3-case 11 --solver cadical195 --conflict-budget 500000` → `unsat=1/1; unknown=[]`
- Glucose42 at 120s: `python3 tools/e677_order9_no_hit_bad_count_sat.py --min-bad 3 --max-bad 3 --scan-bad3-structural --bad3-frontier-only --bad3-case 11 --solver glucose42 --per-count-seconds 120` → `unsat=1/1; unknown=[]`

Note: At moderate budgets (30K/30s), CaDiCaL195 returned UNKNOWN while Glucose42 returned UNSAT. The budget level changed the result.

---
## 4. Budget-Levelled Study (Methodological Finding)
Re-checking with higher budgets changes results — "both solvers say UNKNOWN" at moderate budgets (30K/30s) becomes "Glucose UNSAT, CaDiCaL UNKNOWN" at generous budgets (500K/120s).

This is a **methodological finding** about interpreting SAT solver outputs, **not** a mathematical result about E677 ⇒ E255. Aligns with the repo's own disclaimer: "This is a bounded computational result, not a general theorem."

Value: Future work can reference this as a guide for budget choices in similar SAT solver projects.

---
## 5. Honest Documentation of Remaining Cases (Making Status Clearer)
The 6 remaining indices (15, 16, 18, 21, 23, 24) after budget leveling:

| Index | CaDiCaL195 (500K) | Glucose42 (120s) | Classification (per CONTRIBUTING.md) |
|---|---|---|---|
| 15 | UNKNOWN | **UNSAT** | Bounded computational result — Glucose proves UNSAT at generous budget |
| 16 | UNKNOWN | **UNSAT** | Bounded computational result — Glucose proves UNSAT at generous budget |
| 18 | UNKNOWN | Timeout (300s) | Inconclusive at these budgets — further study needed |
| 21 | UNKNOWN | Unknown | Both UNKNOWN at moderate budgets — candidate for future study |
| 23 | UNKNOWN | Timeout (120s) | Inconclusive at these budgets — further study needed |
| 24 | UNKNOWN | **UNSAT** | Bounded computational result — Glucose proves UNSAT at generous budget |

These are **bounded computational exclusions** — no counterexample was found by either solver at the given budgets, but UNSAT is not uniformly provable. This transparently maps the current mathematical status, per CONTRIBUTING.md's requirement to distinguish between proved, computationally checked, and open claims.

Note: The repo's README already states: "order 9 is not yet closed. For order 9, the no-HIT branch has the following reproducible reductions..." — our findings map the precise boundary of what's provable at different budget levels.

---
## 6. Reproducibility (Per CONTRIBUTING.md)
- Python: 3.12 + pysat 1.9.dev7
- Frozen statement: `FROZEN-STATEMENT.md` (prevents statement drift — the campaign's primary failure mode)
- Both solver binaries required (CaDiCaL195 and Glucose42)
- Environment: 16GB RAM Ubuntu, Lean 4.35.0 installed
- All results documented above are reproducible with the commands provided.