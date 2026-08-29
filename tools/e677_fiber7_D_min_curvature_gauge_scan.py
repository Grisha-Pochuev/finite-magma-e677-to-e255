"""Incrementally test the 21-map gauge quotient of minimum-curvature D."""

from __future__ import annotations

import argparse
import threading
import time

import e677_fiber7_cyclic_p_isotope_t0267_sat as isotope
import e677_fiber7_cyclic_p_two_role_pair_scan as pair_scan
from pysat.solvers import Solver  # type: ignore


def render(permutation):
    return "".join(map(str, permutation))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--per-d-seconds", type=float, default=10.0)
    parser.add_argument("--solver", default="glucose42")
    args = parser.parse_args()

    clauses, V, A_vars, B_vars, D_vars, variable_count = isotope.build(
        include_t0=True, normalize=False
    )
    selectors, variable_count = isotope.add_identity_center_gauge_constraints(
        clauses, variable_count, A_vars, B_vars, D_vars
    )
    allowed_d = isotope.identity_center_curvature_permutations()
    print(
        f"encoding: variables={variable_count}; clauses={len(clauses)}; "
        f"gauge-D={len(selectors)}; per-D={args.per_d_seconds}; "
        f"solver={args.solver}",
        flush=True,
    )

    counts = {"SAT": 0, "UNSAT": 0, "UNKNOWN": 0}
    unknown = []
    started = time.time()
    with Solver(name=args.solver, bootstrap_with=clauses) as solver:
        for index, (selector, permutation) in enumerate(
            zip(selectors, allowed_d), 1
        ):
            timer = threading.Timer(
                max(0.05, args.per_d_seconds), solver.interrupt
            )
            timer.daemon = True
            timer.start()
            try:
                status = solver.solve_limited(
                    assumptions=[selector], expect_interrupt=True
                )
            finally:
                timer.cancel()
            if status is True:
                counts["SAT"] += 1
                result = pair_scan.audit_model(
                    solver.get_model(), V, A_vars, B_vars, D_vars, True
                )
                A, B, D, C_table, H_table, O7, failures = result
                print(
                    f"SAT T0267 CORE; D-index={index}/{len(selectors)}; "
                    f"A={render(A)}; B={render(B)}; D={render(D)}; "
                    f"failures={failures}; elapsed={time.time()-started:.3f}s"
                )
                for name, table in (("C", C_table), ("H", H_table), ("O7", O7)):
                    print(f"{name}={pair_scan.routing.render(table)}")
                return 0
            if status is False:
                counts["UNSAT"] += 1
            else:
                counts["UNKNOWN"] += 1
                unknown.append((index, permutation))
                solver.clear_interrupt()
            if index % 7 == 0 or index == len(selectors):
                print(
                    f"progress={index}/{len(selectors)}; counts={counts}; "
                    f"elapsed={time.time()-started:.3f}s",
                    flush=True,
                )

    print(
        f"GAUGE LAYER COMPLETE; counts={counts}; "
        f"elapsed={time.time()-started:.3f}s"
    )
    for index, permutation in unknown:
        print(f"UNKNOWN index={index}; D={render(permutation)}")
    return 2 if not unknown else 3


if __name__ == "__main__":
    raise SystemExit(main())
