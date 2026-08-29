"""Search the first genuinely nonaffine cyclic-isotope C class.

Add permutations A,B,D satisfying

    D(C_q(u)) = A(q) + B(u) mod 7

to the exact cyclic-P T0/T2/T6/T7 routing reduction.  The representation
gauge is normalized losslessly by A(0)=0, A(1)=1, B(0)=0.  All 252 literal
affine tables alpha*q+beta*u+gamma are blocked, so any SAT result has a
genuinely nonaffine C in the fixed fibre coordinates.
"""

from __future__ import annotations

import argparse
import itertools
import threading
import time

import e677_fiber7_cyclic_p_reduced_t0267_sat as routing
import e677_fiber7_cyclic_p_reduced_t6_sat as reduced
import e677_size7_orbit_full_sat as full
from pysat.card import CardEnc, EncType  # type: ignore
from pysat.solvers import Solver  # type: ignore


N = 7


def minimum_curvature_permutations():
    """The 294 harmonic double swaps of affine permutations on F_7."""
    result = set()
    for slope in range(1, N):
        for offset in range(N):
            affine = tuple((slope * x + offset) % N for x in range(N))
            for anchor in range(N):
                for step in range(1, N):
                    defect = list(range(N))
                    left, right = anchor, (anchor + step) % N
                    defect[left], defect[right] = defect[right], defect[left]
                    left = (anchor + 4 * step) % N
                    right = (anchor + 5 * step) % N
                    defect[left], defect[right] = defect[right], defect[left]
                    result.add(tuple(affine[defect[x]] for x in range(N)))
    if len(result) != 294:
        raise AssertionError(f"minimum-curvature D count is {len(result)}")
    return tuple(sorted(result))


def identity_center_curvature_permutations():
    """The 21 harmonic double swaps with affine centre equal to identity."""
    result = set()
    for anchor in range(N):
        for step in range(1, N):
            defect = list(range(N))
            left, right = anchor, (anchor + step) % N
            defect[left], defect[right] = defect[right], defect[left]
            left = (anchor + 4 * step) % N
            right = (anchor + 5 * step) % N
            defect[left], defect[right] = defect[right], defect[left]
            result.add(tuple(defect))
    if len(result) != 21:
        raise AssertionError(f"identity-centre D count is {len(result)}")
    return tuple(sorted(result))


def canonical_curvature_permutations():
    """Four scalar-conjugacy representatives of the 21-map gauge layer."""
    representatives = set()
    for permutation in identity_center_curvature_permutations():
        conjugates = []
        for scalar in range(1, N):
            inverse = pow(scalar, -1, N)
            conjugates.append(tuple(
                scalar * permutation[(inverse * x) % N] % N
                for x in range(N)
            ))
        representatives.add(min(conjugates))
    if len(representatives) != 4:
        raise AssertionError(
            f"canonical minimum-curvature D count is {len(representatives)}"
        )
    return tuple(sorted(representatives))


def add_identity_center_gauge_constraints(
    clauses, variable_count, A_vars, B_vars, D_vars,
    allowed_d=None, expose_transversals=False,
):
    """Add the lossless 21-map quotient and return its selector literals."""
    clauses.append([A_vars[0][0]])
    if allowed_d is None:
        allowed_d = identity_center_curvature_permutations()
    selectors = list(
        range(variable_count + 1, variable_count + 1 + len(allowed_d))
    )
    variable_count += len(allowed_d)
    clauses.append(selectors)
    for selector, permutation in zip(selectors, allowed_d):
        for inp, value in enumerate(permutation):
            clauses.append([-selector, D_vars[inp][value]])
        if expose_transversals:
            if any(permutation[permutation[x]] != x for x in range(N)):
                raise AssertionError("curvature representative is not involutive")
            # D is an involution, so D(C)=A+B is exactly C=D(A+B).
            # Expose the four defect transversals cell by cell.
            for q in range(N):
                for u in range(N):
                    for a in range(N):
                        for b in range(N):
                            clauses.append([
                                -selector,
                                -A_vars[q][a],
                                -B_vars[u][b],
                                reduced.var(
                                    reduced.C, q, u,
                                    permutation[(a + b) % N],
                                ),
                            ])

    # Residual gauge fixes A(0)=0.  Therefore B(u)=D(C_0(u)), while
    # A(q)=D(C_q(0))-B(0).  Complete both anchor compositions.
    for u in range(N):
        for c in range(N):
            c_literal = reduced.var(reduced.C, 0, u, c)
            for value in range(N):
                clauses.append([
                    -c_literal, -D_vars[c][value], B_vars[u][value]
                ])
    for q in range(N):
        for c in range(N):
            c_literal = reduced.var(reduced.C, q, 0, c)
            for d_value in range(N):
                for b0 in range(N):
                    clauses.append([
                        -c_literal,
                        -D_vars[c][d_value],
                        -B_vars[0][b0],
                        A_vars[q][(d_value - b0) % N],
                    ])
    return selectors, variable_count


