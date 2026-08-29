"""Exact bounded repair of a named near-T6 kernel seed.

The base formula is the complete T6 kernel abstraction.  D is fixed, while
O7 and A are constrained to Hamming balls around a supplied Latin near-core.
SAT yields an exact T6 core; UNSAT excludes the whole stated ball.
"""

from __future__ import annotations

import argparse
import threading
import time

import e677_fiber7_T6_kernel_pair_clique_search as clique
import e677_fiber7_T6_kernel_sat as kernel
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
    parser.add_argument("--o7", required=True, type=parse_O7)
    parser.add_argument("--a", required=True, type=parse_permutation)
    parser.add_argument("--d-index", required=True, type=int, choices=range(4))
    parser.add_argument("--o-radius", type=int, default=8, choices=range(50))
    parser.add_argument("--a-radius", type=int, default=2, choices=range(8))
    parser.add_argument("--seconds", type=float, default=120.0)
    parser.add_argument("--solver", default="glucose42")
    args = parser.parse_args()

    clauses, O_vars, A_vars, K_vars, D_selectors, variable_count = kernel.build()
    clauses.append([D_selectors[args.d_index]])
    O_agreements = [
        O_vars[row][inp][args.o7[row][inp]]
        for row in range(kernel.N)
        for inp in range(kernel.N)
    ]
    A_agreements = [A_vars[inp][args.a[inp]] for inp in range(kernel.N)]
    O_card = CardEnc.atleast(
        lits=O_agreements,
        bound=len(O_agreements) - args.o_radius,
        top_id=variable_count,
        encoding=EncType.seqcounter,
    )
    clauses.extend(O_card.clauses)
    variable_count = max(variable_count, O_card.nv)
    A_card = CardEnc.atleast(
        lits=A_agreements,
        bound=len(A_agreements) - args.a_radius,
        top_id=variable_count,
        encoding=EncType.seqcounter,
    )
    clauses.extend(A_card.clauses)
    variable_count = max(variable_count, A_card.nv)

    print(
        f"near-seed repair: D={args.d_index}; O-radius={args.o_radius}; "
        f"A-radius={args.a_radius}; variables={variable_count}; "
        f"clauses={len(clauses)}; seconds={args.seconds}",
        flush=True,
    )
    started = time.time()
    with Solver(name=args.solver, bootstrap_with=clauses) as solver:
        solver.set_phases(O_agreements + A_agreements)
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
                f"NEAR-SEED BALL UNSAT; O-radius={args.o_radius}; "
                f"A-radius={args.a_radius}; elapsed={time.time()-started:.3f}s; "
                f"stats={stats}"
            )
            return 2
        model = solver.get_model()

    O7 = tuple(kernel.decode_permutation(model, row) for row in O_vars)
    A = kernel.decode_permutation(model, A_vars)
    K = tuple(kernel.decode_permutation(model, row) for row in K_vars)
    D = kernel.CANONICAL_D[args.d_index]
    clique.audit(O7, A, D, K)
    O_distance = sum(
        O7[row][inp] != args.o7[row][inp]
        for row in range(kernel.N)
        for inp in range(kernel.N)
    )
    A_distance = sum(A[inp] != args.a[inp] for inp in range(kernel.N))
    if O_distance > args.o_radius or A_distance > args.a_radius:
        raise AssertionError((O_distance, A_distance))
    print(
        f"REPAIRED T6 CORE; D={''.join(map(str,D))}; "
        f"A={''.join(map(str,A))}; O-distance={O_distance}; "
        f"A-distance={A_distance}; profile={clique.kernel_profile(O7)}; "
        f"elapsed={time.time()-started:.3f}s; stats={stats}"
    )
    print(f"O7={clique.render(O7)}")
    print(f"K={clique.render(K)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
