"use strict";

// Bounded ground-congruence diagnostic for the shared-step anchored identity.
// It is intentionally narrow: failure to prove the target is not a refutation.

const maxDepth = Number(process.argv[2] || 4);
const formulaRounds = Number(process.argv[3] || 8);
const maxTerms = Number(process.argv[4] || 200000);

const termByKey = new Map();
const terms = [];
const parent = [];
const rank = [];

function makeTerm(key, expr, depth, left = -1, right = -1) {
  if (termByKey.has(key)) return termByKey.get(key);
  if (terms.length >= maxTerms) {
    throw new Error(`term cap reached (${maxTerms}); lower depth or narrow watch set`);
  }
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
  return makeTerm(
    `*(${x},${y})`,
    `(${terms[x].expr}*${terms[y].expr})`,
    1 + Math.max(terms[x].depth, terms[y].depth),
    x,
    y
  );
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

const b = constant("b");
const p = constant("p");
const q = constant("q");
const z = constant("z");
const U = constant("U");
const W = constant("W");
const h = constant("h");
const T = constant("T");
const S = constant("S");
const alpha = constant("alpha");

const assumptions = [];
function eq(x, y, label) {
  assumptions.push({ x, y, label });
}

eq(op(p, b), z, "p*b=z");
eq(op(q, b), z, "q*b=z");
eq(op(p, z), U, "p*z=U");
eq(op(q, z), W, "q*z=W");
eq(op(U, p), h, "U*p=h");
eq(op(W, q), h, "W*q=h");
eq(op(z, h), b, "z*h=b");
eq(op(z, alpha), h, "z*alpha=h");
eq(op(U, h), T, "T=U*h");
eq(op(W, h), S, "S=W*h");

// Keep the active set small.  These are the named vertices in the proposed
// anchored triangle plus the two candidate outputs T and S.
const watch = [b, p, q, z, U, W, h, T, S, alpha];

function seedNamedNeighborhood() {
  for (const x of watch) {
    for (const y of watch) {
      const xy = op(x, y);
      if (terms[xy].depth <= maxDepth) {
        op(xy, x);
        op(xy, y);
        op(x, xy);
        op(y, xy);
      }
    }
  }
}

function presentProducts() {
  return terms.filter((term) => term.left >= 0 && term.depth <= maxDepth);
}

function close() {
  let changed = false;

  for (const item of assumptions) changed = union(item.x, item.y) || changed;

  const current = watch.filter((id) => terms[id].depth <= maxDepth);

  // E677: y*(x*((y*x)*y)) = x.
  for (const y of current) {
    for (const x of current) {
      const yx = op(y, x);
      const suffix = op(yx, y);
      const inner = op(x, suffix);
      const e = op(y, inner);
      changed = union(e, x) || changed;
    }
  }

  // Finite E677 consequence used throughout the project:
  // if a=y*x and c=y*a, then a*(c*y)=x.
  for (const y of current) {
    for (const x of current) {
      const a = op(y, x);
      const c = op(y, a);
      changed = union(op(a, op(c, y)), x) || changed;
    }
  }

  // Shared-input collision consequence:
  // if y*x = r*x = c, then (y*c)*y = (r*c)*r.
  for (const x of current) {
    for (let i = 0; i < current.length; i++) {
      const y = current[i];
      const c = op(y, x);
      for (let j = i + 1; j < current.length; j++) {
        const r = current[j];
        const d = op(r, x);
        if (!same(c, d)) continue;
        changed = union(op(op(y, c), y), op(op(r, d), r)) || changed;
      }
    }
  }

  // Left cancellation for present products.
  const byLeftAndValue = new Map();
  for (const t of presentProducts()) {
    const key = `${find(t.left)}:${find(t.id)}`;
    if (byLeftAndValue.has(key)) {
      changed = union(t.right, terms[byLeftAndValue.get(key)].right) || changed;
    } else {
      byLeftAndValue.set(key, t.id);
    }
  }

  // Congruence for products with equal left and right classes.
  const byPair = new Map();
  for (const t of presentProducts()) {
    const key = `${find(t.left)},${find(t.right)}`;
    if (byPair.has(key)) {
      changed = union(t.id, byPair.get(key)) || changed;
    } else {
      byPair.set(key, t.id);
    }
  }

  return changed;
}

seedNamedNeighborhood();

let closeRounds = 0;
for (; closeRounds < formulaRounds; closeRounds++) {
  if (!close()) break;
}

function classTerms(id, limit = 18) {
  const root = find(id);
  const out = [];
  for (const term of terms) {
    if (term.depth > maxDepth) continue;
    if (find(term.id) !== root) continue;
    out.push(term.expr);
    if (out.length >= limit) break;
  }
  return out;
}

console.log("Anchored identity saturation");
console.log(`maxDepth: ${maxDepth}`);
console.log(`formulaRounds: ${formulaRounds}`);
console.log(`maxTerms: ${maxTerms}`);
console.log(`closeRounds: ${closeRounds}`);
console.log(`terms: ${terms.length}`);
console.log(`T=U*h: ${terms[T].expr}`);
console.log(`S=W*h: ${terms[S].expr}`);
console.log(`T == S: ${same(T, S)}`);
console.log(`T class: ${JSON.stringify(classTerms(T))}`);
console.log(`S class: ${JSON.stringify(classTerms(S))}`);
console.log(`h class: ${JSON.stringify(classTerms(h))}`);
console.log(`p class: ${JSON.stringify(classTerms(p))}`);
console.log(`q class: ${JSON.stringify(classTerms(q))}`);
