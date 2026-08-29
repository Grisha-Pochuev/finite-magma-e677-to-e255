"""Exact T6-kernel check of the maximum column-collision diagnostic layer.

The diagnostic E_col(A,D)=sum_t sum_v C(|F_t^-1(v)|,2), where
F_t(q)=D(q-t)-A(q), is not itself a tuple-6 invariant.  Its maximum 63,
however, selects only 28 concrete (D,A) pairs.  This script checks their
union in one exact SAT formula.
"""

from __future__ import annotations

import argparse
import itertools
import threading
import time
from collections import Counter

import e677_fiber7_T6_kernel_sat as kernel
from pysat.solvers import Solver  # type: ignore


def column_collision(A, D):
    total = 0
    for t in range(kernel.N):
        counts = Counter(
            (D[(q - t) % kernel.N] - A[q]) % kernel.N
            for q in range(kernel.N)
        )
        total += sum(size * (size - 1) // 2 for size in counts.values())
    return total


def render(table):
    return "/".join("".join(map(str, row)) for row in table)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seconds", type=float, default=180.0)
    parser.add_argument("--solver", default="glucose42")
    args = parser.parse_args()

    clauses, O7_vars, A_vars, K_vars, D_selectors, variable_count = kernel.build()
    allowed = []
    for D_index, D in enumerate(kernel.CANONICAL_D):
        for tail in itertools.permutations(range(1, kernel.N)):
            A = (0, *tail)
            if column_collision(A, D) == 63:
                allowed.append((D_index, A))
    if len(allowed) != 28:
        raise AssertionError(len(allowed))

    pair_selectors = list(
        range(variable_count + 1, variable_count + 1 + len(allowed))
    )
    kernel.add_exactly_one(clauses, pair_selectors)
    for selector, (D_index, A) in zip(pair_selectors, allowed):
        clauses.append([-selector, D_selectors[D_index]])
        for inp, value in enumerate(A):
            clauses.append([-selector, A_vars[inp][value]])

    print(
        f"max-column-collision pairs={len(allowed)}; variables={pair_selectors[-1]}; "
        f"clauses={len(clauses)}; seconds={args.seconds}",
        flush=True,
    )
    started = time.time()
    with Solver(name=args.solver, bootstrap_with=clauses) as solver:
        timer = threading.Timer(max(0.05, args.seconds), solver.interrupt)
        timer.daemon = True
        timer.start()
        try:
            status = solver.solve_limited(expect_interrupt=True)
        finally:
            timer.cancel()
        stats = solver.accum_stats()
        if status is None:
            print(
                f"status=UNKNOWN; elapsed={time.time()-started:.3f}s; stats={stats}"
            )
            return 3
        if status is False:
            print(
                f"MAX COLUMN-COLLISION T6 LAYER UNSAT; "
                f"elapsed={time.time()-started:.3f}s; stats={stats}"
            )
            return 2
        model = solver.get_model()

    positive = {literal for literal in model if literal > 0}
    pair_index = next(
        index for index, selector in enumerate(pair_selectors)
        if selector in positive
    )
    D_index, expected_A = allowed[pair_index]
    O7 = tuple(kernel.decode_permutation(model, row) for row in O7_vars)
    A = kernel.decode_permutation(model, A_vars)
    K = tuple(kernel.decode_permutation(model, row) for row in K_vars)
    if A != expected_A:
        raise AssertionError((A, expected_A))
    print(
        f"SAT MAX COLUMN-COLLISION T6 CORE; D={''.join(map(str,kernel.CANONICAL_D[D_index]))}; "
        f"A={''.join(map(str,A))}; profile={kernel.kernel_profile(O7)}; "
        f"elapsed={time.time()-started:.3f}s; stats={stats}"
    )
    print(f"O7={render(O7)}")
    print(f"K={render(K)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
