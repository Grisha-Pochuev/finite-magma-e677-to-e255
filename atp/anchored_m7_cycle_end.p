% Anchored-M7 cycle-end template for E677.
%
% Purpose:
%   Formalize the remaining clean same-orbit right-h self-repeat after
%   anchored_m7_first_event_routing_lemma.md.
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

% Anchored shared-step data and false branch.
fof(shared_step_p, axiom, f(p,b) = z).
fof(shared_step_q, axiom, f(q,b) = z).
fof(def_u, axiom, f(p,z) = u).
fof(def_w, axiom, f(q,z) = w).
fof(def_h_u, axiom, f(u,p) = h).
fof(def_h_w, axiom, f(w,q) = h).
fof(z_h_b, axiom, f(z,h) = b).
fof(alpha_pred, axiom, f(z,alpha) = h).
fof(def_t, axiom, f(u,h) = t).
fof(def_s, axiom, f(w,h) = s).
fof(false_branch, axiom, t != s).

% Back-projection consequences.
fof(back_project_p, axiom, f(h, f(t,u)) = p).
fof(back_project_q, axiom, f(h, f(s,w)) = q).
fof(back_project_alpha, axiom, f(h, f(b,z)) = alpha).

% First source-successor layer in H_h.
fof(next_t_edge, axiom, f(t, f(f(u,t), u)) = h).
fof(next_s_edge, axiom, f(s, f(f(w,s), w)) = h).
fof(next_b_edge, axiom, f(b, f(f(z,b), z)) = h).

% Clean visible short-repeat exclusions.
fof(no_t_eq_u, axiom, t != u).
fof(no_s_eq_w, axiom, s != w).
fof(no_b_eq_z, axiom, b != z).
fof(no_t_h_u, axiom, f(t,h) != u).
fof(no_s_h_w, axiom, f(s,h) != w).
fof(no_b_h_z, axiom, f(b,h) != z).

% ---------------------------------------------------------------------------
% Cycle-end residual.
%
% r0 is a chosen source row in the clean self-repeat orbit.
% r1 is its next right-h successor.
% rm2 and rm1 are the next-to-last and last source rows before returning to r0.
%
%   r0*h  = r1
%   rm2*h = rm1
%   rm1*h = r0
%
% Each source row carries an H_h edge:
%
%   i0  -> r1   by row r0
%   im2 -> rm1  by row rm2
%   im1 -> r0   by row rm1
% ---------------------------------------------------------------------------

fof(cycle_start, axiom, f(r0,h) = r1).
fof(cycle_next_to_last, axiom, f(rm2,h) = rm1).
fof(cycle_last, axiom, f(rm1,h) = r0).

fof(edge_r0_input, axiom, f(r0,i0) = h).
fof(edge_rm2_input, axiom, f(rm2,im2) = h).
fof(edge_rm1_input, axiom, f(rm1,im1) = h).

fof(edge_r0_output, axiom, f(r0,h) = r1).
fof(edge_rm2_output, axiom, f(rm2,h) = rm1).
fof(edge_rm1_output, axiom, f(rm1,h) = r0).

% The predecessor formulas are included explicitly so ATP runs can focus on
% cycle-end consequences instead of rediscovering them.
fof(pred_i0, axiom, i0 = f(h, f(r1,r0))).
fof(pred_im2, axiom, im2 = f(h, f(rm1,rm2))).
fof(pred_im1, axiom, im1 = f(h, f(r0,rm1))).

% Clean cycle-end assumptions: the displayed three H_h edges are not already
% a routed fan/path/full-interval hit.  Remove or weaken these when testing a
% specific collision route.
fof(clean_sources_01, axiom, r0 != r1).
fof(clean_sources_0m1, axiom, r0 != rm1).
fof(clean_sources_0m2, axiom, r0 != rm2).
fof(clean_sources_m2m1, axiom, rm2 != rm1).
fof(clean_inputs_0m1, axiom, i0 != im1).
fof(clean_inputs_0m2, axiom, i0 != im2).
fof(clean_inputs_m2m1, axiom, im2 != im1).
fof(no_start_input_output_hit, axiom, i0 != rm1).
fof(no_end_input_output_hit, axiom, im1 != r1).

% ---------------------------------------------------------------------------
% Conjecture block.
%
% Replace with a concrete proposed consequence.  Useful first tests:
%
%   fof(conj, conjecture, im1 = r1).
%   fof(conj, conjecture, f(r0,r1) = f(rm1,r0)).
%   fof(conj, conjecture, f(r1, f(f(r0,r1), r0)) = h).
%
% The default conjecture only checks that the template loads.
% ---------------------------------------------------------------------------

fof(template_loads, conjecture,
    r0 = r0).
