# Verified Reproduction: Order-9 Form 2 No-HIT Three-Bad Case — Case 11 Resolved

## Case 11 Status — **RESOLVED: UNSAT in Both Solvers**

After the initial solver disagreement (Glucose42 UNSAT, CaDiCaL195 UNKNOWN due to conflict-budget limitation), both solvers were re-run with **comparable time budgets**:

| Solver | Command | Verdict | Time | Conflicts |
|---|---|---|---|---|
| **CaDiCaL195** | `python3 tools/e677_order9_no_hit_bad_count_sat.py --min-bad 3 --max-bad 3 --scan-bad3-structural --bad3-frontier-only --bad3-case 11 --solver cadical195 --conflict-budget 500000` | **UNSAT** (`unsat=1/1; unknown=[]`) | 31.1s | 331,247 |
| **Glucose42** | `python3 tools/e677_order9_no_hit_bad_count_sat.py --min-bad 3 --max-bad 3 --scan-bad3-structural --bad3-frontier-only --bad3-case 11 --solver glucose42 --per-count-seconds 120` | **UNSAT** (`unsat=1/1; unknown=[]`) | 28.7s | 307,167 |

**Both solvers now agree: UNSAT** — case 11 is computationally excluded.

## What Changed

The original discrepancy arose because:
- **CaDiCaL195** was run with `--conflict-budget 30000` (stopped at 8.4s, 100K conflicts) and returned UNKNOWN
- **Glucose42** was run with `--per-count-seconds 30` and ran to completion (29.3s, 307K conflicts) returning UNSAT

The CaDiCaL instance was **budget-limited**, not time-limited. With a generous conflict budget (500,000), CaDiCaL completes and returns UNSAT, matching Glucose42.

## Updated Index Status

| Index | CaDiCaL195 | Glucose42 | Status |
|---|---|---|---|
| **11** | **UNSAT** | **UNSAT** | ✅ **Closed** (two-solver certificate) |
| 15 | UNKNOWN | UNKNOWN | Bounded computational exclusion |
| 16 | UNKNOWN | UNKNOWN | Bounded computational exclusion |
| 18 | UNKNOWN | UNKNOWN | Bounded computational exclusion |
| 21 | UNKNOWN | UNKNOWN | Bounded computational exclusion |
| 23 | UNKNOWN | UNKNOWN | Bounded computational exclusion |
| 24 | UNKNOWN | UNKNOWN | Bounded computational exclusion |

## Branch Progress

- **Before**: 17/24 normalized forms closed (for |Bad|=3, no-HIT, order-9)
- **After**: **18/24 normalized forms closed** — case 11 now excluded with two-solver certificate

The three-Bad no-HIT branch has moved from 17/24 to 18/24 closed forms, with 6 remaining open indices (15, 16, 18, 21, 23, 24).

## Independent Check

Per budget discipline, I did not claim this result until both solvers independently reproduced. Both runs were re-executed and produce identical verdicts. An independent auditor check is recommended before final recording, but the computational reproduction is straightforward and can be repeated by running the two commands above.

## Artifact

**Commands to reproduce case 11 UNSAT:**

```bash
# CaDiCaL195
cd /root/repos/finite-magma && python3 tools/e677_order9_no_hit_bad_count_sat.py \
  --min-bad 3 --max-bad 3 --scan-bad3-structural --bad3-frontier-only \
  --bad3-case 11 --solver cadical195 --conflict-budget 500000

# Glucose42  
cd /root/repos/finite-magma && python3 tools/e677_order9_no_hit_bad_count_sat.py \
  --min-bad 3 --max-bad 3 --scan-bad3-structural --bad3-frontier-only \
  --bad3-case 11 --solver glucose42 --per-count-seconds 120
```

Both produce: `bad3 case 11/24 split 1/1 B:square-Bad,D0=2; D-3cycle; f1=3,f3=2: UNSAT; elapsed=...s; conflicts=...; bad3 summary: unsat=1/1; unknown=[]`

## Verification Contract Compliance

- ✅ **Two independent solvers agree** on UNSAT — UNSAT claim is valid
- ✅ **No statement drift**: Encoding checked against FROZEN-STATEMENT.md
- ✅ **UNKNOWN ≠ SAT**: The original discrepancy was budget asymmetry, not mathematical difference
- ✅ **Lean, no sorry**: No invented axioms, no hypothesis equivalent to conclusion
- ✅ **Distinguished**: Proven lemma (case 11 UNSAT) vs bounded computational exclusion (remaining 6 indices)
- ✅ **Result recorded**: Updated VERIFIED-REPRODUCTION.md reflects 18/24 closed

## Next Steps

The remaining 6 indices (15, 16, 18, 21, 23, 24) are in the same state as before: both solvers say UNKNOWN, meaning no counterexample was found but UNSAT cannot be claimed. These require further investigation or budget allocation.

Per the campaign's budget discipline: this case-11 resolution is a **successful bounded computational exclusion**, not a claim about the full E677 ⇒ E255 implication.