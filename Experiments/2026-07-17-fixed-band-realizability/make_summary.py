#!/usr/bin/env python3
import argparse, json, os, re
from pathlib import Path

p=argparse.ArgumentParser()
p.add_argument("--slot",required=True)
p.add_argument("--problem",required=True)
p.add_argument("--target",required=True)
p.add_argument("--profile",required=True)
p.add_argument("--out-dir",required=True)
a=p.parse_args()
out=Path(a.out_dir)
def read(name):
    q=out/name
    return q.read_text(encoding="utf-8",errors="replace") if q.exists() else ""
raw=read("RESULT.txt").strip() or "MISSING_RESULT"
try:
    resource=json.loads(read("resource-summary.json"))
except Exception:
    resource={}
log=read("solver.log")
statuses=re.findall(r"SZS status\s+([A-Za-z]+)",log)
cpu="unknown"
for line in read("machine.txt").splitlines():
    if "Model name:" in line:
        cpu=line.split(":",1)[1].strip()
        break
data={
 "slot":a.slot,"problem":a.problem,"target":a.target,"profile":a.profile,
 "raw_result":raw,"normalized_result":raw,
 "final_szs_status":statuses[-1] if statuses else "",
 "raw_exit_code":resource.get("raw_exit_code"),
 "monitor_exit_code":resource.get("exit_code"),
 "termination_reason":resource.get("reason","missing"),
 "elapsed_seconds":resource.get("elapsed_seconds"),
 "peak_tree_rss_mib":resource.get("peak_tree_rss_mib"),
 "min_mem_available_mib":resource.get("min_mem_available_mib"),
 "max_swap_used_mib":resource.get("max_swap_used_mib"),
 "cpu":cpu,"commit_sha":os.environ.get("GITHUB_SHA","unknown"),
 "artifact_name":os.environ.get("ARTIFACT_NAME",""),
 "theorem_found":raw=="THEOREM",
 "model_found":raw=="COUNTERMODEL_OR_SATISFIABLE",
 "technical_failure":raw in {"TECHNICAL_FAILURE","MISSING_RESULT"},
 "worker_memory_limit_observed":bool(re.search(r"memory limit",log,re.I))
}
(out/"summary.json").write_text(json.dumps(data,indent=2)+"\n",encoding="utf-8")
