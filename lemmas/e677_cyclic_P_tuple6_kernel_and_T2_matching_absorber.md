# Cyclic `P`: tuple-6 kernel lemma and the `T2` matching absorber

Date: 2026-07-26.

Status:

```text
T2 alone, even with seven distinct Bad O7 rows, absorbs every canonical
minimum-curvature D; tuple 6 eliminates the complete natural absorber family
through an exact forced-kernel obstruction
```

## Eliminating `H` from tuple 6

In the cyclic isotope class write

```text
D(C_q(u))=A(q)+B(u).
```

No involutivity assumption on `D` is needed.  For fixed `s,t`, define

```text
q_s(t)=O7_t(s),
z_s(t)=O7_t^(-1)(s),
rho_s(t)=D(q_s(t)-t)-A(q_s(t)).
```

Tuple 6 is

```text
C_(q_s(t))(H_s(z_s(t)))=q_s(t)-t.
```

Applying `D` and using the isotope equation gives the forced cell

```text
H_s(z_s(t))=B^(-1)(rho_s(t)).                  (T6-FORCED)
```

Since `B` is injective, a permutation row `H_s` satisfying all seven forced
cells exists if and only if

```text
z_s(t)=z_s(t')  <=>  rho_s(t)=rho_s(t')        (T6-KERNEL)
```

for every `t,t'`.  Necessity is the function and injection property of
`H_s`.  Conversely, `(T6-KERNEL)` makes the forced relation a partial
bijection, and every partial bijection of a finite set extends to a
permutation.  Thus `(T6-KERNEL)` exactly eliminates `H` from tuple 6.  The
permutation `B` cancels completely from its feasibility test.

## Exact matching criterion for `T2`

For fixed `C,W`, put

```text
f_t(h)=W_h(t-C_t(h)).
```

Choosing permutation rows `H_t` so that

```text
V(r,t)=f_t(H_t(r))
```

has every row `V_r` a permutation is equivalent to edge-colouring the
bipartite multigraph whose left vertices are `t`, right vertices are output
values, and whose edge labelled `h` joins `t` to `f_t(h)`.

Every left degree is seven.  Such `H_t` exist whenever every output value has
global multiplicity seven; then the graph is 7-regular bipartite and splits
into seven perfect matchings.  The matchings are the rows `r`, and their edge
labels define `H_t(r)`.  The converse is immediate by counting values in the
seven permutation rows of `V`.  Hence the exact criterion is

```text
|{(t,h):f_t(h)=v}|=7 for every v.              (T2-BALANCE)
```

This is strictly weaker than requiring each fixed-`t` map `h->f_t(h)` to be
a permutation.

## A nondegenerate universal `T2` absorber

Take

```text
A=B=id,
C_t(h)=D^(-1)(t+h),
W_h(p)=P(h)+p,
P=1046253.
```

The two maps

```text
P(h),
P(h)-h=1623504
```

are permutations, and `P(h)+h` is never zero.  Therefore `W` is Latin, its
Bad diagonal `W_s(s)` is nonzero, and

```text
O7_s(z)=W_(z+s)(s)=P(z+s)+s
```

has seven distinct permutation rows and all required cyclic transversals.
Moreover, with `x=t+h`,

```text
f_t(h)=(P(h)-h)+(x-D^(-1)(x)).
```

For each fixed `x`, the first term runs through all seven values.  Thus
`(T2-BALANCE)` holds for every permutation `D`.  The perfect-matching
construction gives explicit permutation rows `H,V`.  The verifier constructs
and audits them for all four canonical minimum-curvature `D`.

Consequently no `T2`-only collision lemma can exclude the four-transversal
layer, even after requiring Badness and seven distinct `O7` rows.

## Tuple-6 exclusion of the complete natural family

Classify every permutation `P` satisfying

```text
P-id is a permutation,
P(h)+h != 0 for every h,
the seven O7 rows are distinct.
```

There are exactly `42`.  They all give the same complete-mapping `T2`
absorber construction above.  Against the four canonical harmonic
double-swap maps `D`, all `42*4=168` pairs violate `(T6-KERNEL)`:

```text
D=0125634: 31 forced-cell conflicts, 11 forced-value collisions;
D=0145236: 32 forced-cell conflicts, 10 forced-value collisions;
D=1023546: 19 forced-cell conflicts, 23 forced-value collisions;
D=1024356: 22 forced-cell conflicts, 20 forced-value collisions;
total survivors: 0.
```

A forced-cell conflict assigns two values to one `H_s(z)`.  A forced-value
collision assigns one value to two different inputs in the same permutation
row.  Hence this is an exact tuple-6 exclusion of the full natural absorber
family, not a timeout boundary.

It does not exclude arbitrary nonlinear `W` or nonidentity `A,B`.

## Continuation

Use `(T6-KERNEL)` before constructing `H`.  In the four-transversal layer the
next object is the seven equality partitions

```text
ker(t -> O7_t^(-1)(s))
=ker(t -> D(O7_t(s)-t)-A(O7_t(s))).
```

They couple `A,D,O7` but not `B`.  Only after these kernels agree should the
remaining partial bijections be extended and tested against `(T2-BALANCE)`.
Do not search for a `T2` collision alone or revisit the complete-mapping
translation-row family.

## Verification

```text
python tools/e677_fiber7_T2_matching_absorber_verify.py
python tools/e677_fiber7_T2_complete_mapping_family_classify.py
```
