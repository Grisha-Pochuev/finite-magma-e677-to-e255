#!/usr/bin/env bash
set -uo pipefail

PROVER="${1:?prover: e or vampire}"
MODE="${2:?mode}"
VARIANT="${3:?variant}"
SLOT="${4:?slot}"
ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
RUN_DIR="$ROOT/run-output/slot-$SLOT"
BASE="$ROOT/experiments/github-runs/fixed-eta-2026-07-11/problem.p"
PROBLEM="$RUN_DIR/problem-$VARIANT.p"
LOG="$RUN_DIR/${PROVER}-${MODE}-${VARIANT}.log"
mkdir -p "$RUN_DIR"
cp "$BASE" "$PROBLEM"

python3 - "$PROBLEM" "$VARIANT" <<'PY'
from pathlib import Path
import sys

path = Path(sys.argv[1])
variant = sys.argv[2]
text = path.read_text(encoding="utf-8")
target = "fof(fixed_eta_target, conjecture, a = z)."

if variant == "base":
    pass
elif variant == "row-image":
    text = text.replace(target, "fof(fixed_eta_target, conjecture, f(r,a) = u).")
elif variant == "expanded":
    text = text.replace(target, "fof(fixed_eta_target, conjecture, f(r,f(ib,c)) = u).")
elif variant == "contradiction":
    text = text.replace(
        target,
        "fof(not_target, axiom, a != z).\nfof(fixed_eta_target, conjecture, $false).",
    )
elif variant == "ground-boost":
    constants = ["z", "b", "c", "h", "ib", "ic", "a", "r", "u"]
    ground = ["% Explicit ground instances of E677; these do not strengthen the theory."]
    k = 0
    for x in constants:
        for y in constants:
            k += 1
            ground.append(
                f"fof(e677_g_{k:03d}, axiom, f({y},f({x},f(f({y},{x}),{y}))) = {x})."
            )
    text = text.replace(target, "\n".join(ground) + "\n\n" + target)
else:
    raise SystemExit(f"unknown variant: {variant}")

path.write_text(text, encoding="utf-8")
PY

{
  echo "slot=$SLOT"
  echo "prover=$PROVER"
  echo "mode=$MODE"
  echo "variant=$VARIANT"
  echo "started_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "commit=${GITHUB_SHA:-unknown}"
  echo "runner_os=${RUNNER_OS:-unknown}"
  echo "runner_arch=${RUNNER_ARCH:-unknown}"
  echo "nproc=$(nproc)"
  echo "memory_kb=$(awk '/MemTotal/ {print $2}' /proc/meminfo)"
} > "$RUN_DIR/metadata.txt"

set +e
if [[ "$PROVER" == "e" ]]; then
  if [[ "$MODE" == "auto" ]]; then
    CMD=(eprover --auto-schedule=4 --cpu-limit=20400 --proof-object --tstp-format "$PROBLEM")
  elif [[ "$MODE" == "sat" ]]; then
    CMD=(eprover --satauto-schedule=4 --cpu-limit=20400 --proof-object --tstp-format "$PROBLEM")
  else
    echo "unknown E mode: $MODE" | tee "$LOG"
    exit 0
  fi
elif [[ "$PROVER" == "vampire" ]]; then
  if [[ "$MODE" != "casc" && "$MODE" != "casc_sat" ]]; then
    echo "unknown Vampire mode: $MODE" | tee "$LOG"
    exit 0
  fi
  CMD=(vampire --mode "$MODE" --cores 4 -m 14500 -t 20400 --proof tptp "$PROBLEM")
else
  echo "unknown prover: $PROVER" | tee "$LOG"
  exit 0
fi

printf 'command=' >> "$RUN_DIR/metadata.txt"
printf '%q ' "${CMD[@]}" >> "$RUN_DIR/metadata.txt"
printf '\n' >> "$RUN_DIR/metadata.txt"

timeout --signal=TERM --kill-after=60s 20700s "${CMD[@]}" > "$LOG" 2>&1
STATUS=$?
set -e

{
  echo "exit_status=$STATUS"
  echo "finished_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
} >> "$RUN_DIR/metadata.txt"

{
  grep -E "SZS status|Termination reason|Refutation found|Proof found|Satisfiable|Unsatisfiable|CounterSatisfiable|Theorem" "$LOG" || true
} > "$RUN_DIR/summary.txt"

# A prover timeout or resource exhaustion is a valid experimental outcome.
exit 0
