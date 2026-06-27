% Period-3 zipper target template for E677.
%
% Purpose:
%   Test whether the clean period-3 fixed-target zipper already forces E255
%   for one of the displayed period-3 vertices.
%
% TPTP convention:
%   f(x,y) means x*y.

fof(e677, axiom,
    ! [X,Y] : f(Y, f(X, f(f(Y,X), Y))) = X).

fof(left_cancel, axiom,
    ! [R,X,Y] : (f(R,X) = f(R,Y) => X = Y)).

fof(edge_predecessor_formula, axiom,
    ! [R,H,O,I] :
      ((f(R,I) = H & f(R,H) = O) => I = f(H, f(O,R)))).

fof(fixed_target_source_successor_formula, axiom,
    ! [R,H,O] :
      (f(R,H) = O => f(O, f(f(R,O), R)) = H)).

% Period-3 right-h source cycle:
%
%   z*h=b,
%   b*h=c,
%   c*h=z.

fof(z_h_b, axiom, f(z,h) = b).
fof(b_h_c, axiom, f(b,h) = c).
fof(c_h_z, axiom, f(c,h) = z).

% H_h zipper inputs:
%
%   alpha -> b  carried by row z,
%   ib    -> c  carried by row b,
%   ic    -> z  carried by row c.

fof(z_alpha_h, axiom, f(z,alpha) = h).
fof(b_ib_h, axiom, f(b,ib) = h).
fof(c_ic_h, axiom, f(c,ic) = h).

fof(pred_alpha, axiom, alpha = f(h, f(b,z))).
fof(pred_ib, axiom, ib = f(h, f(c,b))).
fof(pred_ic, axiom, ic = f(h, f(z,c))).

% Zipper formulas.

fof(zip_alpha, axiom, alpha = f(f(c,z), c)).
fof(zip_ib, axiom, ib = f(f(z,b), z)).
fof(zip_ic, axiom, ic = f(f(b,c), b)).

% Target-advanced outputs.

fof(def_zb, axiom, zb = f(z,b)).
fof(def_bc, axiom, bc = f(b,c)).
fof(def_cz, axiom, cz = f(c,z)).

% Clean period-3 assumptions.  Remove these if testing a routed case.

fof(clean_z_b, axiom, z != b).
fof(clean_z_c, axiom, z != c).
fof(clean_b_c, axiom, b != c).
fof(clean_h_z, axiom, h != z).
fof(clean_h_b, axiom, h != b).
fof(clean_h_c, axiom, h != c).
fof(clean_inputs_alpha_ib, axiom, alpha != ib).
fof(clean_inputs_alpha_ic, axiom, alpha != ic).
fof(clean_inputs_ib_ic, axiom, ib != ic).
fof(clean_outputs_zb_bc, axiom, zb != bc).
fof(clean_outputs_zb_cz, axiom, zb != cz).
fof(clean_outputs_bc_cz, axiom, bc != cz).
fof(clean_zb_z, axiom, zb != z).
fof(clean_zb_b, axiom, zb != b).
fof(clean_zb_c, axiom, zb != c).
fof(clean_bc_z, axiom, bc != z).
fof(clean_bc_b, axiom, bc != b).
fof(clean_bc_c, axiom, bc != c).
fof(clean_cz_z, axiom, cz != z).
fof(clean_cz_b, axiom, cz != b).
fof(clean_cz_c, axiom, cz != c).

% ---------------------------------------------------------------------------
% Conjecture block.
%
% Useful tests:
%
%   E255 for the bad-target candidate b:
%     fof(conj, conjecture, f(f(f(b,b),b),b) = b).
%
%   E255 for the whole period-3 source triangle:
%     fof(conj, conjecture,
%       f(f(f(z,z),z),z) = z &
%       f(f(f(b,b),b),b) = b &
%       f(f(f(c,c),c),c) = c).
%
%   db fingerprint candidates:
%     fof(conj, conjecture, f(h,h) = zb).
%     fof(conj, conjecture, f(h,alpha) = b).
%     fof(conj, conjecture, f(z,ib) = ic).
%
% The default conjecture only checks that the template loads.
% ---------------------------------------------------------------------------

fof(template_loads, conjecture,
    z = z).

