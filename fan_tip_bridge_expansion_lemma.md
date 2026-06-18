# Fan-Tip Bridge Expansion Lemma

Date: 2026-06-08.

Status:

```text
general proved / recursive double-interval pressure mechanism
```

## Setup

Assume a self-containing common-edge fan:

```text
q*0=P
q*P=T_q
T_q*q=h
P*h=0.
```

The value:

```text
h=pred_P(0)
```

is common to all fan sources.

For every source `q`, define:

```text
u_q=q*T_q
w_q=u_q*q=(q*T_q)*q.
```

## Tip Bridge

Lemma 13.1(iii), applied with:

```text
x=P
y=q,
```

gives:

```text
P=(q*P)*((q*(q*P))*q).
```

Therefore:

```text
T_q*w_q=P.
```

Every original fan source creates the bridge:

```text
row q:
  0 -> P -> T_q

row T_q:
  q   -> h
  w_q -> P.
```

The two columns in row `T_q` are distinct:

```text
w_q!=q,
```

because:

```text
T_q*q=h
T_q*w_q=P
h!=P.
```

## Internal-Tip Equivalence

The bridge is zero exactly when the tip is itself a source:

```text
w_q=0
<=>
T_q*0=P
<=>
T_q in F(0,P).
```

Thus:

```text
internal fan tip
<=>
zero bridge.
```

In this case:

```text
(q*T_q)*q=0,
```

which is exactly the tip-source collision zero tooth.

## Right-Fixed Tip Equivalence

The bridge equals `P` exactly when the tip fixes `P` on the right:

```text
w_q=P
<=>
T_q*P=P.
```

Proof:

If `w_q=P`, then:

```text
T_q*P=P.
```

Conversely, if `T_q*P=P`, row `T_q` sends both:

```text
P   -> P
w_q -> P.
```

Left-row injectivity gives:

```text
w_q=P.
```

If `P` is good, so that:

```text
h*P=P,
```

then:

```text
T_q=h
<=>
w_q=P.
```

For the reverse implication, `w_q=P` gives `T_q*P=P`. Both `T_q` and `h`
then contain the repeated interval:

```text
P -> P -> P.
```

Two-step source reconstruction gives `T_q=h`. This uses uniqueness of a
right fixed point, not general right cancellativity.

## Bridge-Collision Expansion

Suppose two distinct fan sources satisfy:

```text
w_p=w_q=w.
```

Their tips are distinct:

```text
T_p!=T_q.
```

Both tip rows contain the common edge:

```text
w -> P.
```

Therefore the common-edge fan lemma applies again.

Define:

```text
V_p=T_p*P
V_q=T_q*P.
```

Then:

```text
V_p!=V_q
V_p*T_p=V_q*T_q=pred_P(w).
```

Thus a collision among bridge columns does not end the pressure. It creates a
second-generation fan:

```text
sources: T_p,T_q
common edge: w -> P
distinct tips: V_p,V_q
common hub: pred_P(w).
```

## No-Collision Branch

If no two bridges collide, then:

```text
q -> w_q
```

is injective on the original source fiber.

Thus every common-edge fan has the dichotomy:

```text
bridge collision
  -> a second-generation common-edge fan;

no bridge collision
  -> one distinct bridge column per original source.
```

Together with the two-sided fan lemma, every source then carries:

```text
alpha_q -> 0 -> P -> T_q
```

and its tip row carries:

```text
q   -> h
w_q -> P.
```

## Exact Six-Cycle Form

For the self source:

```text
q=P
T_P=C
u_P=P*C=f
w_P=f*P=k.
```

Therefore the six-cycle classifier:

```text
k=f*P
```

is exactly the self-source tip bridge:

```text
C*k=P.
```

The good six-cycle cross-ladder is the first member of this general bridge
expansion, not a separate numerical phenomenon.

## Significance

This is the recursive double-interval pressure mechanism:

```text
common edge
-> distinct tips and common hub
-> one bridge back to the common middle value per tip
-> either distinct bridge expansion
   or a new common-edge fan at a bridge collision.
```

The remaining termination theorem must show that this recursion cannot stay
inside a finite bad-cycle counterexample while all new bridges, tips, and hubs
avoid the already classified zero and descent roles.

The next forced step after every bridge is recorded in:

```text
fan_bridge_zipper_extension_lemma.md
```

If:

```text
T*w=P
V=T*P,
```

then:

```text
V*T=pred_P(w).
```

Thus every bridge intersection with a known row-`P` point has an explicit
return.
