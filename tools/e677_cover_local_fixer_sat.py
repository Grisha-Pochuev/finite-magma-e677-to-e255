"""Exact local fibre equations around a Good base point in an E677 cover.

For p=x*x, q=p*x and r=x*q, write the five fibre-permutation families

    A_j=P[q,j,x], B_i=P[x,i,q], C_i=P[x,i,r],
    F_j=P[x,j,x], G_i=P[p,i,x].

E677 at the base pairs (x,q) and (x,x) gives the two nested equations encoded
below.  The formula asks whether A_j(0) can avoid 0 for every j, i.e. whether
the local system can support a Bad lifted point over x.
"""

from __future__ import annotations

import argparse
import itertools
import sys
import threading
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools" / "vendor" / "python_sat311"))
from pysat.solvers import Solver  # type: ignore


def exactly_one(clauses: list[list[int]], literals: list[int]) -> None:
    clauses.append(literals)
    for left, right in itertools.combinations(literals, 2):
        clauses.append([-left, -right])


class Variables:
    def __init__(self, fibre: int) -> None:
        self.fibre = fibre
        self.next_variable = 1
        self.families = {name: self._family() for name in "ABCFG"}

    def _family(self) -> list[list[list[int]]]:
        family = []
        for _ in range(self.fibre):
            permutation = []
            for _ in range(self.fibre):
                row = list(range(self.next_variable, self.next_variable + self.fibre))
                self.next_variable += self.fibre
                permutation.append(row)
            family.append(permutation)
        return family


def build_formula(fibre: int, include_rx: bool) -> tuple[Variables, list[list[int]]]:
    variables = Variables(fibre)
    a, b, c, f, g = (variables.families[name] for name in "ABCFG")
    clauses: list[list[int]] = []

    for family in (a, b, c, f, g):
        for permutation in family:
            for inp in range(fibre):
                exactly_one(clauses, permutation[inp])
            for value in range(fibre):
                exactly_one(clauses, [permutation[inp][value] for inp in range(fibre)])

    # Bad target zero: no row over q fixes fibre point zero.
    for row_fibre in range(fibre):
        clauses.append([-a[row_fibre][0][0]])

    # E677 at (x_i,q_j): A_j(C_i(B_{A_j(i)}(j)))=i.
    for i in range(fibre):
        for j in range(fibre):
            for a_value in range(fibre):
                for b_value in range(fibre):
                    for c_value in range(fibre):
                        clauses.append(
                            [
                                -a[j][i][a_value],
                                -b[a_value][j][b_value],
                                -c[i][b_value][c_value],
                                a[j][c_value][i],
                            ]
                        )

    if include_rx:
        # E677 at the base pair (r_i,x_j), where x*r=x, r*p=q,
        # and x*q=r: B_j(K_i(F_{C_j(i)}(j)))=i.  Eliminate K_i:
        # U_i(j)=F_{C_j(i)}(j) and V_i(j)=B_j^-1(i) must have exactly
        # the same equality partition.
        u = []
        for i in range(fibre):
            u_row = []
            for j in range(fibre):
                literals = list(range(variables.next_variable, variables.next_variable + fibre))
                variables.next_variable += fibre
                exactly_one(clauses, literals)
                u_row.append(literals)
                for c_value in range(fibre):
                    for f_value in range(fibre):
                        clauses.append([-c[j][i][c_value], -f[c_value][j][f_value], literals[f_value]])
            u.append(u_row)
        for i in range(fibre):
            for j, ell in itertools.combinations(range(fibre), 2):
                # Equal U values cannot have different V values.
                for u_value in range(fibre):
                    for v_value in range(fibre):
                        for w_value in range(fibre):
                            if v_value != w_value:
                                clauses.append(
                                    [
                                        -u[i][j][u_value],
                                        -u[i][ell][u_value],
                                        -b[j][v_value][i],
                                        -b[ell][w_value][i],
                                    ]
                                )
                # Different U values cannot have equal V values.
                for u_value in range(fibre):
                    for w_value in range(fibre):
                        if u_value == w_value:
                            continue
                        for v_value in range(fibre):
                            clauses.append(
                                [
                                    -u[i][j][u_value],
                                    -u[i][ell][w_value],
                                    -b[j][v_value][i],
                                    -b[ell][v_value][i],
                                ]
                            )

    # E677 at (x_i,x_j): C_j(B_i(G_{F_j(i)}(j)))=i.
    for i in range(fibre):
        for j in range(fibre):
            for f_value in range(fibre):
                for g_value in range(fibre):
                    for b_value in range(fibre):
                        clauses.append(
                            [
                                -f[j][i][f_value],
                                -g[f_value][j][g_value],
                                -b[i][g_value][b_value],
                                c[j][b_value][i],
                            ]
                        )

    return variables, clauses


