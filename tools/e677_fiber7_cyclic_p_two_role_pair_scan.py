"""Exhaust one normalized two-role isotope rank/relative-cycle class."""

from __future__ import annotations

import argparse
import itertools
import threading
import time

import e677_fiber7_cyclic_p_isotope_t0267_sat as isotope
import e677_fiber7_cyclic_p_reduced_t0267_sat as routing
import e677_fiber7_cyclic_p_reduced_t6_sat as reduced
import e677_size7_orbit_full_sat as full
from pysat.solvers import Solver  # type: ignore


N = 7
IDENTITY = tuple(range(N))


def difference_rank(permutation: tuple[int, ...]) -> int:
    return len({(permutation[x] - x) % N for x in range(N)})


def inverse(permutation: tuple[int, ...]):
    result = [0] * N
    for inp, value in enumerate(permutation):
        result[value] = inp
    return tuple(result)


def relative(left: tuple[int, ...], right: tuple[int, ...]):
    inverse_left = inverse(left)
    return tuple(inverse_left[right[inp]] for inp in range(N))


def cycle_type(permutation: tuple[int, ...]):
    seen = set()
    lengths = []
    for start in range(N):
        if start in seen:
            continue
        value = start
        length = 0
        while value not in seen:
            seen.add(value)
            length += 1
            value = permutation[value]
        lengths.append(length)
    return tuple(sorted(lengths))


def domains(branch: str):
    permutations = list(itertools.permutations(range(N)))
    normalized_a = [
        p for p in permutations if p[0] == 0 and p[1] == 1 and p != IDENTITY
    ]
    normalized_b = [p for p in permutations if p[0] == 0 and p != IDENTITY]
    nonidentity = [p for p in permutations if p != IDENTITY]
    if branch == "AB":
        return normalized_a, normalized_b
    if branch == "AD":
        return normalized_a, nonidentity
    if branch == "BD":
        return normalized_b, nonidentity
    raise AssertionError(branch)


def candidates(branch: str, left_rank: int, right_rank: int, target_cycle):
    left_domain, right_domain = domains(branch)
    return [
        (left, right)
        for left in left_domain
        if left_rank == 0 or difference_rank(left) == left_rank
        for right in right_domain
        if (right_rank == 0 or difference_rank(right) == right_rank)
        and (
            target_cycle is None
            or cycle_type(relative(left, right)) == target_cycle
        )
    ]


def decode_permutation(model, variables):
    positive = {literal for literal in model if literal > 0}
    return tuple(
        next(value for value in range(N) if variables[inp][value] in positive)
        for inp in range(N)
    )


