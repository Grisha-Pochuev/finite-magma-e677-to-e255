"""Scan the exact rank of t -> O7_t^-1(0) in the T6-kernel abstraction."""

from __future__ import annotations

import argparse
import itertools
import threading
import time

import e677_fiber7_T6_kernel_sat as kernel
from pysat.solvers import Solver  # type: ignore


def add_conditional_rank(clauses, used, selector, rank):
    # At most rank used values.
    for subset in itertools.combinations(used, rank + 1):
        clauses.append([-selector, *(-literal for literal in subset)])
    # At least rank used values.
    for subset in itertools.combinations(used, len(used) - rank + 1):
        clauses.append([-selector, *subset])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--per-rank-seconds", type=float, default=20.0)
    parser.add_argument("--solver", default="glucose42")
    args = parser.parse_args()

    clauses, O7_vars, A_vars, K_vars, D_selectors, variable_count = kernel.build()
    next_variable = variable_count + 1
    used = list(range(next_variable, next_variable + kernel.N))
    next_variable += kernel.N
    for z in range(kernel.N):
        witnesses = [O7_vars[t][z][0] for t in range(kernel.N)]
        for witness in witnesses:
            clauses.append([-witness, used[z]])
        clauses.append([-used[z], *witnesses])
    rank_selectors = list(range(next_variable, next_variable + kernel.N))
    next_variable += kernel.N
    for rank, selector in enumerate(rank_selectors, 1):
        add_conditional_rank(clauses, used, selector, rank)

    print(
        f"encoding: variables={next_variable-1}; clauses={len(clauses)}; "
        f"ranks=1..7; per-rank={args.per_rank_seconds}; solver={args.solver}",
        flush=True,
    )
    results = []
    started = time.time()
    with Solver(name=args.solver, bootstrap_with=clauses) as solver:
        for rank, selector in enumerate(rank_selectors, 1):
            timer = threading.Timer(
                max(0.05, args.per_rank_seconds), solver.interrupt
            )
            timer.daemon = True
            timer.start()
            try:
                status = solver.solve_limited(
                    assumptions=[selector], expect_interrupt=True
                )
            finally:
                timer.cancel()
            if status is None:
                results.append((rank, "UNKNOWN", None))
                solver.clear_interrupt()
            elif status is False:
                results.append((rank, "UNSAT", None))
            else:
                model = solver.get_model()
                positive = {literal for literal in model if literal > 0}
                D_index = next(
                    index for index, literal in enumerate(D_selectors)
                    if literal in positive
                )
                O7 = tuple(
                    kernel.decode_permutation(model, row) for row in O7_vars
                )
                profile = kernel.kernel_profile(O7)
                if len(profile[0]) != rank:
                    raise AssertionError((rank, profile))
                results.append((rank, "SAT", (D_index, profile)))
            print(
                f"rank={rank}; status={results[-1][1]}; "
                f"witness={results[-1][2]}; elapsed={time.time()-started:.3f}s",
                flush=True,
            )
    print(f"RANK SCAN COMPLETE; results={results}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