def decode(permutation: list[list[int]], model: set[int]) -> tuple[int, ...]:
    result = []
    for row in permutation:
        values = [value for value, literal in enumerate(row) if literal in model]
        if len(values) != 1:
            raise RuntimeError(f"bad one-hot permutation row: {values}")
        result.append(values[0])
    return tuple(result)


def audit(families: dict[str, list[tuple[int, ...]]], include_rx: bool) -> None:
    fibre = len(families["A"])
    a, b, c, f, g = (families[name] for name in "ABCFG")
    if any(sorted(permutation) != list(range(fibre)) for family in families.values() for permutation in family):
        raise RuntimeError("decoded map is not a permutation")
    if any(a[j][0] == 0 for j in range(fibre)):
        raise RuntimeError("decoded target has a fixer")
    for i in range(fibre):
        for j in range(fibre):
            if a[j][c[i][b[a[j][i]][j]]] != i:
                raise RuntimeError("first local E677 equation failed")
            if c[j][b[i][g[f[j][i]][j]]] != i:
                raise RuntimeError("second local E677 equation failed")
    if include_rx:
        for i in range(fibre):
            u_values = [f[c[j][i]][j] for j in range(fibre)]
            v_values = [next(value for value in range(fibre) if b[j][value] == i) for j in range(fibre)]
            if any((u_values[j] == u_values[ell]) != (v_values[j] == v_values[ell]) for j in range(fibre) for ell in range(fibre)):
                raise RuntimeError("(r,x) kernel equality failed")


def reconstruct_k(families: dict[str, list[tuple[int, ...]]]) -> list[tuple[int, ...]]:
    fibre = len(families["A"])
    b, c, f = (families[name] for name in "BCF")
    result = []
    for i in range(fibre):
        mapping = [-1] * fibre
        for j in range(fibre):
            source = f[c[j][i]][j]
            target = next(value for value in range(fibre) if b[j][value] == i)
            if mapping[source] not in (-1, target):
                raise RuntimeError("inconsistent K reconstruction")
            mapping[source] = target
        unused_sources = [value for value in range(fibre) if mapping[value] < 0]
        unused_targets = [value for value in range(fibre) if value not in mapping]
        for source, target in zip(unused_sources, unused_targets):
            mapping[source] = target
        result.append(tuple(mapping))
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fibre", type=int, default=3)
    parser.add_argument("--solver", default="glucose42")
    parser.add_argument("--seconds", type=float, default=30.0)
    parser.add_argument("--include-rx", action="store_true")
    args = parser.parse_args()
    if args.fibre < 2:
        raise SystemExit("fibre must be at least two")

    variables, clauses = build_formula(args.fibre, args.include_rx)
    print(
        f"encoding: fibre={args.fibre}; variables={variables.next_variable-1}; clauses={len(clauses)}",
        flush=True,
    )
    with Solver(name=args.solver, bootstrap_with=clauses) as solver:
        timer = threading.Timer(args.seconds, solver.interrupt)
        timer.start()
        try:
            result = solver.solve_limited(expect_interrupt=True)
        finally:
            timer.cancel()
        if result is None:
            print(f"UNKNOWN ({args.seconds:g}s)")
            return 3
        if result is False:
            print("UNSAT: the two local E677 equations force a fixer")
            return 2
        model = {literal for literal in solver.get_model() if literal > 0}

    decoded = {
        name: [decode(permutation, model) for permutation in family]
        for name, family in variables.families.items()
    }
    audit(decoded, args.include_rx)
    print("SAT: audited fixed-point-free local fibre seed")
    for name in "ABCFG":
        print(f"{name}=" + "/".join("".join(map(str, permutation)) for permutation in decoded[name]))
    if args.include_rx:
        print("K=" + "/".join("".join(map(str, permutation)) for permutation in reconstruct_k(decoded)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
