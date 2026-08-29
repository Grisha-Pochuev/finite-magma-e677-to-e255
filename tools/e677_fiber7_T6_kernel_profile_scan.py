"""Scan the nine remaining block profiles of ker(t -> O7_t^-1(0))."""

from __future__ import annotations

import argparse
import itertools
import threading
import time

import e677_fiber7_T6_kernel_sat as kernel
from pysat.solvers import Solver  # type: ignore


PROFILES = (
    (5, 1, 1),
    (4, 2, 1),
    (3, 3, 1),
    (3, 2, 2),
    (4, 1, 1, 1),
    (3, 2, 1, 1),
    (2, 2, 2, 1),
    (3, 1, 1, 1, 1),
    (2, 2, 1, 1, 1),
)


def conditional_exact(clauses, literals, selector, bound):
    for subset in itertools.combinations(literals, bound + 1):
        clauses.append([-selector, *(-literal for literal in subset)])
    for subset in itertools.combinations(
        literals, len(literals) - bound + 1
    ):
        clauses.append([-selector, *subset])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--per-profile-seconds", type=float, default=20.0)
    parser.add_argument("--solver", default="glucose42")
    args = parser.parse_args()

    clauses, O7_vars, A_vars, K_vars, D_selectors, variable_count = kernel.build()
    next_variable = variable_count + 1
    count_variables = []
    for z in range(kernel.N):
        row = list(range(next_variable, next_variable + kernel.N + 1))
        next_variable += kernel.N + 1
        count_variables.append(row)
        kernel.add_exactly_one(clauses, row)
        witnesses = [O7_vars[t][z][0] for t in range(kernel.N)]
        for count, selector in enumerate(row):
            conditional_exact(clauses, witnesses, selector, count)

    profile_selectors = list(
        range(next_variable, next_variable + len(PROFILES))
    )
    next_variable += len(PROFILES)
    for profile, selector in zip(PROFILES, profile_selectors):
        padded = profile + (0,) * (kernel.N - len(profile))
        for count in range(kernel.N + 1):
            multiplicity = padded.count(count)
            conditional_exact(
                clauses,
                [count_variables[z][count] for z in range(kernel.N)],
                selector,
                multiplicity,
            )

    print(
        f"encoding: variables={next_variable-1}; clauses={len(clauses)}; "
        f"profiles={len(PROFILES)}; per-profile={args.per_profile_seconds}; "
        f"solver={args.solver}",
        flush=True,
    )
    results = []
    started = time.time()
    with Solver(name=args.solver, bootstrap_with=clauses) as solver:
        for profile, selector in zip(PROFILES, profile_selectors):
            timer = threading.Timer(
                max(0.05, args.per_profile_seconds), solver.interrupt
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
                results.append((profile, "UNKNOWN", None))
                solver.clear_interrupt()
            elif status is False:
                results.append((profile, "UNSAT", None))
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
                full_profile = kernel.kernel_profile(O7)
                if full_profile[0] != profile:
                    raise AssertionError((profile, full_profile))
                results.append((profile, "SAT", (D_index, full_profile)))
            print(
                f"profile={profile}; status={results[-1][1]}; "
                f"witness={results[-1][2]}; elapsed={time.time()-started:.3f}s",
                flush=True,
            )
    print(f"PROFILE SCAN COMPLETE; results={results}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
