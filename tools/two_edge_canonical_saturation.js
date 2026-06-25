"use strict";

// Small ground-congruence diagnostic for the directed two-edge canonical
// collapse boundary. It is intentionally bounded: failure is not a refutation.

const maxDepth = Number(process.argv[2] || 3);

const termByKey = new Map();
const terms = [];
const parent = [];
const rank = [];

function makeTerm(key, expr, depth, left = -1, right = -1) {
  if (termByKey.has(key)) return termByKey.get(key);
  const id = terms.length;
  termByKey.set(key, id);
  terms.push({ id, key, expr, depth, left, right });
  parent.push(id);
  rank.push(0);
  return id;
}

function constant(name) {
  return makeTerm(name, name, 0);
}

function op(x, y) {
  const key = `*(${x},${y})`;
  const expr = `(${terms[x].expr}*${terms[y].expr})`;
  return makeTerm(key, expr, 1 + Math.max(terms[x].depth, terms[y].depth), x, y);
}

function find(x) {
  while (parent[x] !== x) {
    parent[x] = parent[parent[x]];
    x = parent[x];
  }
  return x;
}

function union(a, b) {
  let ra = find(a);
  let rb = find(b);
  if (ra === rb) return false;
  if (rank[ra] < rank[rb]) [ra, rb] = [rb, ra];
  parent[rb] = ra;
  if (rank[ra] === rank[rb]) rank[ra]++;
  return true;
}

function same(a, b) {
  return find(a) === find(b);
}

const a = constant("a");
const b = constant("b");
const c = constant("c");
const p = constant("p");
const r = constant("r");
const v = constant("v");
const u = constant("u");
const k = constant("k");

const assumptions = [];
function eq(x, y, label) {
  assumptions.push({ x, y, label });
}

eq(op(p, a), b, "p*a=b");
eq(op(p, b), v, "p*b=v");
eq(op(r, v), b, "r*v=b");
eq(op(r, b), c, "r*b=c");
eq(op(p, v), u, "p*v=u");
eq(op(u, p), k, "u*p=k");
eq(op(v, k), b, "v*k=b");

// Explicit edge-certificate consequences for p*a=b,p*b=v.
eq(op(b, op(v, p)), a, "b*(v*p)=a");
eq(op(p, op(a, op(b, p))), a, "p*(a*(b*p))=a");

// Explicit edge-certificate consequences for r*v=b,r*b=c.
eq(op(b, op(c, r)), v, "b*(c*r)=v");
eq(op(c, op(op(r, c), r)), b, "c*((r*c)*r)=b");
eq(op(r, op(v, op(b, r))), v, "r*(v*(b*r))=v");

const B = op(b, c);
const suffix = op(u, k);
const Y = op(B, suffix);
const canonical = op(op(b, b), b);

const basis = new Set([a, b, c, p, r, v, u, k, B, suffix, Y, canonical]);

function addBasisProducts(rounds) {
  for (let round = 0; round < rounds; round++) {
    const snapshot = [...basis];
    for (const x of snapshot) {
      for (const y of snapshot) {
        const xy = op(x, y);
        if (terms[xy].depth <= maxDepth) basis.add(xy);
      }
    }
  }
}

addBasisProducts(1);

function close() {
  let changed = false;
  for (const item of assumptions) changed = union(item.x, item.y) || changed;

  const current = [...basis];
  for (const y of current) {
    for (const x of current) {
      const yx = op(y, x);
      const inner = op(x, op(yx, y));
      const e = op(y, inner);
      changed = union(e, x) || changed;
    }
  }

  // Left cancellation for already present products.
  const byLeftAndValue = new Map();
  for (let id = 0; id < terms.length; id++) {
    const t = terms[id];
    if (t.left < 0) continue;
    const key = `${find(t.left)}:${find(id)}`;
    if (byLeftAndValue.has(key)) {
      changed = union(t.right, terms[byLeftAndValue.get(key)].right) || changed;
    } else {
      byLeftAndValue.set(key, id);
    }
  }

  // Congruence for products with equal left and right classes.
  const byPair = new Map();
  for (let id = 0; id < terms.length; id++) {
    const t = terms[id];
    if (t.left < 0) continue;
    const key = `${find(t.left)},${find(t.right)}`;
    if (byPair.has(key)) {
      changed = union(id, byPair.get(key)) || changed;
    } else {
      byPair.set(key, id);
    }
  }

  return changed;
}

for (let round = 0; round < 20; round++) {
  if (!close()) break;
}

console.log("Directed two-edge canonical saturation");
console.log(`maxDepth: ${maxDepth}`);
console.log(`terms: ${terms.length}`);
console.log(`Y: ${terms[Y].expr}`);
console.log(`canonical: ${terms[canonical].expr}`);
console.log(`Y == canonical: ${same(Y, canonical)}`);
console.log(`Y == b: ${same(Y, b)}`);
console.log(`Y*b == b: ${same(op(Y, b), b)}`);