def add_permutation(clauses: list[list[int]], next_variable: int):
    variables = []
    for inp in range(N):
        row = list(range(next_variable, next_variable + N))
        next_variable += N
        variables.append(row)
        full.add_exactly_one(clauses, row)
    for value in range(N):
        full.add_exactly_one(
            clauses, [variables[inp][value] for inp in range(N)]
        )
    return variables, next_variable


def build(include_t0: bool = True, normalize: bool = True):
    clauses, V, variable_count = routing.build(include_t0)
    next_variable = variable_count + 1
    A, next_variable = add_permutation(clauses, next_variable)
    B, next_variable = add_permutation(clauses, next_variable)
    D, next_variable = add_permutation(clauses, next_variable)

    # Gauge: A'=kA+p, B'=kB+q, D'=kD+p+q.
    if normalize:
        clauses.extend(([A[0][0]], [A[1][1]], [B[0][0]]))

    for q in range(N):
        for u in range(N):
            for c in range(N):
                c_literal = reduced.var(reduced.C, q, u, c)
                for a in range(N):
                    for b in range(N):
                        clauses.append([
                            -c_literal,
                            -A[q][a],
                            -B[u][b],
                            D[c][(a + b) % N],
                        ])

    # Exclude every literal affine C in these fixed coordinates.
    for alpha in range(1, N):
        for beta in range(1, N):
            for gamma in range(N):
                clauses.append([
                    -reduced.var(
                        reduced.C,
                        q,
                        u,
                        (alpha * q + beta * u + gamma) % N,
                    )
                    for q in range(N)
                    for u in range(N)
                ])
    return clauses, V, A, B, D, next_variable - 1


