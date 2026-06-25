"use strict";

// Diagnostic for pure same-row target-advance periods in the known M496 model.
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

function enc(x, s) {
  return x * FIBER + s;
}

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
  return enc(z, u);
}

function rowCycleLengths(row) {
  const seen = new Uint8Array(N);
  const lengths = [];
  for (let start = 0; start < N; start++) {
    if (seen[start]) continue;
    let cur = start;
    let length = 0;
    do {
      seen[cur] = 1;
      cur = op(row, cur);
      length++;
      if (length > N) throw new Error("row is not a permutation");
    } while (cur !== start);
    lengths.push(length);
  }
  return lengths;
}

function add(map, key, count = 1) {
  map.set(key, (map.get(key) || 0) + count);
}

function main() {
  const cycleLengthHistogram = new Map();
  const rowTypeHistogram = new Map();
  const examples = [];
  let maxLen = 0;
  let rowsWithShortOnly = 0;

  for (let row = 0; row < N; row++) {
    const lengths = rowCycleLengths(row);
    const type = Array.from(new Set(lengths)).sort((a, b) => a - b).join(",");
    add(rowTypeHistogram, type);
    if (lengths.every((length) => length <= 2)) rowsWithShortOnly++;
    for (const length of lengths) {
      add(cycleLengthHistogram, length);
      maxLen = Math.max(maxLen, length);
    }
    if (examples.length < 8 && lengths.some((length) => length >= 3)) {
      examples.push({
        row,
        cycleLengths: Array.from(new Set(lengths)).sort((a, b) => a - b),
        firstLengths: lengths.slice(0, 10),
      });
    }
  }

  console.log(
    JSON.stringify(
      {
        N,
        zeta,
        omega,
        maxLen,
        rowsWithShortOnly,
        rowTypeHistogram: Array.from(rowTypeHistogram.entries()).sort((a, b) =>
          a[0].localeCompare(b[0])
        ),
        cycleLengthHistogram: Array.from(cycleLengthHistogram.entries()).sort(
          (a, b) => a[0] - b[0]
        ),
        examples,
      },
      null,
      2
    )
  );
}

main();
