% E677 complete synchronized fixed-band experiment.
% f(x,y) means x*y.
fof(e677, axiom,
    ! [X,Y] : f(Y, f(X, f(f(Y,X), Y))) = X).
fof(left_cancel, axiom,
    ! [R,X,Y] : (f(R,X) = f(R,Y) => X = Y)).
fof(z_h_b, axiom, f(z,h) = b).
fof(b_h_c, axiom, f(b,h) = c).
fof(c_h_z, axiom, f(c,h) = z).
fof(b_ib_h, axiom, f(b,ib) = h).
fof(strict_zb, axiom, z != b).
fof(strict_bc, axiom, b != c).
fof(strict_cz, axiom, c != z).

% Complete band position 0.
fof(r0_b_z, axiom, f(r0,b) = z).
fof(r0_z_t0, axiom, f(r0,z) = t0).
fof(t0_b_r0, axiom, f(t0,b) = r0).
fof(t0_ib_r1, axiom, f(t0,ib) = r1).
fof(t0_r0_h, axiom, f(t0,r0) = h).
fof(h_t0_p0, axiom, f(h,t0) = p0).
fof(r0_p0_b, axiom, f(r0,p0) = b).
fof(p0_b_z, axiom, f(p0,b) = z).
fof(p0_z_v0, axiom, f(p0,z) = v0).
fof(v0_ib_p0, axiom, f(v0,ib) = p0).
fof(v0_p0_h, axiom, f(v0,p0) = h).

% Complete band position 1.
fof(r1_b_z, axiom, f(r1,b) = z).
fof(r1_z_t1, axiom, f(r1,z) = t1).
fof(t1_b_r1, axiom, f(t1,b) = r1).
fof(t1_ib_r0, axiom, f(t1,ib) = r0).
fof(t1_r1_h, axiom, f(t1,r1) = h).
fof(h_t1_p1, axiom, f(h,t1) = p1).
fof(r1_p1_b, axiom, f(r1,p1) = b).
fof(p1_b_z, axiom, f(p1,b) = z).
fof(p1_z_v1, axiom, f(p1,z) = v1).
fof(v1_ib_p1, axiom, f(v1,ib) = p1).
fof(v1_p1_h, axiom, f(v1,p1) = h).

% Proven cycle and layer separation.
fof(r0_neq_r1, axiom, r0 != r1).
fof(p0_neq_p1, axiom, p0 != p1).
fof(r0_neq_p0, axiom, r0 != p0).
fof(r0_neq_p1, axiom, r0 != p1).
fof(r1_neq_p0, axiom, r1 != p0).
fof(r1_neq_p1, axiom, r1 != p1).

fof(def_a, axiom, a = f(ib,c)).
% Together with p0*z=v0 and left cancellation this proves A=z.
fof(band_bridge, conjecture, f(p0,a) = v0).
