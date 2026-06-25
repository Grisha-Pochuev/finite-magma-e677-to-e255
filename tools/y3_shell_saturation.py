"""Bounded ground-congruence diagnostic for the Y3 clean shell.

This is not a model search.  It closes the local Y3 equations under E677 and
left-row injectivity up to a small term depth, then reports whether any named
Y3 endpoints are forced to coincide.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass


@dataclass(frozen=True)
class Term:
    key: str
    expr: str
    depth: int
    left: int = -1
    right: int = -1


class Saturation:
    def __init__(self, max_depth: int) -> None:
        self.max_depth = max_depth
        self.term_by_key: dict[str, int] = {}
        self.terms: list[Term] = []
        self.parent: list[int] = []
        self.rank: list[int] = []
        self.basis: set[int] = set()
        self.assumptions: list[tuple[int, int, str]] = []

    def make(self, key: str, expr: str, depth: int, left: int = -1, right: int = -1) -> int:
        if key in self.term_by_key:
            return self.term_by_key[key]
        idx = len(self.terms)
        self.term_by_key[key] = idx
        self.terms.append(Term(key, expr, depth, left, right))
        self.parent.append(idx)
        self.rank.append(0)
        return idx

    def const(self, name: str) -> int:
        idx = self.make(name, name, 0)
        self.basis.add(idx)
        return idx

    def op(self, x: int, y: int) -> int:
        term = self.terms[x]
        other = self.terms[y]
        return self.make(
            f"*({x},{y})",
            f"({term.expr}*{other.expr})",
            1 + max(term.depth, other.depth),
            x,
            y,
        )

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x: int, y: int) -> bool:
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        return True

    def same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def eq(self, x: int, y: int, label: str) -> None:
        self.assumptions.append((x, y, label))

    def add_basis_products(self, rounds: int) -> None:
        for _ in range(rounds):
            snapshot = list(self.basis)
            for x in snapshot:
                for y in snapshot:
                    xy = self.op(x, y)
                    if self.terms[xy].depth <= self.max_depth:
                        self.basis.add(xy)

    def close_once(self) -> bool:
        changed = False
        for x, y, _label in self.assumptions:
            changed = self.union(x, y) or changed

        current = list(self.basis)
        for y in current:
            for x in current:
                yx = self.op(y, x)
                inner = self.op(x, self.op(yx, y))
                if self.terms[inner].depth <= self.max_depth + 2:
                    e677 = self.op(y, inner)
                    changed = self.union(e677, x) or changed

        by_left_value: dict[tuple[int, int], int] = {}
        for idx, term in enumerate(self.terms):
            if term.left < 0:
                continue
            key = (self.find(term.left), self.find(idx))
            other = by_left_value.get(key)
            if other is None:
                by_left_value[key] = idx
            else:
                changed = self.union(term.right, self.terms[other].right) or changed

        by_pair: dict[tuple[int, int], int] = {}
        for idx, term in enumerate(self.terms):
            if term.left < 0:
                continue
            key = (self.find(term.left), self.find(term.right))
            other = by_pair.get(key)
            if other is None:
                by_pair[key] = idx
            else:
                changed = self.union(idx, other) or changed

        return changed

    def close(self, max_iterations: int = 20) -> int:
        for iteration in range(1, max_iterations + 1):
            if not self.close_once():
                return iteration
        return max_iterations


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--depth", type=int, default=3)
    parser.add_argument("--rounds", type=int, default=1)
    parser.add_argument("--max-iterations", type=int, default=20)
    parser.add_argument("--assume-u-equals-v", action="store_true")
    args = parser.parse_args()

    sat = Saturation(args.depth)
    A = sat.const("A")
    p = sat.const("p")
    x = sat.const("x")
    b = sat.const("b")
    P = sat.const("P")
    Beta = sat.const("Beta")
    H = sat.const("H")
    S = sat.const("S")
    D = sat.const("D")
    x1 = sat.const("x1")
    U = sat.const("U")
    V = sat.const("V")

    sat.eq(sat.op(p, P), A, "p*P=A")
    sat.eq(sat.op(p, A), S, "p*A=S")
    sat.eq(sat.op(x, Beta), A, "x*Beta=A")
    sat.eq(sat.op(x, A), b, "x*A=b")
    sat.eq(sat.op(x, b), x1, "x*b=x1")
    sat.eq(sat.op(b, H), A, "b*H=A")
    sat.eq(sat.op(b, A), D, "b*A=D")
    sat.eq(sat.op(p, S), U, "p*S=U")
    sat.eq(sat.op(S, A), V, "S*A=V")
    if args.assume_u_equals_v:
        sat.eq(U, V, "extra U=V")

    sat.add_basis_products(args.rounds)
    iterations = sat.close(args.max_iterations)

    names = {
        "A": A,
        "p": p,
        "x": x,
        "b": b,
        "P": P,
        "Beta": Beta,
        "H": H,
        "S": S,
        "D": D,
        "x1": x1,
        "U": U,
        "V": V,
    }
    forced: list[str] = []
    keys = list(names)
    for i, left in enumerate(keys):
        for right in keys[i + 1 :]:
            if sat.same(names[left], names[right]):
                forced.append(f"{left}={right}")

    print(f"Y3 shell saturation depth={args.depth}, rounds={args.rounds}")
    print(f"terms={len(sat.terms)}, basis={len(sat.basis)}, iterations={iterations}")
    if forced:
        print("forced named equalities:")
        for item in forced:
            print(f"  {item}")
    else:
        print("forced named equalities: none")


if __name__ == "__main__":
    main()
