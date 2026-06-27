"use strict";

// Bounded ground-congruence diagnostic for the period-3 fixed-target zipper.
// This is a local consequence checker, not a proof and not a model search.

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

const h = constant("h");
const z = constant("z");
const b = constant("b");
const c = constant("c");
const alpha = constant("alpha");
const ib = constant("Ib");
const ic = constant("Ic");
const zb = constant("ZB");
const bc = constant("BC");
const cz = constant("CZ");

const assumptions = [];
function eq(x, y, label) {
  assumptions.push({ x, y, label });
}

// Period-3 right-h source cycle.
eq(op(z, h), b, "z*h=b");
eq(op(b, h), c, "b*h=c");
eq(op(c, h), z, "c*h=z");

// H_h zipper inputs.
eq(op(z, alpha), h, "z*alpha=h");
eq(op(b, ib), h, "b*Ib=h");
eq(op(c, ic), h, "c*Ic=h");
eq(alpha, op(h, op(b, z)), "alpha=h*(b*z)");
eq(ib, op(h, op(c, b)), "Ib=h*(c*b)");
eq(ic, op(h, op(z, c)), "Ic=h*(z*c)");

// Target-advanced triangle outputs.
eq(op(z, b), zb, "z*b=ZB");
eq(op(b, c), bc, "b*c=BC");
eq(op(c, z), cz, "c*z=CZ");

const watch = [h, z, b, c, alpha, ib, ic, zb, bc, cz];

const forbidden = [
  [z, b, "z!=b"],
  [z, c, "z!=c"],
  [b, c, "b!=c"],
  [h, z, "h!=z"],
  [h, b, "h!=b"],
  [h, c, "h!=c"],
  [alpha, ib, "alpha!=Ib"],
  [alpha, ic, "alpha!=Ic"],
  [ib, ic, "Ib!=Ic"],
  [zb, bc, "ZB!=BC"],
  [zb, cz, "ZB!=CZ"],
  [bc, cz, "BC!=CZ"],
  [zb, z, "ZB!=z"],
  [zb, b, "ZB!=b"],
  [zb, c, "ZB!=c"],
  [bc, z, "BC!=z"],
  [bc, b, "BC!=b"],
  [bc, c, "BC!=c"],
  [cz, z, "CZ!=z"],
  [cz, b, "CZ!=b"],
  [cz, c, "CZ!=c"],
];

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
  const products = presentProducts();

  // E677.
  for (const y of current) {
    for (const x of current) {
      const yx = op(y, x);
      const suffix = op(yx, y);
      changed = union(op(y, op(x, suffix)), x) || changed;
    }
  }

  // Derived consequence: if a=y*x and c=y*a, then a*(c*y)=x.
  for (const y of current) {
    for (const x of current) {
      const a = op(y, x);
      const yyx = op(y, a);
      changed = union(op(a, op(yyx, y)), x) || changed;
    }
  }

  // Edge predecessor formula: if r*i=H and r*H=O, then i=H*(O*r).
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
      const yx = op(y, x);
      for (let j = i + 1; j < current.length; j++) {
        const r = current[j];
        const rx = op(r, x);
        if (!same(yx, rx)) continue;
        changed = union(op(op(y, yx), y), op(op(r, rx), r)) || changed;
      }
    }
  }

  // Left cancellation for present products.
  const byLeftAndValue = new Map();
  for (const term of products) {
    const key = `${find(term.left)}:${find(term.id)}`;
    if (byLeftAndValue.has(key)) {
      changed = union(term.right, terms[byLeftAndValue.get(key)].right) || changed;
    } else {
      byLeftAndValue.set(key, term.id);
    }
  }

  // Congruence for products.
  const byPair = new Map();
  for (const term of products) {
    const key = `${find(term.left)},${find(term.right)}`;
    if (byPair.has(key)) {
      changed = union(term.id, byPair.get(key)) || changed;
    } else {
      byPair.set(key, term.id);
    }
  }

  return changed;
}

function d4(x) {
  return op(op(op(x, x), x), x);
}

seedNamedNeighborhood();
let closeRounds = 0;
for (; closeRounds < formulaRounds; closeRounds++) {
  if (!close()) break;
}

function classTerms(id, limit = 10) {
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

const useful = [
  [alpha, op(op(c, z), c), "alpha=(c*z)*c"],
  [ib, op(op(z, b), z), "Ib=(z*b)*z"],
  [ic, op(op(b, c), b), "Ic=(b*c)*b"],
  [op(b, op(op(z, b), z)), h, "b*((z*b)*z)=h"],
  [op(c, op(op(b, c), b)), h, "c*((b*c)*b)=h"],
  [op(z, op(op(c, z), c)), h, "z*((c*z)*c)=h"],
  [d4(z), z, "E255(z)"],
  [d4(b), b, "E255(b)"],
  [d4(c), c, "E255(c)"],
  [d4(h), h, "E255(h)"],
  [op(z, z), z, "z*z=z"],
  [op(b, b), b, "b*b=b"],
  [op(c, c), c, "c*c=c"],
  [op(h, h), h, "h*h=h"],
  [op(h, h), zb, "h*h=ZB"],
  [op(h, alpha), b, "h*alpha=b"],
  [op(h, ib), cz, "h*Ib=CZ"],
  [op(alpha, zb), h, "alpha*ZB=h"],
  [op(b, cz), ic, "b*CZ=Ic"],
  [op(bc, z), c, "BC*z=c"],
  [op(cz, ic), zb, "CZ*Ic=ZB"],
  [op(ib, c), z, "Ib*c=z"],
  [op(ib, h), c, "Ib*h=c"],
  [op(ic, z), ib, "Ic*z=Ib"],
  [op(z, ib), ic, "z*Ib=Ic"],
];

console.log("Period-3 zipper saturation");
console.log(`maxDepth: ${maxDepth}`);
console.log(`formulaRounds: ${formulaRounds}`);
console.log(`maxTerms: ${maxTerms}`);
console.log(`closeRounds: ${closeRounds}`);
console.log(`terms: ${terms.length}`);

console.log("forbidden clean collapses:");
let anyForbidden = false;
for (const [a, bTerm, label] of forbidden) {
  const hit = same(a, bTerm);
  if (hit) anyForbidden = true;
  console.log(`  ${label}: ${hit}`);
}
console.log(`clean-consistent-in-closure: ${!anyForbidden}`);

console.log("useful/candidate equalities:");
for (const [a, bTerm, label] of useful) {
  console.log(`  ${label}: ${same(a, bTerm)}`);
}

console.log(`alpha class: ${JSON.stringify(classTerms(alpha))}`);
console.log(`Ib class: ${JSON.stringify(classTerms(ib))}`);
console.log(`Ic class: ${JSON.stringify(classTerms(ic))}`);
console.log(`ZB class: ${JSON.stringify(classTerms(zb))}`);
console.log(`BC class: ${JSON.stringify(classTerms(bc))}`);
console.log(`CZ class: ${JSON.stringify(classTerms(cz))}`);
