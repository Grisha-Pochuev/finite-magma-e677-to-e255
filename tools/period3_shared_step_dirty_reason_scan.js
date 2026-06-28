"use strict";

// For strict right-h period-3 cycles, scan shared-step anchored-X3 candidates
// before the clean filter and classify why the H_h triple is dirty.  This is
// the contrapositive companion to period3_clean_triple_identity_scan.js.

const fs = require("fs");
const path = require("path");

const cacheDir = process.argv[2] || path.join("cache", "eq677-db");

function parseTable(file) {
  return fs.readFileSync(file, "utf8").trim().split(/\n/).map((line) =>
    line.trim().split(/\s+/).map(Number)
  );
}

function inverseRows(table) {
  const n = table.length;
  const inv = Array.from({ length: n }, () => new Int32Array(n).fill(-1));
  for (let row = 0; row < n; row++) {
    for (let col = 0; col < n; col++) inv[row][table[row][col]] = col;
  }
  return inv;
}

function localModelFiles() {
  if (!fs.existsSync(cacheDir)) return [];
  const out = [];
  const sizes = fs.readdirSync(cacheDir).filter((x) => /^\d+$/.test(x));
  for (const size of sizes) {
    const dir = path.join(cacheDir, size);
    if (!fs.existsSync(dir)) continue;
    for (const name of fs.readdirSync(dir)) {
      const file = path.join(dir, name);
      if (fs.statSync(file).isFile()) out.push({ size, name, file });
    }
  }
  out.sort((a, b) => Number(a.size) - Number(b.size) || a.name.localeCompare(b.name));
  return out;
}

function distinct(values) {
  return new Set(values).size === values.length;
}

function add(map, key, amount = 1) {
  map.set(key, (map.get(key) || 0) + amount);
}

function profileFor(table, inv, z, b, h) {
  const c = table[b][h];
  const Ib = inv[b][h];
  const Ic = inv[c][h];
  const BC = table[b][c];
  const A = table[Ib][c];
  const K = table[A][Ib];
  const L = table[c][K];
  const parts = [];
  if (A === z) parts.push("A=Ib*c=z");
  if (A === b) parts.push("A=Ib*c=b");
  if (A === c) parts.push("A=Ib*c=c");
  if (A === h) parts.push("A=Ib*c=h");
  if (A === BC) parts.push("A=Ib*c=BC");
  if (K === Ic) parts.push("K=Ic");
  if (K === c) parts.push("K=c");
  if (K === A) parts.push("K=A");
  if (L === h) parts.push("L=h");
  if (L === table[c][c]) parts.push("L=c*c");
  if (table[Ib][h] === c) parts.push("Ib*h=c");
  if (table[z][Ib] === Ic) parts.push("z*Ib=Ic");
  return parts.length ? parts.sort().join(";") : "fresh";
}

function dirtyReasons(inputs, outputs) {
  const reasons = [];
  const inputEntries = Object.entries(inputs);
  const outputEntries = Object.entries(outputs);
  for (let i = 0; i < inputEntries.length; i++) {
    for (let j = i + 1; j < inputEntries.length; j++) {
      if (inputEntries[i][1] === inputEntries[j][1]) {
        reasons.push(`input-repeat:${inputEntries[i][0]}=${inputEntries[j][0]}`);
      }
    }
  }
  for (let i = 0; i < outputEntries.length; i++) {
    for (let j = i + 1; j < outputEntries.length; j++) {
      if (outputEntries[i][1] === outputEntries[j][1]) {
        reasons.push(`output-repeat:${outputEntries[i][0]}=${outputEntries[j][0]}`);
      }
    }
  }
  for (const [iName, iValue] of inputEntries) {
    for (const [oName, oValue] of outputEntries) {
      if (iValue === oValue) reasons.push(`input-output:${iName}=${oName}`);
    }
  }
  return reasons.length ? reasons.sort().join("|") : "clean";
}

const totals = {
  candidates: 0,
  clean: 0,
  dirty: 0,
  candidatesWithoutAIbcz: 0,
  cleanWithoutAIbcz: 0,
  dirtyWithoutAIbcz: 0,
  profileCounts: new Map(),
  reasonCounts: new Map(),
  profileReasonCounts: new Map(),
  examplesWithoutAIbcz: [],
};

for (const item of localModelFiles()) {
  const table = parseTable(item.file);
  const inv = inverseRows(table);
  const n = table.length;
  const groups = new Map();
  for (let p = 0; p < n; p++) {
    for (let b = 0; b < n; b++) {
      const z = table[p][b];
      const key = b * n + z;
      let rows = groups.get(key);
      if (rows === undefined) groups.set(key, (rows = []));
      rows.push(p);
    }
  }

  for (const [key, rows] of groups) {
    if (rows.length < 2) continue;
    const b = Math.floor(key / n);
    const z = key % n;
    for (let i = 0; i < rows.length; i++) {
      for (let j = i + 1; j < rows.length; j++) {
        const p = rows[i];
        const q = rows[j];
        const U = table[p][z];
        const W = table[q][z];
        const h = table[U][p];
        if (table[W][q] !== h) continue;
        if (table[z][h] !== b) continue;
        const c = table[b][h];
        if (table[c][h] !== z) continue;
        if (!distinct([z, b, c])) continue;
        const Ib = inv[b][h];
        const Ic = inv[c][h];
        const ZB = table[z][b];
        const BC = table[b][c];
        const CZ = table[c][z];
        const strict =
          distinct([z, b, c, h, Ib, Ic, ZB, BC, CZ]) &&
          distinct([ZB, BC, CZ]) &&
          ![ZB, BC, CZ].some((v) => v === h || v === z || v === b || v === c);
        if (!strict) continue;

        const T = table[U][h];
        const S = table[W][h];
        if (T === S) continue;
        const alpha = inv[z][h];
        const profile = profileFor(table, inv, z, b, h);
        const reason = dirtyReasons({ p, q, alpha }, { T, S, b });
        const withoutAIbcz = !profile.includes("A=Ib*c=z");

        totals.candidates++;
        if (reason === "clean") totals.clean++;
        else totals.dirty++;
        if (withoutAIbcz) {
          totals.candidatesWithoutAIbcz++;
          if (reason === "clean") totals.cleanWithoutAIbcz++;
          else totals.dirtyWithoutAIbcz++;
          if (totals.examplesWithoutAIbcz.length < 30) {
            const A = table[Ib][c];
            const K = table[A][Ib];
            const L = table[c][K];
            totals.examplesWithoutAIbcz.push({ model: `${item.size}/${item.name}`, z, b, c, h, Ib, Ic, p, q, U, W, T, S, alpha, A, K, L, profile, reason });
          }
        }
        add(totals.profileCounts, profile);
        add(totals.reasonCounts, reason);
        add(totals.profileReasonCounts, `${profile} || ${reason}`);
      }
    }
  }
}

function sortedObject(map) {
  return Object.fromEntries([...map.entries()].sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0])));
}

console.log(JSON.stringify({
  cache: cacheDir,
  candidates: totals.candidates,
  clean: totals.clean,
  dirty: totals.dirty,
  candidatesWithoutAIbcz: totals.candidatesWithoutAIbcz,
  cleanWithoutAIbcz: totals.cleanWithoutAIbcz,
  dirtyWithoutAIbcz: totals.dirtyWithoutAIbcz,
  profileCounts: sortedObject(totals.profileCounts),
  reasonCounts: sortedObject(totals.reasonCounts),
  profileReasonCounts: sortedObject(totals.profileReasonCounts),
  examplesWithoutAIbcz: totals.examplesWithoutAIbcz,
}, null, 2));
