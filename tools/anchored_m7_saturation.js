"use strict";

// Bounded ground-congruence diagnostic for the anchored-X3 M7 template.
// This is a local idea generator, not a proof search over finite models.

const maxDepth = Number(process.argv[2] || 4);
const formulaRounds = Number(process.argv[3] || 12);
const maxTerms = Number(process.argv[4] || 250000);

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
const u = constant("U");
const w = constant("W");
const h = constant("h");
const alpha = constant("alpha");
const t = constant("T");
const s = constant("S");
const t1 = constant("T1");
const s1 = constant("S1");
const b1 = constant("B1");

const assumptions = [];
function eq(x, y, label) {
  assumptions.push({ x, y, label });
}

eq(op(p, b), z, "p*b=z");
eq(op(q, b), z, "q*b=z");
eq(op(p, z), u, "p*z=U");
eq(op(q, z), w, "q*z=W");
eq(op(u, p), h, "U*p=h");
eq(op(w, q), h, "W*q=h");
eq(op(z, h), b, "z*h=b");
eq(op(z, alpha), h, "z*alpha=h");
eq(op(u, h), t, "U*h=T");
eq(op(w, h), s, "W*h=S");
eq(op(h, op(t, u)), p, "h*(T*U)=p");
eq(op(h, op(s, w)), q, "h*(S*W)=q");
eq(op(h, op(b, z)), alpha, "h*(b*z)=alpha");
eq(op(t, op(op(u, t), u)), h, "T*((U*T)*U)=h");
eq(op(s, op(op(w, s), w)), h, "S*((W*S)*W)=h");
eq(op(b, op(op(z, b), z)), h, "b*((z*b)*z)=h");
eq(op(t, h), t1, "T*h=T1");
eq(op(s, h), s1, "S*h=S1");
eq(op(b, h), b1, "b*h=B1");

const forbidden = [
  [t, s, "T!=S"],
  [t, u, "T!=U"],
  [s, w, "S!=W"],
  [b, z, "b!=z"],
  [t1, u, "T*h!=U"],
  [s1, w, "S*h!=W"],
  [b1, z, "b*h!=z"],
];

const watch = [b, p, q, z, u, w, h, alpha, t, s, t1, s1, b1];

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

  // E677.
  for (const y of current) {
    for (const x of current) {
      const yx = op(y, x);
      const suffix = op(yx, y);
      changed = union(op(y, op(x, suffix)), x) || changed;
    }
  }

  // Edge predecessor formula: if r*i=H and r*H=O, then i=H*(O*r).
  const products = presentProducts();
  for (const ri of products) {
    for (const rH of products) {
      if (!same(ri.left, rH.left)) continue;
      const r = ri.left;
      const i = ri.right;
      const H = ri.id;
      const O = rH.id;
      if (!same(rH.right, H)) continue;
      changed = union(i, op(H, op(O, r))) || changed;
    }
  }

  // Fixed-target source successor: if r*H=O then O*((r*O)*r)=H.
  for (const rH of products) {
    const r = rH.left;
    const H = rH.right;
    const O = rH.id;
    changed = union(op(O, op(op(r, O), r)), H) || changed;
  }

  // Shared-input collision consequence.
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
  for (const term of presentProducts()) {
    const key = `${find(term.left)}:${find(term.id)}`;
    if (byLeftAndValue.has(key)) {
      changed = union(term.right, terms[byLeftAndValue.get(key)].right) || changed;
    } else {
      byLeftAndValue.set(key, term.id);
    }
  }

  // Congruence for products.
  const byPair = new Map();
  for (const term of presentProducts()) {
    const key = `${find(term.left)},${find(term.right)}`;
    if (byPair.has(key)) {
      changed = union(term.id, byPair.get(key)) || changed;
    } else {
      byPair.set(key, term.id);
    }
  }

  return changed;
}

seedNamedNeighborhood();
let closeRounds = 0;
for (; closeRounds < formulaRounds; closeRounds++) {
  if (!close()) break;
}

function classTerms(id, limit = 12) {
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

const comparisons = [
  [t1, s1, "T1=S1"],
  [t1, b1, "T1=B1"],
  [s1, b1, "S1=B1"],
  [t1, t, "T1=T"],
  [s1, s, "S1=S"],
  [b1, b, "B1=b"],
  [t1, p, "T1=p"],
  [s1, q, "S1=q"],
  [b1, alpha, "B1=alpha"],
  [op(t1, h), t, "T1*h=T"],
  [op(s1, h), s, "S1*h=S"],
  [op(b1, h), b, "B1*h=b"],
];

console.log("Anchored M7 saturation");
console.log(`maxDepth: ${maxDepth}`);
console.log(`formulaRounds: ${formulaRounds}`);
console.log(`maxTerms: ${maxTerms}`);
console.log(`closeRounds: ${closeRounds}`);
console.log(`terms: ${terms.length}`);

console.log("forbidden collapses:");
let anyForbidden = false;
for (const [a, bTerm, label] of forbidden) {
  const hit = same(a, bTerm);
  if (hit) anyForbidden = true;
  console.log(`  ${label}: ${hit}`);
}
console.log(`clean-consistent-in-closure: ${!anyForbidden}`);

console.log("candidate equalities:");
for (const [a, bTerm, label] of comparisons) {
  console.log(`  ${label}: ${same(a, bTerm)}`);
}

console.log(`T1 class: ${JSON.stringify(classTerms(t1))}`);
console.log(`S1 class: ${JSON.stringify(classTerms(s1))}`);
console.log(`B1 class: ${JSON.stringify(classTerms(b1))}`);