def audit_model(model, V, A_vars, B_vars, D_vars, include_t0: bool):
    A = decode_permutation(model, A_vars)
    B = decode_permutation(model, B_vars)
    D = decode_permutation(model, D_vars)
    C_table = reduced.decode(model, reduced.C)
    for q in range(N):
        for u in range(N):
            if D[C_table[q][u]] != (A[q] + B[u]) % N:
                raise AssertionError("isotope audit failed")
    O7 = reduced.decode(model, reduced.O7Q)
    H_table = reduced.decode(model, reduced.H)
    O0 = routing.decode_v(model, V)
    O2, O4, O6 = reduced.reconstruct(C_table, H_table)
    W = [[O7[s][(t - s) % N] for s in range(N)] for t in range(N)]
    O1 = routing.inverse_rows(W)
    operations = [[row[:] for row in full.BASE] for _ in range(8)]
    for q, table in (
        (0, O0), (1, O1), (2, O2), (4, O4), (6, O6), (7, O7)
    ):
        operations[q] = table
    audited = (0, 2, 6, 7) if include_t0 else (2, 6, 7)
    failures = {
        d: sum(
            not full.holds(operations, d, s, t)
            for s in range(N) for t in range(N)
        )
        for d in audited
    }
    if any(failures.values()):
        raise AssertionError(f"original identity audit failed: {failures}")
    return A, B, D, C_table, H_table, O7, failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--branch", choices=("AB", "AD", "BD"), default="AB")
    parser.add_argument("--left-rank", type=int, required=True)
    parser.add_argument("--right-rank", type=int, required=True)
    parser.add_argument("--relative-cycle", required=True)
    parser.add_argument("--per-pair-seconds", type=float, default=2.0)
    parser.add_argument("--solver", default="glucose42")
    parser.add_argument("--skip-t0", action="store_true")
    parser.add_argument("--fix-left")
    parser.add_argument("--fix-right")
    parser.add_argument("--right-affine-nontranslation", action="store_true")
    parser.add_argument("--fix-right-only")
    args = parser.parse_args()
    target_cycle = (
        None
        if args.relative_cycle == "any"
        else tuple(sorted(int(value) for value in args.relative_cycle.split(",")))
    )
    if target_cycle is not None and sum(target_cycle) != N:
        raise SystemExit("--relative-cycle lengths must sum to 7")
    pairs = candidates(
        args.branch, args.left_rank, args.right_rank, target_cycle
    )
    if args.right_affine_nontranslation:
        affine_right = {
            tuple((slope * x + shift) % N for x in range(N))
            for slope in range(2, N)
            for shift in range(N)
        }
        pairs = [pair for pair in pairs if pair[1] in affine_right]
    if args.fix_right_only:
        fixed_right = tuple(int(value) for value in args.fix_right_only)
        if len(fixed_right) != N or sorted(fixed_right) != list(range(N)):
            raise SystemExit("--fix-right-only must be a seven-digit permutation")
        pairs = [pair for pair in pairs if pair[1] == fixed_right]
    if bool(args.fix_left) != bool(args.fix_right):
        raise SystemExit("--fix-left and --fix-right must be used together")
    if args.fix_left:
        fixed_pair = (
            tuple(int(value) for value in args.fix_left),
            tuple(int(value) for value in args.fix_right),
        )
        if fixed_pair not in pairs:
            raise SystemExit("fixed pair is not in the requested class")
        pairs = [fixed_pair]

    clauses, V, A_vars, B_vars, D_vars, variable_count = isotope.build(
        not args.skip_t0
    )
    systems = {"A": A_vars, "B": B_vars, "D": D_vars}
    third = ({"A", "B", "D"} - set(args.branch)).pop()
    for value in range(N):
        clauses.append([systems[third][value][value]])

    print(
        f"encoding: variables={variable_count}; clauses={len(clauses)}; "
        f"branch={args.branch}; ranks=({args.left_rank},{args.right_rank}); "
        f"relative={target_cycle}; pairs={len(pairs)}; t0={not args.skip_t0}; "
        f"solver={args.solver}",
        flush=True,
    )
    if not pairs:
        return 2
    selected_vars = [systems[name] for name in args.branch]
    counts = {"SAT": 0, "UNSAT": 0, "UNKNOWN": 0}
    unknown = []
    started = time.time()
    with Solver(name=args.solver, bootstrap_with=clauses) as solver:
        for index, pair in enumerate(pairs, 1):
            assumptions = [
                variables[inp][value]
                for variables, permutation in zip(selected_vars, pair)
                for inp, value in enumerate(permutation)
            ]
            timer = threading.Timer(max(0.05, args.per_pair_seconds), solver.interrupt)
            timer.daemon = True
            timer.start()
            try:
                status = solver.solve_limited(
                    assumptions=assumptions, expect_interrupt=True
                )
            finally:
                timer.cancel()
            if status is True:
                counts["SAT"] += 1
                result = audit_model(
                    solver.get_model(), V, A_vars, B_vars, D_vars,
                    not args.skip_t0,
                )
                A, B, D, C_table, H_table, O7, failures = result
                print(
                    f"SAT T0267 CORE; pair={index}/{len(pairs)}; "
                    f"A={''.join(map(str,A))}; B={''.join(map(str,B))}; "
                    f"D={''.join(map(str,D))}; failures={failures}; "
                    f"elapsed={time.time()-started:.3f}s"
                )
                for name, table in (("C", C_table), ("H", H_table), ("O7", O7)):
                    print(f"{name}={routing.render(table)}")
                return 0
            if status is False:
                counts["UNSAT"] += 1
            else:
                counts["UNKNOWN"] += 1
                unknown.append(pair)
                solver.clear_interrupt()
            if index % 50 == 0 or index == len(pairs):
                print(
                    f"progress={index}/{len(pairs)}; counts={counts}; "
                    f"elapsed={time.time()-started:.3f}s",
                    flush=True,
                )
    print(f"PAIR CLASS COMPLETE; counts={counts}; elapsed={time.time()-started:.3f}s")
    for left, right in unknown[:20]:
        print(
            f"UNKNOWN left={''.join(map(str,left))}; "
            f"right={''.join(map(str,right))}"
        )
    if len(unknown) > 20:
        print(f"omitted-UNKNOWN={len(unknown)-20}")
    return 2 if not unknown else 3


if __name__ == "__main__":
    raise SystemExit(main())
