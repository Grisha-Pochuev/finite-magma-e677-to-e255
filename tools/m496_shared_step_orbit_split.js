"use strict";

// Diagnostic for the two-row orbit-theta split in the known M496 model.
// For every pair of distinct rows sharing one step b -> z, it checks whether
// their row cycles meet again outside {b,z}. This is only a model diagnostic,
// not a proof.

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

function bitsetFor(arr) {
  const words = new Uint32Array(16);
  for (const v of arr) words[v >>> 5] |= 1 << (v & 31);
  return words;
}

function hasExtraIntersection(maskA, maskB, b, z) {
  for (let k = 0; k < 16; k++) {
    let word = maskA[k] & maskB[k];
    if (word === 0) continue;
    if (k === (b >>> 5)) word &= ~(1 << (b & 31));
    if (k === (z >>> 5)) word &= ~(1 << (z & 31));
    if (word !== 0) return true;
  }
  return false;
}

function buildCycleData() {
  const cycleMaskByRowStart = Array.from({ length: N }, () => Array(N));
  const cycleLenByRowStart = Array.from({ length: N }, () => new Uint16Array(N));

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
      const mask = bitsetFor(cycle);
      for (const v of cycle) {
        cycleMaskByRowStart[row][v] = mask;
        cycleLenByRowStart[row][v] = cycle.length;
      }
    }
  }

  return { cycleMaskByRowStart, cycleLenByRowStart };
}

function main() {
  const { cycleMaskByRowStart, cycleLenByRowStart } = buildCycleData();
  const groups = new Map();

  for (let row = 0; row < N; row++) {
    for (let b = 0; b < N; b++) {
      const z = op(row, b);
      const key = `${b},${z}`;
      if (!groups.has(key)) groups.set(key, []);
      groups.get(key).push(row);
    }
  }

  let sharedStepPairs = 0;
  let extraIntersectionPairs = 0;
  let cleanThetaPairs = 0;
  let maxFiber = 0;
  const fiberHist = new Map();
  const examplesExtra = [];
  const examplesClean = [];

  for (const [key, rows] of groups.entries()) {
    if (rows.length < 2) continue;
    maxFiber = Math.max(maxFiber, rows.length);
    fiberHist.set(rows.length, (fiberHist.get(rows.length) || 0) + 1);
    const [bText, zText] = key.split(",");
    const b = Number(bText);
    const z = Number(zText);

    for (let i = 0; i < rows.length; i++) {
      for (let j = i + 1; j < rows.length; j++) {
        const p = rows[i];
        const q = rows[j];
        sharedStepPairs++;
        const hasExtra = hasExtraIntersection(
          cycleMaskByRowStart[p][b],
          cycleMaskByRowStart[q][b],
          b,
          z
        );
        if (hasExtra) {
          extraIntersectionPairs++;
          if (examplesExtra.length < 5) {
            examplesExtra.push({
              b,
              z,
              p,
              q,
              pLen: cycleLenByRowStart[p][b],
              qLen: cycleLenByRowStart[q][b],
            });
          }
        } else {
          cleanThetaPairs++;
          if (examplesClean.length < 5) {
            examplesClean.push({
              b,
              z,
              p,
              q,
              pLen: cycleLenByRowStart[p][b],
              qLen: cycleLenByRowStart[q][b],
            });
          }
        }
      }
    }
  }

  console.log(
    JSON.stringify(
      {
        groupsWithFiberGe2: Array.from(fiberHist.entries()).sort(
          (a, b) => a[0] - b[0]
        ),
        maxFiber,
        sharedStepPairs,
        extraIntersectionPairs,
        cleanThetaPairs,
        examplesExtra,
        examplesClean,
      },
      null,
      2
    )
  );
}

main();
