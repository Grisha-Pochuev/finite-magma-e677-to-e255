"use strict";

// Bounded ground-congruence diagnostic for anchored-X3 plus period-3 zipper.
// It tests whether the size-77 db identities that reconnect the period-3
// zipper to the original anchored layer are local E677 consequences.

const maxDepth = Number(process.argv[2] || 4);
const formulaRounds = Number(process.argv[3] || 12);
const maxTerms = Number(process.argv[4] || 400000);
const extraAssumptions = process.argv
  .slice(5)
  .flatMap((arg) => arg.startsWith("--assume=") ? arg.slice("--assume=".length).split(",") : [])
  .filter(Boolean);

const termByKey = new Map();
const terms = [];
const parent = [];
const rank = [];

function makeTerm(key, expr, depth, left = -1, right = -1) {
  if (termByKey.has(key)) return termByKey.get(key);
  if (terms.length >= maxTerms) throw new Error(`term cap reached (${maxTerms})`);
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
const c = constant("c");
const ib = constant("Ib");
const ic = constant("Ic");
const zb = constant("ZB");
const bc = constant("BC");
const cz = constant("CZ");

const assumptions = [];
function eq(x, y, label) {
  assumptions.push({ x, y, label });
}

// Anchored-X3 false branch.
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

// Period-3 z-orbit and zipper.
eq(op(b, h), c, "b*h=c");
eq(op(c, h), z, "c*h=z");
eq(op(b, ib), h, "b*Ib=h");
eq(op(c, ic), h, "c*Ic=h");
eq(ib, op(h, op(c, b)), "Ib=h*(c*b)");
eq(ic, op(h, op(z, c)), "Ic=h*(z*c)");
eq(ib, op(op(z, b), z), "Ib=(z*b)*z");
eq(ic, op(op(b, c), b), "Ic=(b*c)*b");
eq(alpha, op(op(c, z), c), "alpha=(c*z)*c");

// Advanced period-3 outputs.
eq(op(z, b), zb, "z*b=ZB");
eq(op(b, c), bc, "b*c=BC");
eq(op(c, z), cz, "c*z=CZ");

const extraAssumptionMap = {
  pcT: [op(p, c), t, "assume p*c=T"],
  qcS: [op(q, c), s, "assume q*c=S"],
  UzIb: [op(u, z), ib, "assume U*z=Ib"],
  WzIb: [op(w, z), ib, "assume W*z=Ib"],
  UzWz: [op(u, z), op(w, z), "assume U*z=W*z"],
};

for (const name of extraAssumptions) {
  const item = extraAssumptionMap[name];
  if (item === undefined) throw new Error(`unknown --assume item: ${name}`);
  eq(...item);
}

const watch = [b, p, q, z, u, w, h, alpha, t, s, c, ib, ic, zb, bc, cz];

const forbidden = [
  [t, s, "T!=S"],
  [b, z, "b!=z"],
  [b, c, "b!=c"],
  [z, c, "z!=c"],
  [h, z, "h!=z"],
  [h, b, "h!=b"],
  [h, c, "h!=c"],
  [alpha, ib, "alpha!=Ib"],
  [alpha, ic, "alpha!=Ic"],
  [ib, ic, "Ib!=Ic"],
  [zb, bc, "ZB!=BC"],
  [zb, cz, "ZB!=CZ"],
  [bc, cz, "BC!=CZ"],
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

  for (const y of current) {
    for (const x of current) {
      const yx = op(y, x);
      const suffix = op(yx, y);
      changed = union(op(y, op(x, suffix)), x) || changed;
    }
  }

  for (const y of current) {
    for (const x of current) {
      const a = op(y, x);
      const yyx = op(y, a);
      changed = union(op(a, op(yyx, y)), x) || changed;
    }
  }

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

  for (const rH of products) {
    const r = rH.left;
    const H = rH.right;
    const O = rH.id;
    changed = union(op(O, op(op(r, O), r)), H) || changed;
  }

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

  const byLeftAndValue = new Map();
  for (const term of products) {
    const key = `${find(term.left)}:${find(term.id)}`;
    if (byLeftAndValue.has(key)) changed = union(term.right, terms[byLeftAndValue.get(key)].right) || changed;
    else byLeftAndValue.set(key, term.id);
  }

  const byPair = new Map();
  for (const term of products) {
    const key = `${find(term.left)},${find(term.right)}`;
    if (byPair.has(key)) changed = union(term.id, byPair.get(key)) || changed;
    else byPair.set(key, term.id);
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

const useful = [
  [op(ib, c), z, "A=Ib*c=z"],
  [op(op(ib, c), ib), ic, "K=(Ib*c)*Ib=Ic"],
  [op(c, op(op(ib, c), ib)), h, "L=c*((Ib*c)*Ib)=h"],
  [op(ib, h), c, "Ib*h=c"],
  [op(z, ib), ic, "z*Ib=Ic"],
  [op(p, c), t, "p*c=T"],
  [op(q, c), s, "q*c=S"],
  [op(u, z), ib, "U*z=Ib"],
  [op(w, z), ib, "W*z=Ib"],
  [op(u, z), op(w, z), "U*z=W*z"],
  [op(p, c), op(u, h), "p*c=U*h"],
  [op(q, c), op(w, h), "q*c=W*h"],
  [zb, bc, "shifted bridge output hit ZB=BC"],
  [zb, cz, "triangle output hit ZB=CZ"],
  [bc, cz, "triangle output hit BC=CZ"],
  [h, zb, "shifted bridge input-output hit h=ZB"],
  [h, bc, "shifted bridge input-output hit h=BC"],
  [h, cz, "triangle input-output hit h=CZ"],
  [alpha, ib, "lift input hit alpha=Ib"],
  [alpha, ic, "lift input hit alpha=Ic"],
  [ib, ic, "lift input hit Ib=Ic"],
  [alpha, z, "lift/source hit alpha=z"],
  [alpha, b, "lift/source hit alpha=b"],
  [alpha, c, "lift cross hit alpha=c"],
  [ib, b, "lift cross hit Ib=b"],
  [ib, z, "lift cross hit Ib=z"],
  [ib, c, "lift/source hit Ib=c"],
  [ic, z, "lift/source hit Ic=z"],
  [ic, b, "lift cross hit Ic=b"],
  [ic, c, "lift cross hit Ic=c"],
  [zb, z, "ZB hits source z"],
  [zb, b, "ZB hits source b"],
  [zb, c, "ZB hits source c"],
  [bc, z, "BC hits source z"],
  [bc, b, "BC hits source b"],
  [bc, c, "BC hits source c"],
  [cz, z, "CZ hits source z"],
  [cz, b, "CZ hits source b"],
  [cz, c, "CZ hits source c"],
  [op(h, h), zb, "h*h=ZB"],
  [op(h, alpha), b, "h*alpha=b"],
  [d4(b), b, "E255(b)"],
  [d4(z), z, "E255(z)"],
  [d4(c), c, "E255(c)"],
  [d4(h), h, "E255(h)"],
];

console.log("Anchored period-3 saturation");
console.log(`maxDepth: ${maxDepth}`);
console.log(`formulaRounds: ${formulaRounds}`);
console.log(`maxTerms: ${maxTerms}`);
console.log(`extraAssumptions: ${extraAssumptions.length ? extraAssumptions.join(",") : "none"}`);
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
