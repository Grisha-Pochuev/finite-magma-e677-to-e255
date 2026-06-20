"use strict";

// Diagnostic for the first extra intersection in the known M496 model.
// For each pair of distinct rows sharing b -> z, find the first extra
// intersection of their row cycles after z and classify the two H_w edges by
// same_target_pair_collision_trichotomy_lemma.md.
// This is only a model diagnostic, not a proof.

const P = 31;
const FIBER = 16;
const N = P * FIBER;

function mod(a, p) {
  a %= p;
  return a < 0 ? a + p : a;
}

function gfMul(a, b) {
  let out = 0;
  let aa = a;
  let bb = b;
  while (bb) {
    if (bb & 1) out ^= aa;
    bb >>= 1;
    aa <<= 1;
    if (aa & 0x10) aa ^= 0x13;
  }
  return out & 0x0f;
}

function gfPow(a, e) {
  let out = 1;
  let base = a;
  while (e) {
    if (e & 1) out = gfMul(out, base);
    base = gfMul(base, base);
    e >>= 1;
  }
  return out;
}

const zeta = gfPow(2, 3);
const omega = gfPow(2, 5);
const residues = new Set();
for (let x = 1; x < P; x++) residues.add(mod(x * x, P));

function dec(a) {
  return [Math.floor(a / FIBER), a & 15];
}

function op(a, b) {
  const [x, s] = dec(a);
  const [y, t] = dec(b);
  const z = mod(x - 2 * (y - x), P);
  const d = mod(y - x, P);
  const kind = d === 0 ? "0" : residues.has(d) ? "+" : "-";
  const u = kind === "+" ? t : s ^ gfMul(kind === "0" ? zeta : omega, t ^ s);
  return z * FIBER + u;
}

function buildCycleData() {
  const cycleArr = Array.from({ length: N }, () => Array(N));
  const posMap = Array.from({ length: N }, () => Array(N));

  for (let row = 0; row < N; row++) {
    const seen = new Uint8Array(N);
    for (let start = 0; start < N; start++) {
      if (seen[start]) continue;
      const cycle = [];
      let cur = start;
      while (!seen[cur]) {
        seen[cur] = 1;
        cycle.push(cur);
        cur = op(row, cur);
        if (cycle.length > N) throw new Error("row is not a permutation");
      }
      const positions = new Int16Array(N);
      positions.fill(-1);
      for (let i = 0; i < cycle.length; i++) positions[cycle[i]] = i;
      for (const v of cycle) {
        cycleArr[row][v] = cycle;
        posMap[row][v] = positions;
      }
    }
  }

  return { cycleArr, posMap };
}

function classify(lp, rp, lq, rq) {
  if (lp === lq && rp === rq) return "full";
  if (lp === lq) return "sameInput";
  if (rp === rq) return "sameOutput";
  if (lp === rq || lq === rp) return "crossHit";
  return "clean";
}

function main() {
  const { cycleArr, posMap } = buildCycleData();
  const groups = new Map();
  for (let row = 0; row < N; row++) {
    for (let b = 0; b < N; b++) {
      const z = op(row, b);
      const key = `${b},${z}`;
      if (!groups.has(key)) groups.set(key, []);
      groups.get(key).push(row);
    }
  }

  const counts = {
    full: 0,
    sameInput: 0,
    sameOutput: 0,
    crossHit: 0,
    clean: 0,
    noExtra: 0,
  };
  const examples = Object.fromEntries(
    Object.keys(counts).map((key) => [key, []])
  );

  function addExample(kind, value) {
    if (examples[kind].length < 3) examples[kind].push(value);
  }

  for (const [key, rows] of groups.entries()) {
    if (rows.length < 2) continue;
    const [bText, zText] = key.split(",");
    const b = Number(bText);
    const z = Number(zText);

    for (let left = 0; left < rows.length; left++) {
      for (let right = left + 1; right < rows.length; right++) {
        const p = rows[left];
        const q = rows[right];
        const pCycle = cycleArr[p][b];
        const qCycle = cycleArr[q][b];
        const qPos = posMap[q][b];
        let i = -1;

        for (let k = 2; k < pCycle.length; k++) {
          const vertex = pCycle[k];
          if (vertex !== b && vertex !== z && qPos[vertex] >= 0) {
            i = k;
            break;
          }
        }

        if (i < 0) {
          counts.noExtra++;
          addExample("noExtra", { b, z, p, q });
          continue;
        }

        const w = pCycle[i];
        const j = qPos[w];
        const lp = pCycle[(i - 1 + pCycle.length) % pCycle.length];
        const rp = pCycle[(i + 1) % pCycle.length];
        const lq = qCycle[(j - 1 + qCycle.length) % qCycle.length];
        const rq = qCycle[(j + 1) % qCycle.length];
        const kind = classify(lp, rp, lq, rq);
        counts[kind]++;
        addExample(kind, {
          b,
          z,
          p,
          q,
          w,
          i,
          j,
          lp,
          rp,
          lq,
          rq,
          pLen: pCycle.length,
          qLen: qCycle.length,
        });
      }
    }
  }

  console.log(JSON.stringify({ counts, examples }, null, 2));
}

main();
