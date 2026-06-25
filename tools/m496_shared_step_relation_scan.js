"use strict";

// Scan extra relations around the shared-step anchored triangle in M496.
// This is diagnostic only; universal counts suggest proof targets.

const Prime = 31;
const F = 16;
const N = Prime * F;

function modP(a) {
  const r = a % Prime;
  return r < 0 ? r + Prime : r;
}

function gfMul(a, b) {
  let out = 0;
  let aa = a;
  let bb = b;
  while (bb !== 0) {
    if ((bb & 1) !== 0) out ^= aa;
    bb >>= 1;
    aa <<= 1;
    if ((aa & 0x10) !== 0) aa ^= 0x13;
  }
  return out & 0x0f;
}

function gfPow(a, e) {
  let out = 1;
  let base = a;
  while (e !== 0) {
    if ((e & 1) !== 0) out = gfMul(out, base);
    base = gfMul(base, base);
    e >>= 1;
  }
  return out;
}

const zeta = gfPow(2, 3);
const omega = gfPow(2, 5);
const residues = Array(Prime).fill(false);
for (let x = 1; x < Prime; x++) residues[modP(x * x)] = true;

function op(a, b) {
  const x = Math.floor(a / F);
  const s = a & 15;
  const y = Math.floor(b / F);
  const t = b & 15;
  const z = modP(x - 2 * (y - x));
  const d = modP(y - x);
  let u;
  if (d === 0) {
    u = s ^ gfMul(zeta, t ^ s);
  } else if (residues[d]) {
    u = t;
  } else {
    u = s ^ gfMul(omega, t ^ s);
  }
  return z * F + u;
}

const table = Array.from({ length: N }, () => Array(N));
for (let row = 0; row < N; row++) {
  for (let col = 0; col < N; col++) table[row][col] = op(row, col);
}

const groups = new Map();
for (let p = 0; p < N; p++) {
  for (let b = 0; b < N; b++) {
    const z = table[p][b];
    const key = b * N + z;
    if (!groups.has(key)) groups.set(key, []);
    groups.get(key).push(p);
  }
}

const counts = new Map();
function bump(name, ok) {
  counts.set(name, (counts.get(name) || 0) + (ok ? 1 : 0));
}

let pairs = 0;
for (const [key, rows] of groups) {
  if (rows.length < 2) continue;
  const b = Math.floor(key / N);
  const z = key % N;
  for (let i = 0; i < rows.length; i++) {
    for (let j = i + 1; j < rows.length; j++) {
      const p = rows[i];
      const q = rows[j];
      const U = table[p][z];
      const W = table[q][z];
      const h = table[U][p];
      if (h !== table[W][q]) continue;
      const T = table[U][h];
      if (T !== table[W][h]) continue;
      const A = table[T][U];
      const B = table[T][W];
      const pU = table[p][U];
      const qW = table[q][W];
      const UT = table[U][T];
      const WT = table[W][T];
      const hp = table[h][p];
      const hq = table[h][q];
      const zT = table[z][T];
      const Tb = table[T][b];
      const Th = table[T][h];
      pairs++;

      bump("h*(T*U)=p", table[h][A] === p);
      bump("h*(T*W)=q", table[h][B] === q);
      bump("T*U=T*W", A === B);
      bump("p*U=q*W", pU === qW);
      bump("U*T=W*T", UT === WT);
      bump("h*p=h*q", hp === hq);
      bump("z*T=b", zT === b);
      bump("T*b=z", Tb === z);
      bump("T*h=b", Th === b);
      bump("p*U=T", pU === T);
      bump("q*W=T", qW === T);
      bump("U*T=h", UT === h);
      bump("W*T=h", WT === h);
    }
  }
}

console.log(`pairs: ${pairs}`);
for (const [name, count] of [...counts.entries()].sort()) {
  console.log(`${name}: ${count}`);
}
