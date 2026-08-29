#!/usr/bin/env python3
"""Normalize one six-leaf SAT run into a compact JSON record."""

from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path


CASE_RE = re.compile(
    r"bad3 case 02/24 split (?P<ordinal>\d+)/6 (?P<name>.*): "
    r"(?P<status>SAT|UNSAT|UNKNOWN); elapsed=(?P<elapsed>[0-9.]+)s; "
    r"conflicts=(?P<conflicts>\d+)"
)
BASE_BLOB_RE = re.compile(r"base-checker-git-blob: ([0-9a-f]{40})")


def cpu_name() -> str:
    try:
        for line in Path("/proc/cpuinfo").read_text(encoding="utf-8").splitlines():
            if line.lower().startswith("model name"):
                return line.split(":", 1)[1].strip()
    except OSError:
        pass
    return "unknown"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--phase", choices=("smoke", "full"), required=True)
    parser.add_argument("--solver", required=True)
    parser.add_argument("--log", type=Path, required=True)
    parser.add_argument("--exit-code", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    text = args.log.read_text(encoding="utf-8", errors="replace")
    leaves = []
    for match in CASE_RE.finditer(text):
        leaves.append(
            {
                "ordinal": int(match.group("ordinal")),
                "name": match.group("name"),
                "status": match.group("status"),
                "elapsed_seconds": float(match.group("elapsed")),
                "conflicts": int(match.group("conflicts")),
            }
        )

    counts = {
        status: sum(leaf["status"] == status for leaf in leaves)
        for status in ("SAT", "UNSAT", "UNKNOWN")
    }
    blob_match = BASE_BLOB_RE.search(text)
    has_verified_model = "status: VERIFIED NO-HIT COUNTEREXAMPLE" in text
    technical_reason = ""

    if args.exit_code not in (0, 2, 3):
        normalized = "TECHNICAL_FAILURE"
        technical_reason = f"unexpected checker exit code {args.exit_code}"
    elif counts["SAT"]:
        if args.exit_code == 0 and has_verified_model:
            normalized = "VERIFIED_NO_HIT_COUNTEREXAMPLE"
        else:
            normalized = "TECHNICAL_FAILURE"
            technical_reason = "SAT line without the checker's verified-model marker"
    elif len(leaves) != 6:
        normalized = "TECHNICAL_FAILURE"
        technical_reason = f"expected six leaf records, found {len(leaves)}"
    elif counts["UNSAT"] == 6 and args.exit_code == 2:
        normalized = "ALL_SIX_UNSAT"
    elif counts["UNKNOWN"] and args.exit_code == 3:
        normalized = "BOUNDED_UNKNOWN"
    else:
        normalized = "TECHNICAL_FAILURE"
        technical_reason = "exit code and six-leaf statuses are inconsistent"

    record = {
        "phase": args.phase,
        "solver": args.solver,
        "normalized_result": normalized,
        "technical_reason": technical_reason,
        "raw_exit_code": args.exit_code,
        "leaf_count": len(leaves),
        "sat_count": counts["SAT"],
        "unsat_count": counts["UNSAT"],
        "unknown_count": counts["UNKNOWN"],
        "verified_model_marker": has_verified_model,
        "base_checker_git_blob": blob_match.group(1) if blob_match else "missing",
        "commit_sha": os.environ.get("GITHUB_SHA", "local"),
        "cpu": cpu_name(),
        "leaves": leaves,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(record, indent=2))
    return 1 if normalized == "TECHNICAL_FAILURE" else 0


if __name__ == "__main__":
    raise SystemExit(main())
