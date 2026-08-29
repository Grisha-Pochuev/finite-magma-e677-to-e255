#!/usr/bin/env python3
"""Run the exact six-leaf continuation of order-9 three-Bad top form 2.

The audited main checker is left unchanged.  This wrapper verifies its exact
Git blob, inserts one narrowly scoped command-line mode in memory, and executes
that patched source with the original checker path as ``__file__``.  The six
leaves are precisely the cases in equation (19) of
``lemmas/e677_order9_three_bad_root_and_case2_reduction.md``.
"""

from __future__ import annotations

import argparse
import hashlib
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CHECKER = ROOT / "tools" / "e677_order9_no_hit_bad_count_sat.py"
EXPECTED_GIT_BLOB_SHA = "efe356acd0047eef8ae5645b2cb04ac2a493632d"

PARSER_MARKER = '    parser.add_argument("--bad3-case2-reduction", action="store_true")\n'
BRANCH_MARKER = "                if args.bad3_case2_reduction:\n"


def git_blob_sha(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def patched_source() -> str:
    data = CHECKER.read_bytes()
    observed = git_blob_sha(data)
    if observed != EXPECTED_GIT_BLOB_SHA:
        raise RuntimeError(
            "refusing to patch an unreviewed checker: "
            f"expected Git blob {EXPECTED_GIT_BLOB_SHA}, got {observed}"
        )

    source = data.decode("utf-8")
    if source.count(PARSER_MARKER) != 1:
        raise RuntimeError("the parser insertion marker is not unique")
    source = source.replace(
        PARSER_MARKER,
        PARSER_MARKER
        + '    parser.add_argument("--bad3-case2-paused-continuation", action="store_true")\n',
        1,
    )

    if source.count(BRANCH_MARKER) != 1:
        raise RuntimeError("the case-split insertion marker is not unique")

    continuation = '''                if args.bad3_case2_paused_continuation:
                    if index != 2:
                        continue
                    # Exact paused continuation after the sole surviving root
                    # (0,2) with 0*2=3 Good.  Put a=0*3 and k=a*0; E677
                    # forces 3*k=2.  Equation (19) leaves exactly these six
                    # residual relabelling representatives.
                    paused_leaves = (
                        (0, 1),
                        (2, 1),
                        (4, 1),
                        (4, 3),
                        (4, 4),
                        (4, 5),
                    )
                    for a_value, hinge in paused_leaves:
                        split_cases.append((
                            index,
                            f"{name}; root=(0,2),u=3,a={a_value},k={hinge}",
                            [
                                *structural,
                                bad3_root_witnesses_by_pair[(0, 2)][3],
                                cell(0, 3, a_value),
                                cell(a_value, 0, hinge),
                                cell(3, hinge, 2),
                            ],
                        ))
                elif args.bad3_case2_reduction:
'''
    return source.replace(BRANCH_MARKER, continuation, 1)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--solver", default="cadical195")
    parser.add_argument("--per-leaf-seconds", type=int, default=30)
    parser.add_argument("--conflict-budget", type=int, default=50_000)
    args = parser.parse_args()

    forwarded = [
        "--min-bad",
        "3",
        "--max-bad",
        "3",
        "--scan-bad3-structural",
        "--bad3-frontier-only",
        "--bad3-case",
        "2",
        "--bad3-case2-paused-continuation",
        "--solver",
        args.solver,
        "--per-count-seconds",
        str(args.per_leaf_seconds),
        "--conflict-budget",
        str(args.conflict_budget),
    ]

    source = patched_source()
    print(f"base-checker-git-blob: {EXPECTED_GIT_BLOB_SHA}", flush=True)
    print(
        "paused-leaves: (a,k)=(0,1),(2,1),(4,1),(4,3),(4,4),(4,5)",
        flush=True,
    )
    print(f"forwarded: {' '.join(forwarded)}", flush=True)

    sys.argv = [str(CHECKER), *forwarded]
    namespace = {
        "__name__": "__main__",
        "__file__": str(CHECKER),
        "__package__": None,
    }
    exec(compile(source, str(CHECKER), "exec"), namespace)


if __name__ == "__main__":
    main()
