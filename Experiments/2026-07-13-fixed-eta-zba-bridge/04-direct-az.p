% Direct control target from the same fixed-eta relay package.
% f(x,y) means x*y.

fof(e677, axiom,
    ! [X,Y] : f(Y, f(X, f(f(Y,X), Y))) = X).

fof(left_cancel, axiom,
    ! [R,X,Y] : (f(R,X) = f(R,Y) => X = Y)).

fof(z_h_b, axiom, f(z,h) = b).
fof(b_h_c, axiom, f(b,h) = c).
fof(c_h_z, axiom, f(c,h) = z).
fof(b_ib_h, axiom, f(b,ib) = h).
fof(c_ic_h, axiom, f(c,ic) = h).
fof(def_a, axiom, a = f(ib,c)).
fof(def_k, axiom, k = f(a,ib)).
fof(def_zb, axiom, zb = f(z,b)).
fof(r_b_z, axiom, f(r,b) = z).
fof(r_z_u, axiom, f(r,z) = u).
fof(u_r_h, axiom, f(u,r) = h).
fof(fixed_eta, axiom, f(u,ib) = r).
fof(u_c_zb, axiom, f(u,c) = zb).
fof(zb_c_k, axiom, f(zb,c) = k).

fof(direct_az, conjecture, a = z).
