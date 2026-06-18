"use strict";

function permutations(n) {
  const out = [];
  const used = Array(n).fill(false);
  const cur = [];
  function rec() {
    if (cur.length === n) {
      out.push(cur.slice());
      return;
    }
    for (let i = 0; i < n; i++) {
      if (!used[i]) {
        used[i] = true;
        cur.push(i);
        rec();
        cur.pop();
        used[i] = false;
      }
    }
  }
  rec();
  return out;
}

function satisfiesE677(table) {
  const n = table.length;
  for (let x = 0; x < n; x++) {
    for (let y = 0; y < n; y++) {
      const yx = table[y][x];
      const yx_y = table[yx][y];
      const inner = table[x][yx_y];
      const rhs = table[y][inner];
      if (rhs !== x) return false;
    }
  }
  return true;
}

function satisfiesE255(table) {
  const n = table.length;
  for (let x = 0; x < n; x++) {
    const sx = table[x][x];
    const t = table[sx][x];
    const rhs = table[t][x];
    if (rhs !== x) return false;
  }
  return true;
}

function columnHasSelf(table, x) {
  for (let y = 0; y < table.length; y++) {
    if (table[y][x] === x) return true;
  }
  return false;
}

function summarize(table) {
  return table.map((row) => row.join(" ")).join("\n");
}

function enumerate(n) {
  const perms = permutations(n);
  const table = Array(n);
  let total = 0;
  let e677 = 0;
  let e677not255 = 0;
  let firstCounterexample = null;

  function rec(row) {
    if (row === n) {
      total++;
      if (satisfiesE677(table)) {
        e677++;
        if (!satisfiesE255(table)) {
          e677not255++;
          if (!firstCounterexample) firstCounterexample = table.map((r) => r.slice());
        }
      }
      return;
    }

    for (const p of perms) {
      table[row] = p;
      rec(row + 1);
    }
  }

  rec(0);

  console.log(`n=${n}`);
  console.log(`  checked left-quasigroup tables: ${total}`);
  console.log(`  satisfying E677: ${e677}`);
  console.log(`  satisfying E677 but not E255: ${e677not255}`);
  if (firstCounterexample) {
    console.log("  first counterexample table:");
    console.log(summarize(firstCounterexample));
    for (let x = 0; x < n; x++) {
      if (!columnHasSelf(firstCounterexample, x)) {
        console.log(`  missing self in column: ${x}`);
      }
    }
  }
}

const maxN = Number(process.argv[2] || 4);
for (let n = 1; n <= maxN; n++) {
  enumerate(n);
}

