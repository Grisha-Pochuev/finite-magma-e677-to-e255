"use strict";

// Bounded ground-congruence diagnostic for the anchored-M7 cycle-end residual.
// This is a local idea generator, not a finite-model search and not a proof.

const maxDepth = Number(process.argv[2] || 4);
const formulaRounds = Number(process.argv[3] || 12);
const maxTerms = Number(process.argv[4] || 300000);

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

const r0 = constant("r0");
const r1 = constant("r1");
const rm2 = constant("rm2");
const rm1 = constant("rm1");
const i0 = constant("i0");
const im2 = constant("im2");
const im1 = constant("im1");

const assumptions = [];
function eq(x, y, label) {
  assumptions.push({ x, y, label });
}

// Anchored-X3 false-branch data.
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

// First anchored source-successor layer in H_h.
eq(op(t, op(op(u, t), u)), h, "T*((U*T)*U)=h");
eq(op(s, op(op(w, s), w)), h, "S*((W*S)*W)=h");
eq(op(b, op(op(z, b), z)), h, "b*((z*b)*z)=h");

// Clean cycle-end residual.
eq(op(r0, h), r1, "r0*h=r1");
eq(op(rm2, h), rm1, "rm2*h=rm1");
eq(op(rm1, h), r0, "rm1*h=r0");
eq(op(r0, i0), h, "r0*i0=h");
eq(op(rm2, im2), h, "rm2*im2=h");
eq(op(rm1, im1), h, "rm1*im1=h");
eq(i0, op(h, op(r1, r0)), "i0=h*(r1*r0)");
eq(im2, op(h, op(rm1, rm2)), "im2=h*(rm1*rm2)");
eq(im1, op(h, op(r0, rm1)), "im1=h*(r0*rm1)");

const forbidden = [
  [t, s, "T!=S"],
  [t, u, "T!=U"],
  [s, w, "S!=W"],
  [b, z, "b!=z"],
  [r0, r1, "r0!=r1"],
  [r0, rm1, "r0!=rm1"],
  [r0, rm2, "r0!=rm2"],
  [rm2, rm1, "rm2!=rm1"],
  [i0, im1, "i0!=im1"],
  [i0, im2, "i0!=im2"],
  [im2, im1, "im2!=im1"],
  [i0, rm1, "i0!=rm1"],
  [im1, r1, "im1!=r1"],
];

const watch = [
  b, p, q, z, u, w, h, alpha, t, s,
  r0, r1, rm2, rm1, i0, im2, im1,
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
      const c = op(y, a);
      changed = union(op(a, op(c, y)), x) || changed;
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

const comparisons = [
  [im1, r1, "im1=r1"],
  [i0, rm1, "i0=rm1"],
  [im2, r0, "im2=r0"],
  [i0, im1, "i0=im1"],
  [i0, im2, "i0=im2"],
  [im2, im1, "im2=im1"],
  [r0, rm1, "r0=rm1"],
  [r0, rm2, "r0=rm2"],
  [r1, rm1, "r1=rm1"],
  [r1, rm2, "r1=rm2"],
  [op(r0, r1), op(rm1, r0), "r0*r1=rm1*r0"],
  [op(r0, i0), op(rm1, im1), "r0*i0=rm1*im1"],
  [i0, op(op(rm1, r0), rm1), "i0=(rm1*r0)*rm1"],
  [im1, op(op(rm2, rm1), rm2), "im1=(rm2*rm1)*rm2"],
  [im2, op(h, op(rm1, rm2)), "im2=h*(rm1*rm2)"],
  [op(r1, op(op(r0, r1), r0)), h, "r1*((r0*r1)*r0)=h"],
  [op(r0, op(op(rm1, r0), rm1)), h, "r0*((rm1*r0)*rm1)=h"],
];

console.log("Anchored M7 cycle-end saturation");
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

console.log("candidate equalities:");
for (const [a, bTerm, label] of comparisons) {
  console.log(`  ${label}: ${same(a, bTerm)}`);
}

console.log(`r0 class: ${JSON.stringify(classTerms(r0))}`);
console.log(`r1 class: ${JSON.stringify(classTerms(r1))}`);
console.log(`rm1 class: ${JSON.stringify(classTerms(rm1))}`);
console.log(`i0 class: ${JSON.stringify(classTerms(i0))}`);
console.log(`im1 class: ${JSON.stringify(classTerms(im1))}`);
