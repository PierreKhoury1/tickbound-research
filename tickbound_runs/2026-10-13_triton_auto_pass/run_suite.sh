#!/usr/bin/env bash
# run_suite.sh PY LIB OUT [extra suite.py args] - run suite.py, restarting after crashes; a case that kills the
# process is recorded as crashed and skipped on the restart.
PY=$1; LIB=$2; OUT=$3; shift 3; HERE=$(cd "$(dirname "$0")" && pwd)
for attempt in $(seq 1 40); do
  timeout 1500 "$PY" "$HERE/suite.py" --lib "$LIB" --out "$OUT" "$@" && break
  last=$(grep '"status": "start"' "$OUT" | tail -1 | python3 -c 'import sys,json; l=sys.stdin.read().strip(); print(json.loads(l)["case"] if l else "")')
  done_last=$(tail -1 "$OUT" | python3 -c 'import sys,json; l=sys.stdin.read().strip(); d=json.loads(l) if l else {}; print(d.get("status",""))')
  if [ -n "$last" ] && [ "$done_last" = "start" ]; then echo "{\"case\": \"$last\", \"lib\": \"$LIB\", \"status\": \"crashed\"}" >> "$OUT"; echo "CRASH in $last, restarting"; else break; fi
done
