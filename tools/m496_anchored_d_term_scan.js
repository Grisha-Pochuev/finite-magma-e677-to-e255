"use strict";

// Narrow diagnostic inspired by memoryleak47/eq677 src/analysis.rs.
// It scans M496 shared-step anchored triangles and checks short relations
// involving d(x)=((x*x)*x). This is diagnostic only, not a proof.

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

const table = Array.from({ length: N }, () => new Uint16Array(N));
for (let x = 0; x < N; x++) {
  for (let y = 0; y < N; y++) table[x][y] = op(x, y);
}

function mul(x, y) {
  return table[x][y];
}

function d(x) {
  return mul(mul(x, x), x);
}

function bump(map, name, ok) {
  const item = map.get(name) || { true: 0, false: 0 };
  if (ok) item.true++;
  else item.false++;
  map.set(name, item);
}

function main() {
  let e255All = true;
  for (let x = 0; x < N; x++) {
    if (mul(d(x), x) !== x) {
      e255All = false;
      break;
    }
  }

  const groups = new Map();
  for (let p = 0; p < N; p++) {
    for (let b = 0; b < N; b++) {
      const z = mul(p, b);
      const key = b * N + z;
      if (!groups.has(key)) groups.set(key, []);
      groups.get(key).push(p);
    }
  }

  const counts = new Map();
  let pairs = 0;
  let anchoredPairs = 0;

  for (const [key, rows] of groups) {
    if (rows.length < 2) continue;
    const b = Math.floor(key / N);
    const z = key % N;
    for (let i = 0; i < rows.length; i++) {
      for (let j = i + 1; j < rows.length; j++) {
        const p = rows[i];
        const q = rows[j];
        pairs++;

        const U = mul(p, z);
        const W = mul(q, z);
        const h = mul(U, p);
        if (h !== mul(W, q)) continue;
        const T = mul(U, h);
        if (T !== mul(W, h)) continue;
        anchoredPairs++;

        const alpha = mul(h, mul(b, z));
        const names = { b, z, p, q, U, W, h, T, alpha };
        const D = Object.fromEntries(
          Object.entries(names).map(([name, value]) => [`d${name}`, d(value)])
        );

        bump(counts, "E255(b)", mul(D.db, b) === b);
        bump(counts, "E255(z)", mul(D.dz, z) === z);
        bump(counts, "E255(h)", mul(D.dh, h) === h);
        bump(counts, "E255(T)", mul(D.dT, T) === T);
        bump(counts, "E255(U)", mul(D.dU, U) === U);
        bump(counts, "E255(W)", mul(D.dW, W) === W);

        bump(counts, "d(U)=d(W)", D.dU === D.dW);
        bump(counts, "d(p)=d(q)", D.dp === D.dq);
        bump(counts, "d(h)=h", D.dh === h);
        bump(counts, "h*h=h", mul(h, h) === h);
        bump(counts, "d(z)=z", D.dz === z);
        bump(counts, "z*z=z", mul(z, z) === z);
        bump(counts, "d(U)*h=d(W)*h", mul(D.dU, h) === mul(D.dW, h));
        bump(counts, "U*d(h)=W*d(h)", mul(U, D.dh) === mul(W, D.dh));
        bump(counts, "h*d(U)=h*d(W)", mul(h, D.dU) === mul(h, D.dW));
        bump(counts, "d(U*h)=d(T)", d(mul(U, h)) === D.dT);
        bump(counts, "T=d(h)", T === D.dh);
        bump(counts, "T=d(z)", T === D.dz);
        bump(counts, "T=d(b)", T === D.db);
        bump(counts, "b=d(h)", b === D.dh);
        bump(counts, "z=d(h)", z === D.dh);
        bump(counts, "d(T)*h=T", mul(D.dT, h) === T);
        bump(counts, "d(T)*T=T", mul(D.dT, T) === T);
        bump(counts, "T*d(h)=b", mul(T, D.dh) === b);
        bump(counts, "h*d(T)=b", mul(h, D.dT) === b);
        bump(counts, "z*d(h)=b", mul(z, D.dh) === b);
        bump(counts, "d(z)*h=b", mul(D.dz, h) === b);
        bump(counts, "d(h)*z=alpha", mul(D.dh, z) === alpha);
        bump(counts, "h*d(b)=alpha", mul(h, D.db) === alpha);
      }
    }
  }

  const relations = [...counts.entries()]
    .map(([name, item]) => ({
      name,
      true: item.true,
      false: item.false,
      ratio: item.true / (item.true + item.false),
    }))
    .sort((a, b) => b.ratio - a.ratio || a.name.localeCompare(b.name));

  console.log(JSON.stringify({ e255All, pairs, anchoredPairs, relations }, null, 2));
}

main();