def decode_permutation(model: list[int], variables):
    positive = {literal for literal in model if literal > 0}
    result = []
    for inp in range(N):
        hits = [value for value in range(N) if variables[inp][value] in positive]
        if len(hits) != 1:
            raise AssertionError(f"permutation[{inp}]={hits}")
        result.append(hits[0])
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seconds", type=int, default=180)
    parser.add_argument("--solver", default="glucose42")
    parser.add_argument("--skip-t0", action="store_true")
    parser.add_argument("--single-nonlinear", choices=("A", "B", "D"))
    parser.add_argument("--free-systems", choices=("AB", "AD", "BD"))
    parser.add_argument("--d0", type=int, choices=(0, 1))
    parser.add_argument("--delta-rank", type=int, choices=range(1, N + 1))
    parser.add_argument("--fix-d")
    parser.add_argument(
        "--d-affine-class",
        choices=("translation", "pure-dilation", "mixed"),
        help="restrict D to one exact affine class over F_7",
    )
    parser.add_argument(
        "--mixed-ad-transfer",
        action="store_true",
        help=(
            "same class as normalized B=id, D=k*x+c (k!=1,c!=0), "
            "represented instead by normalized A, translated B, and D=k*x"
        ),
    )
    parser.add_argument(
        "--anchored-ad-mixed",
        action="store_true",
        help=(
            "normalized AD mixed-affine branch with the redundant anchored "
            "law D(C_q(u))=D(C_q(0))+u encoded directly"
        ),
    )
    parser.add_argument(
        "--d-min-curvature",
        action="store_true",
        help=(
            "restrict D to the complete kappa=18 nonlinear layer and expose "
            "the normalized anchor compositions directly"
        ),
    )
    parser.add_argument(
        "--d-min-curvature-gauge",
        action="store_true",
        help=(
            "lossless unnormalized gauge quotient of the kappa=18 layer: "
            "D has identity affine centre and A(0)=0"
        ),
    )
    parser.add_argument(
        "--d-min-curvature-canonical",
        action="store_true",
        help=(
            "four scalar representatives of the lossless kappa=18 gauge "
            "quotient, with C=D(A+B) encoded directly"
        ),
    )
    args = parser.parse_args()
    clauses, V, A_vars, B_vars, D_vars, variable_count = build(
        not args.skip_t0,
        normalize=not (
            args.mixed_ad_transfer
            or args.d_min_curvature_gauge
            or args.d_min_curvature_canonical
        ),
    )
    if args.anchored_ad_mixed:
        conflicting = (
            args.single_nonlinear
            or args.free_systems
            or args.d0 is not None
            or args.delta_rank is not None
            or args.fix_d
            or args.d_affine_class
            or args.mixed_ad_transfer
        )
        if conflicting:
            raise SystemExit("--anchored-ad-mixed is a complete branch restriction")
        for value in range(N):
            clauses.append([B_vars[value][value]])
        clauses.append([-A_vars[value][value] for value in range(N)])

        affine_selectors = list(
            range(variable_count + 1, variable_count + 1 + 5 * 6)
        )
        variable_count += 5 * 6
        full.add_exactly_one(clauses, affine_selectors)
        for selector, (slope, shift) in zip(
            affine_selectors,
            (
                (slope, shift)
                for slope in range(2, N)
                for shift in range(1, N)
            ),
        ):
            for inp in range(N):
                clauses.append([
                    -selector,
                    D_vars[inp][(slope * inp + shift) % N],
                ])

        # With B=id, normalization gives A(q)=D(C_q(0)), hence the
        # isotope law is exactly D(C_q(u))=D(C_q(0))+u.  These clauses are
        # redundant but expose the anchored propagation directly.
        for q in range(N):
            for u in range(N):
                for c0 in range(N):
                    c0_literal = reduced.var(reduced.C, q, 0, c0)
                    for c in range(N):
                        c_literal = reduced.var(reduced.C, q, u, c)
                        for a in range(N):
                            clauses.append([
                                -c0_literal,
                                -c_literal,
                                -D_vars[c0][a],
                                D_vars[c][(a + u) % N],
                            ])
    if args.d_min_curvature:
        conflicting = (
            args.single_nonlinear
            or args.free_systems
            or args.d0 is not None
            or args.delta_rank is not None
            or args.fix_d
            or args.d_affine_class
            or args.mixed_ad_transfer
            or args.anchored_ad_mixed
        )
        if conflicting:
            raise SystemExit("--d-min-curvature is a complete D restriction")
        allowed_d = minimum_curvature_permutations()
        selectors = list(
            range(variable_count + 1, variable_count + 1 + len(allowed_d))
        )
        variable_count += len(allowed_d)
        clauses.append(selectors)
        for selector, permutation in zip(selectors, allowed_d):
            for inp, value in enumerate(permutation):
                clauses.append([-selector, D_vars[inp][value]])

        # Complete the two anchor compositions in both directions.  The
        # original isotope clauses already give A,B -> D(C); these clauses
        # expose D(C_q(0)) -> A(q) and D(C_0(u)) -> B(u).
        for q in range(N):
            for c in range(N):
                c_literal = reduced.var(reduced.C, q, 0, c)
                for value in range(N):
                    clauses.append([
                        -c_literal, -D_vars[c][value], A_vars[q][value]
                    ])
        for u in range(N):
            for c in range(N):
                c_literal = reduced.var(reduced.C, 0, u, c)
                for value in range(N):
                    clauses.append([
                        -c_literal, -D_vars[c][value], B_vars[u][value]
                    ])
    if args.d_min_curvature_gauge:
        conflicting = (
            args.single_nonlinear
            or args.free_systems
            or args.d0 is not None
            or args.delta_rank is not None
            or args.fix_d
            or args.d_affine_class
            or args.mixed_ad_transfer
            or args.anchored_ad_mixed
            or args.d_min_curvature
            or args.d_min_curvature_canonical
        )
        if conflicting:
            raise SystemExit(
                "--d-min-curvature-gauge is a complete branch restriction"
            )
        _, variable_count = add_identity_center_gauge_constraints(
            clauses, variable_count, A_vars, B_vars, D_vars
        )
    if args.d_min_curvature_canonical:
        conflicting = (
            args.single_nonlinear
            or args.free_systems
            or args.d0 is not None
            or args.delta_rank is not None
            or args.fix_d
            or args.d_affine_class
            or args.mixed_ad_transfer
            or args.anchored_ad_mixed
            or args.d_min_curvature
            or args.d_min_curvature_gauge
        )
        if conflicting:
            raise SystemExit(
                "--d-min-curvature-canonical is a complete branch restriction"
            )
        _, variable_count = add_identity_center_gauge_constraints(
            clauses,
            variable_count,
            A_vars,
            B_vars,
            D_vars,
            allowed_d=canonical_curvature_permutations(),
            expose_transversals=True,
        )
    if args.mixed_ad_transfer:
        conflicting = (
            args.single_nonlinear
            or args.free_systems
            or args.d0 is not None
            or args.delta_rank is not None
            or args.fix_d
            or args.d_affine_class
        )
        if conflicting:
            raise SystemExit("--mixed-ad-transfer is a complete branch restriction")
        clauses.extend(([A_vars[0][0]], [A_vars[1][1]]))
        clauses.append([-A_vars[value][value] for value in range(N)])

        b_selectors = list(range(variable_count + 1, variable_count + N))
        variable_count += N - 1
        full.add_exactly_one(clauses, b_selectors)
        for selector, shift in zip(b_selectors, range(1, N)):
            for inp in range(N):
                clauses.append([
                    -selector, B_vars[inp][(inp + shift) % N]
                ])

        d_selectors = list(range(variable_count + 1, variable_count + N - 1))
        variable_count += N - 2
        full.add_exactly_one(clauses, d_selectors)
        for selector, slope in zip(d_selectors, range(2, N)):
            for inp in range(N):
                clauses.append([
                    -selector, D_vars[inp][(slope * inp) % N]
                ])
    if args.single_nonlinear:
        systems = {"A": A_vars, "B": B_vars, "D": D_vars}
        for name, variables in systems.items():
            if name == args.single_nonlinear:
                continue
            for value in range(N):
                clauses.append([variables[value][value]])
    if args.free_systems:
        if args.single_nonlinear:
            raise SystemExit("use only one of --single-nonlinear and --free-systems")
        systems = {"A": A_vars, "B": B_vars, "D": D_vars}
        selected = set(args.free_systems)
        for name, variables in systems.items():
            if name not in selected:
                for value in range(N):
                    clauses.append([variables[value][value]])
            else:
                clauses.append([-variables[value][value] for value in range(N)])
    if args.d0 is not None:
        if args.single_nonlinear != "D":
            raise SystemExit("--d0 requires --single-nonlinear D")
        clauses.append([D_vars[0][args.d0]])
    if args.delta_rank is not None:
        if args.single_nonlinear != "D":
            raise SystemExit("--delta-rank requires --single-nonlinear D")
        used = list(range(variable_count + 1, variable_count + 1 + N))
        variable_count += N
        for difference in range(N):
            witnesses = [
                D_vars[inp][(inp + difference) % N] for inp in range(N)
            ]
            for witness in witnesses:
                clauses.append([-witness, used[difference]])
            clauses.append([-used[difference], *witnesses])
        cardinality = CardEnc.equals(
            lits=used,
            bound=args.delta_rank,
            top_id=variable_count,
            encoding=EncType.seqcounter,
        )
        clauses.extend(cardinality.clauses)
        variable_count = max(variable_count, cardinality.nv)
    if args.fix_d:
        fixed_d = tuple(int(value) for value in args.fix_d)
        if len(fixed_d) != N or sorted(fixed_d) != list(range(N)):
            raise SystemExit("--fix-d must be a seven-digit permutation")
        for inp, value in enumerate(fixed_d):
            clauses.append([D_vars[inp][value]])
    if args.d_affine_class:
        if args.d_affine_class == "translation":
            slopes = (1,)
            shifts = range(1, N)
        elif args.d_affine_class == "pure-dilation":
            slopes = range(2, N)
            shifts = (0,)
        else:
            slopes = range(2, N)
            shifts = range(1, N)
        allowed_d = {
            tuple((slope * x + shift) % N for x in range(N))
            for slope in slopes
            for shift in shifts
        }
        for permutation in itertools.permutations(range(N)):
            if permutation not in allowed_d:
                clauses.append([
                    -D_vars[inp][value]
                    for inp, value in enumerate(permutation)
                ])
    print(
        f"encoding: variables={variable_count}; clauses={len(clauses)}; "
        f"t0={not args.skip_t0}; single={args.single_nonlinear}; "
        f"free-systems={args.free_systems}; d0={args.d0}; "
        f"delta-rank={args.delta_rank}; "
        f"d-affine-class={args.d_affine_class}; "
        f"mixed-ad-transfer={args.mixed_ad_transfer}; "
        f"anchored-ad-mixed={args.anchored_ad_mixed}; "
        f"d-min-curvature={args.d_min_curvature}; "
        f"d-min-curvature-gauge={args.d_min_curvature_gauge}; "
        f"d-min-curvature-canonical={args.d_min_curvature_canonical}; "
        f"solver={args.solver}",
        flush=True,
    )
    started = time.time()
    with Solver(name=args.solver, bootstrap_with=clauses) as solver:
        timer = threading.Timer(max(1, args.seconds), solver.interrupt)
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
                f"status=UNSAT; elapsed={time.time()-started:.3f}s; stats={stats}"
            )
            return 2
        model = solver.get_model()

    C_table = reduced.decode(model, reduced.C)
    A = decode_permutation(model, A_vars)
    B = decode_permutation(model, B_vars)
    D = decode_permutation(model, D_vars)
    for q in range(N):
        for u in range(N):
            if D[C_table[q][u]] != (A[q] + B[u]) % N:
                raise AssertionError("isotope audit failed")
    affine = any(
        all(
            C_table[q][u] == (alpha * q + beta * u + gamma) % N
            for q in range(N) for u in range(N)
        )
        for alpha in range(1, N)
        for beta in range(1, N)
        for gamma in range(N)
    )
    if affine:
        raise AssertionError("affine C escaped blocking clauses")

    # Reuse the exact original-identity audit from the routing script.
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
    audited = (2, 6, 7) if args.skip_t0 else (0, 2, 6, 7)
    failures = {
        d: sum(
            not full.holds(operations, d, s, t)
            for s in range(N) for t in range(N)
        )
        for d in audited
    }
    if any(failures.values()):
        raise AssertionError(f"original identity audit failed: {failures}")
    print(
        f"SAT NONAFFINE ISOTOPE T{'267' if args.skip_t0 else '0267'} CORE; "
        f"failures={failures}; elapsed={time.time()-started:.3f}s; stats={stats}"
    )
    print(f"A={''.join(map(str, A))}; B={''.join(map(str, B))}; D={''.join(map(str, D))}")
    for name, table in (("C", C_table), ("H", H_table), ("O7", O7)):
        print(f"{name}={routing.render(table)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
