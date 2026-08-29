"""Exact T6 check of the uniform (2,2,1,1,1) inverse-kernel layer.

The direct pair-kernel formula is augmented by equality indicators for
z_s(t)=O_t^-1(s).  Exactly two equal row pairs are required for every s;
on seven points this is precisely the block profile (2,2,1,1,1).
"""

from __future__ import annotations

import argparse
import threading
import time

import e677_fiber7_T6_kernel_pair_clique_search as clique
import e677_fiber7_T6_kernel_sat as kernel
import e677_fiber7_T6_pair_kernel_sat as pair_kernel
from pysat.card import CardEnc, EncType  # type: ignore
from pysat.solvers import Solver  # type: ignore


def parse_permutation(text):
    value = tuple(map(int, text))
    if len(value) != kernel.N or tuple(sorted(value)) != tuple(range(kernel.N)):
        raise argparse.ArgumentTypeError("expected a permutation of 0..6")
    return value


def parse_O7(text):
    rows = tuple(parse_permutation(row) for row in text.split("/"))
    if len(rows) != kernel.N:
        raise argparse.ArgumentTypeError("expected seven slash-separated rows")
    return rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seconds", type=float, default=180.0)
    parser.add_argument("--solver", default="glucose42")
    parser.add_argument("--d-index", type=int, choices=range(4))
    parser.add_argument("--phase-o7", type=parse_O7)
    parser.add_argument("--phase-a", type=parse_permutation)
    args = parser.parse_args()

    clauses, O_vars, A_vars, rho_vars, D_selectors, variable_count = pair_kernel.build(
        args.d_index
    )
    equality_variables = []
    for s in range(kernel.N):
        row_equalities = []
        for left in range(kernel.N):
            for right in range(left + 1, kernel.N):
                equality = variable_count + 1
                variable_count += 1
                row_equalities.append(equality)
                for left_z in range(kernel.N):
                    for right_z in range(kernel.N):
                        clause = [
                            -O_vars[left][left_z][s],
                            -O_vars[right][right_z][s],
                            equality if left_z == right_z else -equality,
                        ]
                        clauses.append(clause)
        card = CardEnc.equals(
            lits=row_equalities,
            bound=2,
            top_id=variable_count,
            encoding=EncType.seqcounter,
        )
        clauses.extend(card.clauses)
        variable_count = max(variable_count, card.nv)
        equality_variables.extend(row_equalities)

    phases = []
    if args.phase_o7 is not None:
        phases.extend(
            O_vars[row][inp][args.phase_o7[row][inp]]
            for row in range(kernel.N)
            for inp in range(kernel.N)
        )
    if args.phase_a is not None:
        phases.extend(A_vars[inp][args.phase_a[inp]] for inp in range(kernel.N))

    print(
        f"uniform-two-pair: variables={variable_count}; clauses={len(clauses)}; "
        f"D={args.d_index if args.d_index is not None else 'all'}; "
        f"seconds={args.seconds}",
        flush=True,
    )
    started = time.time()
    with Solver(name=args.solver, bootstrap_with=clauses) as solver:
        if phases:
            solver.set_phases(phases)
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
                f"UNIFORM TWO-PAIR T6 UNSAT; D={args.d_index}; "
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
    profiles = clique.kernel_profile(O7)
    if any(profile != (2, 2, 1, 1, 1) for profile in profiles):
        raise AssertionError(profiles)
    print(
        f"UNIFORM TWO-PAIR T6 CORE; D={''.join(map(str,D))}; "
        f"A={''.join(map(str,A))}; profile={profiles}; "
        f"elapsed={time.time()-started:.3f}s; stats={stats}"
    )
    print(f"O7={clique.render(O7)}")
    print(f"K={clique.render(K)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
