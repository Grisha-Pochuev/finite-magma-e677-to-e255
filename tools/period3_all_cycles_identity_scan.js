"use strict";

// Scan cached eq677 db models for all right-h period-3 source cycles.
// This is a candidate-lemma finder for the period-3 c-input V3 branch,
// not a proof.

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

function add(map, key) {
  map.set(key, (map.get(key) || 0) + 1);
}

function relationProfiles(table, inv, data) {
  const { z, b, c, h, Ib, Ic, BC, A, K, L } = data;
  const cc = table[c][c];
  const profiles = [];
  if (A === z) profiles.push("A=Ib*c=z");
  if (A === b) profiles.push("A=Ib*c=b");
  if (A === c) profiles.push("A=Ib*c=c");
  if (A === h) profiles.push("A=Ib*c=h");
  if (A === BC) profiles.push("A=Ib*c=BC");
  if (A === Ic) profiles.push("A=Ib*c=Ic");
  if (L === h) profiles.push("L=h");
  if (L === z) profiles.push("L=z");
  if (L === b) profiles.push("L=b");
  if (L === c) profiles.push("L=c");
  if (L === Ib) profiles.push("L=Ib");
  if (L === Ic) profiles.push("L=Ic");
  if (L === BC) profiles.push("L=BC");
  if (L === A) profiles.push("L=A");
  if (K === Ic) profiles.push("K=(Ib*c)*Ib=Ic");
  if (K === z) profiles.push("K=(Ib*c)*Ib=z");
  if (K === b) profiles.push("K=(Ib*c)*Ib=b");
  if (K === c) profiles.push("K=(Ib*c)*Ib=c");
  if (K === h) profiles.push("K=(Ib*c)*Ib=h");
  if (K === A) profiles.push("K=(Ib*c)*Ib=A");
  if (K === BC) profiles.push("K=(Ib*c)*Ib=BC");
  if (L === cc) profiles.push("L=c*c");
  if (cc === c) profiles.push("c*c=c");
  if (cc === h) profiles.push("c*c=h");
  if (table[Ib][h] === c) profiles.push("Ib*h=c");
  if (table[z][Ib] === Ic) profiles.push("z*Ib=Ic");
  if (table[Ic][z] === Ib) profiles.push("Ic*z=Ib");
  if (table[b][A] === Ic) profiles.push("b*A=Ic");
  if (table[BC][z] === c) profiles.push("BC*z=c");
  if (table[c][K] === h) profiles.push("c*K=h");
  return profiles.length ? profiles.sort().join(";") : "fresh";
}

const modelCounts = new Map();
const strictModelCounts = new Map();
const profileCounts = new Map();
const strictProfileCounts = new Map();
const cleanAdvanceProfileCounts = new Map();
const misses = [];
let total = 0;
let strictTotal = 0;
let cleanAdvanceTotal = 0;

for (const item of localModelFiles()) {
  const table = parseTable(item.file);
  const inv = inverseRows(table);
  const n = table.length;
  let modelTotal = 0;
  let modelStrict = 0;

  for (let h = 0; h < n; h++) {
    for (let z = 0; z < n; z++) {
      const b = table[z][h];
      const c = table[b][h];
      if (table[c][h] !== z) continue;
      if (!distinct([z, b, c])) continue;

      const Ib = inv[b][h];
      const Ic = inv[c][h];
      const ZB = table[z][b];
      const BC = table[b][c];
      const CZ = table[c][z];
      const A = table[Ib][c];
      const K = table[A][Ib];
      const L = table[c][K];
      const data = { z, b, c, h, Ib, Ic, ZB, BC, CZ, A, K, L };
      const profile = relationProfiles(table, inv, data);

      total++;
      modelTotal++;
      add(profileCounts, profile);

      const strict = distinct([z, b, c, h, Ib, Ic, ZB, BC, CZ]);
      if (strict) {
        strictTotal++;
        modelStrict++;
        add(strictProfileCounts, profile);
        if (!profile.includes("A=Ib*c=z") && misses.length < 20) {
          misses.push({
            model: `${item.size}/${item.name}`,
            z, b, c, h, Ib, Ic, ZB, BC, CZ, A, K, L,
            profile,
          });
        }
      }

      const cleanAdvance =
        strict &&
        distinct([ZB, BC, CZ]) &&
        ![ZB, BC, CZ].some((v) => v === h || v === z || v === b || v === c);
      if (cleanAdvance) {
        cleanAdvanceTotal++;
        add(cleanAdvanceProfileCounts, profile);
      }
    }
  }

  if (modelTotal > 0) modelCounts.set(`${item.size}/${item.name}`, modelTotal);
  if (modelStrict > 0) strictModelCounts.set(`${item.size}/${item.name}`, modelStrict);
}

function sortedObject(map) {
  return Object.fromEntries([...map.entries()].sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0])));
}

console.log(JSON.stringify({
  cache: cacheDir,
  totalPeriod3Cycles: total,
  strictPeriod3Cycles: strictTotal,
  cleanAdvancePeriod3Cycles: cleanAdvanceTotal,
  modelCounts: Object.fromEntries(modelCounts),
  strictModelCounts: Object.fromEntries(strictModelCounts),
  profileCounts: sortedObject(profileCounts),
  strictProfileCounts: sortedObject(strictProfileCounts),
  cleanAdvanceProfileCounts: sortedObject(cleanAdvanceProfileCounts),
  strictMissesWithoutAIbcz: misses,
}, null, 2));
