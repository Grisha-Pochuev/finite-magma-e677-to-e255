#!/usr/bin/env python3
import argparse, csv, json
from collections import Counter
from pathlib import Path

p=argparse.ArgumentParser()
p.add_argument("--input",required=True)
p.add_argument("--out",required=True)
p.add_argument("--expected",type=int,required=True)
a=p.parse_args()
rows=[]
bad=[]
for q in Path(a.input).rglob("summary.json"):
    try:
        rows.append(json.loads(q.read_text(encoding="utf-8")))
    except Exception as e:
        bad.append({"path":str(q),"error":str(e)})
rows.sort(key=lambda r:(str(r.get("slot","")),str(r.get("profile",""))))
out=Path(a.out); out.mkdir(parents=True,exist_ok=True)
fields=["slot","problem","target","profile","raw_result","normalized_result","final_szs_status",
"raw_exit_code","monitor_exit_code","termination_reason","elapsed_seconds","peak_tree_rss_mib",
"min_mem_available_mib","max_swap_used_mib","cpu","commit_sha","artifact_name",
"theorem_found","model_found","technical_failure","worker_memory_limit_observed"]
with (out/"run-summary.csv").open("w",newline="",encoding="utf-8") as f:
    w=csv.DictWriter(f,fieldnames=fields,extrasaction="ignore"); w.writeheader(); w.writerows(rows)
counts=Counter(str(r.get("normalized_result","MISSING")) for r in rows)
payload={"expected":a.expected,"found":len(rows),"missing":max(0,a.expected-len(rows)),
         "invalid":bad,"counts":dict(sorted(counts.items())),"rows":rows}
(out/"run-summary.json").write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
lines=["# Run report","",f"- expected summaries: {a.expected}",f"- found summaries: {len(rows)}",
       f"- missing summaries: {max(0,a.expected-len(rows))}",f"- invalid summaries: {len(bad)}","",
       "## Outcomes",""]
for k,v in sorted(counts.items()): lines.append(f"- {k}: {v}")
(out/"RUN_REPORT.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
if len(rows)!=a.expected or bad:
    raise SystemExit(1)
