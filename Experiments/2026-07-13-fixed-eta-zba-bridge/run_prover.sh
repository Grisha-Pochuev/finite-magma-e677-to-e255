#!/usr/bin/env bash
set -euo pipefail

PROFILE=${1:?profile}
PROBLEM=${2:?problem}
OUT_DIR=${3:?out dir}
LIMIT_SECONDS=${LIMIT_SECONDS:-21000}
ROOT_DIR=$(cd "$(dirname "$0")/../.." && pwd)
RUN_DIR=$(cd "$(dirname "$0")" && pwd)
mkdir -p "$OUT_DIR"

{
  uname -a
  echo
  lscpu
  echo
  free -h
  echo
  swapon --show || true
  echo
  df -h
  echo
  echo "problem=$PROBLEM"
  echo "profile=$PROFILE"
  echo "limit_seconds=$LIMIT_SECONDS"
  echo "commit=${GITHUB_SHA:-unknown}"
} > "$OUT_DIR/machine.txt"

case "$PROFILE" in
  e-auto-4x2500)
    CMD=("$ROOT_DIR/prover-bin/eprover" --auto-schedule=4 --memory-limit=2500 --cpu-limit="$LIMIT_SECONDS" --proof-object --tstp-format "$RUN_DIR/$PROBLEM")
    ;;
  vampire-casc-4x2500)
    CMD=("$ROOT_DIR/prover-bin/vampire" --input_syntax tptp --mode casc --cores 4 -m 2500 -t "$LIMIT_SECONDS" -p tptp "$RUN_DIR/$PROBLEM")
    ;;
  vampire-casc-2x5000)
    CMD=("$ROOT_DIR/prover-bin/vampire" --input_syntax tptp --mode casc --cores 2 -m 5000 -t "$LIMIT_SECONDS" -p tptp "$RUN_DIR/$PROBLEM")
    ;;
  vampire-sat-4x2500)
    CMD=("$ROOT_DIR/prover-bin/vampire" --input_syntax tptp --mode casc --intent sat --cores 4 -m 2500 -t "$LIMIT_SECONDS" -p tptp "$RUN_DIR/$PROBLEM")
    ;;
  *)
    echo "unknown profile: $PROFILE" >&2
    exit 2
    ;;
esac

set +e
python3 "$RUN_DIR/monitor_tree.py" \
  --limit-seconds "$LIMIT_SECONDS" \
  --rss-limit-mib 12288 \
  --memavailable-min-mib 2560 \
  --samples-before-stop 3 \
  --interval 2 \
  --out-dir "$OUT_DIR" \
  -- "${CMD[@]}"
STATUS=$?
set -e

echo "$STATUS" > "$OUT_DIR/monitor-exit-code.txt"
LOG="$OUT_DIR/solver.log"
RESULT=UNKNOWN
if grep -Eq 'SZS status (Theorem|Unsatisfiable)' "$LOG"; then
  RESULT=THEOREM
elif grep -Eq 'SZS status (Satisfiable|CounterSatisfiable)' "$LOG"; then
  RESULT=COUNTERMODEL_OR_SATISFIABLE
elif [ "$STATUS" -eq 124 ]; then
  RESULT=TIME_LIMIT
elif [ "$STATUS" -eq 125 ]; then
  RESULT=MEMORY_GUARD
elif grep -Eqi 'memory limit|out of memory' "$LOG"; then
  RESULT=SOLVER_MEMORY_LIMIT
elif [ "$STATUS" -eq 0 ] || [ "$STATUS" -eq 1 ]; then
  RESULT=NO_DECISIVE_RESULT
else
  RESULT=TECHNICAL_FAILURE
fi
printf '%s\n' "$RESULT" | tee "$OUT_DIR/RESULT.txt"

case "$RESULT" in
  THEOREM|COUNTERMODEL_OR_SATISFIABLE|TIME_LIMIT|MEMORY_GUARD|SOLVER_MEMORY_LIMIT|NO_DECISIVE_RESULT)
    exit 0
    ;;
  *)
    exit 1
    ;;
esac
