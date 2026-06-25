% Anchored-X3 M7 self-repeat residual for E677.
%
% Purpose:
%   A small ATP-style template for the current clean false branch
%   of the shared-step anchored triangle.
%
% This is not a full proof of E677 -> E255.  It is a narrow formalization
% of the current residual:
%
%   p*b=q*b=z,
%   U=p*z,
%   W=q*z,
%   h=U*p=W*q,
%   z*h=b,
%   T=U*h,
%   S=W*h,
%   T!=S,
%
% and of the first fixed-target source-successor layer in H_h.
%
% TPTP convention:
%   f(x,y) means x*y.

fof(e677, axiom,
    ! [X,Y] : f(Y, f(X, f(f(Y,X), Y))) = X).

% Finite E677 gives left rows as permutations.  We encode only the
% left-cancellation direction used by the local lemmas.
fof(left_cancel, axiom,
    ! [R,X,Y] : (f(R,X) = f(R,Y) => X = Y)).

% Standard derived consequences used throughout the project.  They are
% included as axioms here so the ATP task stays focused on the M7 residual.
fof(edge_predecessor_formula, axiom,
    ! [R,H,O,I] :
      ((f(R,I) = H & f(R,H) = O) => I = f(H, f(O,R)))).

fof(fixed_target_source_successor_formula, axiom,
    ! [R,H,O] :
      (f(R,H) = O => f(O, f(f(R,O), R)) = H)).

% Anchored shared-step data.
fof(shared_step_p, axiom, f(p,b) = z).
fof(shared_step_q, axiom, f(q,b) = z).
fof(def_u, axiom, f(p,z) = u).
fof(def_w, axiom, f(q,z) = w).
fof(def_h_u, axiom, f(u,p) = h).
fof(def_h_w, axiom, f(w,q) = h).
fof(z_h_b, axiom, f(z,h) = b).
fof(alpha_pred, axiom, f(z,alpha) = h).

% False branch of the strong anchored identity.
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

% Clean local false-branch assumptions: no immediate incoming fan and no
% visible period-1 / period-2 right-h source-repeat.
fof(no_t_eq_u, axiom, t != u).
fof(no_s_eq_w, axiom, s != w).
fof(no_b_eq_z, axiom, b != z).
fof(no_t_h_u, axiom, f(t,h) != u).
fof(no_s_h_w, axiom, f(s,h) != w).
fof(no_b_h_z, axiom, f(b,h) != z).

% Named next source rows for a possible later/fresh M7 repeat study.
fof(def_t1, axiom, f(t,h) = t1).
fof(def_s1, axiom, f(s,h) = s1).
fof(def_b1, axiom, f(b,h) = b1).

% ---------------------------------------------------------------------------
% Conjecture block.
%
% Replace this conjecture with a concrete proposed M7 consequence.  Examples:
%
%   fof(conj, conjecture, t1 = s1).
%   fof(conj, conjecture, t1 = b1).
%   fof(conj, conjecture, f(t1,h) = t).
%
% The default conjecture is deliberately weak and should not be interpreted
% as a project claim.  It only checks that the template loads as a TPTP file.
% ---------------------------------------------------------------------------

fof(template_loads, conjecture,
    t = t).
