# Publication verification

The final repository-wide reproduction and status synchronization ran in
GitHub Actions as

```text
run:      33268775007
head SHA: a4547c5ea3c39bcffb7bd29f2ddf4045a51839d4
result:   success
```

The job independently reran:

```text
six canonical root outcomes / CaDiCaL195: 6/6 UNSAT;
six canonical root outcomes / Glucose42:  6/6 UNSAT;
four Good representatives / CaDiCaL195:   4/4 UNSAT;
four Good representatives / Glucose42:    4/4 UNSAT.
```

It reached the terminal marker

```text
PASS: order-9 three-Bad top form 3 is fully excluded in both engines.
```

The complete committed verifier record is `verifier-linux.txt`, Git blob

```text
8de3ab8beecc5eadb72744f08464375c39d29f05.
```

The same run applied and audited the status updates in `README.md`,
`docs/ACTIVE_FRONTIER_MIN.md`, `Experiments/START_HERE_WEB.md`, and
`Experiments/README.md`, then pushed commit

```text
a2001cb72245dc8ca548f9b3955dc9572b96d1f3.
```

All temporary active workflow files were removed afterwards.  Their exact
snapshots remain in this experiment folder.
