"""Exact relaxation of the uniform two-pair T6 layer.

For every target, both inverse-z and rho partitions are required to have
profile (2,2,1,1,1).  Their concrete pairs may differ, but the seven vertex
degrees in the unions of the colored matchings must agree.  Every exact T6
core in the uniform layer satisfies this relaxation.
"""

from __future__ import annotations

import argparse
import threading
import time

import e677_fiber7_T6_kernel_sat as kernel
import e677_fiber7_T6_pair_kernel_sat as pair_kernel
from pysat.card import CardEnc, EncType  # type: ignore
from pysat.solvers import Solver  # type: ignore


def equality_indicator(clauses, left, right, next_variable):
    equality = next_variable
    next_variable += 1
    for left_value in range(kernel.N):
        for right_value in range(kernel.N):
            clauses.append(
                [
                    -left[left_value],
                    -right[right_value],
                    equality if left_value == right_value else -equality,
                ]
            )
    return equality, next_variable


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seconds", type=float, default=180.0)
    parser.add_argument("--solver", default="glucose42")
    parser.add_argument("--d-index", type=int, choices=range(4))
    args = parser.parse_args()

    clauses, O_vars, A_vars, rho_vars, D_selectors, variable_count = pair_kernel.build(
        args.d_index, enforce_kernel=False
    )
    next_variable = variable_count + 1
    z_edges = [[[] for _ in range(kernel.N)] for _ in range(kernel.N)]
    rho_edges = [[[] for _ in range(kernel.N)] for _ in range(kernel.N)]
    for s in range(kernel.N):
        z_for_target = []
        rho_for_target = []
        for left in range(kernel.N):
            for right in range(left + 1, kernel.N):
                z_left = [O_vars[left][z][s] for z in range(kernel.N)]
                z_right = [O_vars[right][z][s] for z in range(kernel.N)]
                z_equal, next_variable = equality_indicator(
                    clauses, z_left, z_right, next_variable
                )
                rho_equal, next_variable = equality_indicator(
                    clauses, rho_vars[s][left], rho_vars[s][right], next_variable
                )
                z_for_target.append(z_equal)
                rho_for_target.append(rho_equal)
                z_edges[left][s].append(z_equal)
                z_edges[right][s].append(z_equal)
                rho_edges[left][s].append(rho_equal)
                rho_edges[right][s].append(rho_equal)
        for literals in (z_for_target, rho_for_target):
            card = CardEnc.equals(
                lits=literals,
                bound=2,
                top_id=next_variable - 1,
                encoding=EncType.seqcounter,
            )
            clauses.extend(card.clauses)
            next_variable = max(next_variable, card.nv + 1)

    for row in range(kernel.N):
        z_degree = []
        rho_degree = []
        for target in range(kernel.N):
            z_incident = next_variable
            rho_incident = next_variable + 1
            next_variable += 2
            z_degree.append(z_incident)
            rho_degree.append(rho_incident)
            for edge in z_edges[row][target]:
                clauses.append([-edge, z_incident])
            for edge in rho_edges[row][target]:
                clauses.append([-edge, rho_incident])
            clauses.append([-z_incident, *z_edges[row][target]])
            clauses.append([-rho_incident, *rho_edges[row][target]])
        # Each target contributes at most one incident edge, because its
        # equality relation has exactly two edges.  Hence these seven
        # incidence bits are the vertex degree.  Equality is
        # sum(z)+sum(not rho)=7.
        card = CardEnc.equals(
            lits=z_degree + [-edge for edge in rho_degree],
            bound=kernel.N,
            top_id=next_variable - 1,
            encoding=EncType.seqcounter,
        )
        clauses.extend(card.clauses)
        next_variable = max(next_variable, card.nv + 1)

    variable_count = next_variable - 1
    print(
        f"uniform-profile-degree relaxation: variables={variable_count}; "
        f"clauses={len(clauses)}; D={args.d_index if args.d_index is not None else 'all'}; "
        f"seconds={args.seconds}",
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
                f"UNIFORM PROFILE-DEGREE RELAXATION UNSAT; D={args.d_index}; "
                f"elapsed={time.time()-started:.3f}s; stats={stats}"
            )
            return 2
        model = solver.get_model()

    D_index = next(
        index
        for index, selector in enumerate(D_selectors)
        if selector in {literal for literal in model if literal > 0}
    )
    O7 = tuple(kernel.decode_permutation(model, row) for row in O_vars)
    A = kernel.decode_permutation(model, A_vars)
    print(
        f"SAT UNIFORM PROFILE-DEGREE RELAXATION; "
        f"D={''.join(map(str,kernel.CANONICAL_D[D_index]))}; "
        f"A={''.join(map(str,A))}; elapsed={time.time()-started:.3f}s; stats={stats}"
    )
    print("O7=" + "/".join("".join(map(str, row)) for row in O7))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
