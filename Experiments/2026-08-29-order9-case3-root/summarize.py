#!/usr/bin/env python3
"""Normalize one exact six-outcome form-3 root scan."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


CASE_RE = re.compile(
    r"bad3 case 03/24 split (?P<ordinal>\d+)/6 (?P<name>.*): "
    r"(?P<status>SAT|UNSAT|UNKNOWN); elapsed=(?P<elapsed>[0-9.]+)s; "
    r"conflicts=(?P<conflicts>\d+)"
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--solver", required=True)
    parser.add_argument("--log", type=Path, required=True)
    parser.add_argument("--exit-code", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    text = args.log.read_text(encoding="utf-8", errors="replace")
    leaves = [
        {
            "ordinal": int(m.group("ordinal")),
            "name": m.group("name"),
            "status": m.group("status"),
            "elapsed_seconds": float(m.group("elapsed")),
            "conflicts": int(m.group("conflicts")),
        }
        for m in CASE_RE.finditer(text)
    ]
    counts = {
        status: sum(leaf["status"] == status for leaf in leaves)
        for status in ("SAT", "UNSAT", "UNKNOWN")
    }
    verified = "status: VERIFIED NO-HIT COUNTEREXAMPLE" in text
    reason = ""

    if args.exit_code not in (0, 2, 3):
        result = "TECHNICAL_FAILURE"
        reason = f"unexpected exit code {args.exit_code}"
    elif len(leaves) != 6:
        result = "TECHNICAL_FAILURE"
        reason = f"expected six leaf lines, found {len(leaves)}"
    elif counts["SAT"]:
        if args.exit_code == 0 and verified:
            result = "VERIFIED_NO_HIT_COUNTEREXAMPLE"
        else:
            result = "TECHNICAL_FAILURE"
            reason = "SAT leaf without the complete-table verifier marker"
    elif counts["UNSAT"] == 6 and args.exit_code == 2:
        result = "ALL_SIX_UNSAT"
    elif counts["UNKNOWN"] and args.exit_code == 3:
        result = "BOUNDED_UNKNOWN"
    else:
        result = "TECHNICAL_FAILURE"
        reason = "leaf statuses and exit code are inconsistent"

    record = {
        "solver": args.solver,
        "normalized_result": result,
        "technical_reason": reason,
        "raw_exit_code": args.exit_code,
        "leaf_count": len(leaves),
        "sat_count": counts["SAT"],
        "unsat_count": counts["UNSAT"],
        "unknown_count": counts["UNKNOWN"],
        "verified_model_marker": verified,
        "leaves": leaves,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(record, indent=2))
    return 1 if result == "TECHNICAL_FAILURE" else 0


if __name__ == "__main__":
    raise SystemExit(main())
