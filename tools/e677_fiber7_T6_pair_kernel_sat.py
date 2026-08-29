"""Exact direct pair-kernel SAT encoding for the canonical-D T6 core.

Unlike the older K-row encoding, this formula introduces rho_s(t) directly
and enforces

  O_t^-1(s)=O_u^-1(s) iff rho_s(t)=rho_s(u)

for every target and row pair.  It is equivalent to existence of permutation
rows K_s but exposes the pair-clique obstruction to unit propagation.
"""

from __future__ import annotations

import argparse
import itertools
import threading
import time

import e677_fiber7_T6_kernel_pair_clique_search as clique
import e677_fiber7_T6_kernel_sat as kernel
from pysat.solvers import Solver  # type: ignore


def build(fixed_D=None, enforce_kernel=True):
    clauses = []
    next_variable = 1
    O7 = []
    for _ in range(kernel.N):
        variables, next_variable = kernel.add_permutation(clauses, next_variable)
        O7.append(variables)

    for total in range(kernel.N):
        for value in range(kernel.N):
            kernel.add_exactly_one(
                clauses,
                [O7[row][(total - row) % kernel.N][value] for row in range(kernel.N)],
            )

    for row in range(kernel.N):
        clauses.append([-O7[row][0][0]])
    for left in range(kernel.N):
        for right in range(left + 1, kernel.N):
            differences = []
            for inp in range(kernel.N):
                difference = next_variable
                next_variable += 1
                differences.append(difference)
                for value in range(kernel.N):
                    clauses.append(
                        [-difference, -O7[left][inp][value], -O7[right][inp][value]]
                    )
            clauses.append(differences)

    A, next_variable = kernel.add_permutation(clauses, next_variable)
    clauses.append([A[0][0]])
    D_selectors = list(
        range(next_variable, next_variable + len(kernel.CANONICAL_D))
    )
    next_variable += len(D_selectors)
    kernel.add_exactly_one(clauses, D_selectors)
    if fixed_D is not None:
        clauses.append([D_selectors[fixed_D]])

    rho = []
    for _s in range(kernel.N):
        target_rows = []
        for _t in range(kernel.N):
            literals = list(range(next_variable, next_variable + kernel.N))
            next_variable += kernel.N
            kernel.add_exactly_one(clauses, literals)
            target_rows.append(literals)
        rho.append(target_rows)

    for D_selector, D in zip(D_selectors, kernel.CANONICAL_D):
        for s in range(kernel.N):
            for t in range(kernel.N):
                for q in range(kernel.N):
                    for a in range(kernel.N):
                        value = (D[(q - t) % kernel.N] - a) % kernel.N
                        clauses.append(
                            [-D_selector, -O7[t][s][q], -A[q][a], rho[s][t][value]]
                        )

    if enforce_kernel:
        # Forbid the two ways in which the kernels can disagree.
        for s in range(kernel.N):
            for left in range(kernel.N):
                for right in range(left + 1, kernel.N):
                    # Same inverse position but different rho values.
                    for z in range(kernel.N):
                        for left_value in range(kernel.N):
                            for right_value in range(kernel.N):
                                if left_value == right_value:
                                    continue
                                clauses.append(
                                    [
                                        -O7[left][z][s],
                                        -O7[right][z][s],
                                        -rho[s][left][left_value],
                                        -rho[s][right][right_value],
                                    ]
                                )
                    # Different inverse positions but the same rho value.
                    for left_z in range(kernel.N):
                        for right_z in range(kernel.N):
                            if left_z == right_z:
                                continue
                            for value in range(kernel.N):
                                clauses.append(
                                    [
                                        -O7[left][left_z][s],
                                        -O7[right][right_z][s],
                                        -rho[s][left][value],
                                        -rho[s][right][value],
                                    ]
                                )
    return clauses, O7, A, rho, D_selectors, next_variable - 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seconds", type=float, default=180.0)
    parser.add_argument("--solver", default="glucose42")
    parser.add_argument("--d-index", type=int, choices=range(4))
    args = parser.parse_args()

    clauses, O_vars, A_vars, rho_vars, D_selectors, variable_count = build(args.d_index)
    print(
        f"pair-kernel encoding: variables={variable_count}; clauses={len(clauses)}; "
        f"D={args.d_index if args.d_index is not None else 'all'}; "
        f"seconds={args.seconds}; solver={args.solver}",
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
            print(f"status=UNKNOWN; elapsed={time.time()-started:.3f}s; stats={stats}")
            return 3
        if status is False:
            print(
                f"PAIR-KERNEL T6 UNSAT; D={args.d_index}; "
                f"elapsed={time.time()-started:.3f}s; stats={stats}"
            )
            return 2
        model = solver.get_model()

    positive = {literal for literal in model if literal > 0}
    D_index = next(
        index for index, selector in enumerate(D_selectors) if selector in positive
    )
    D = kernel.CANONICAL_D[D_index]
    O7 = tuple(kernel.decode_permutation(model, row) for row in O_vars)
    A = kernel.decode_permutation(model, A_vars)
    K = clique.reconstruct_K(O7, A, D)
    clique.audit(O7, A, D, K)
    print(
        f"PAIR-KERNEL T6 CORE; D={''.join(map(str,D))}; A={''.join(map(str,A))}; "
        f"profile={clique.kernel_profile(O7)}; elapsed={time.time()-started:.3f}s; "
        f"stats={stats}"
    )
    print(f"O7={clique.render(O7)}")
    print(f"K={clique.render(K)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
