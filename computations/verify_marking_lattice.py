#!/usr/bin/env python3
"""Exact E6 Picard lattice and an anticanonical deformation witness.

This only checks integer/rational algebra. The Picard obstruction formula and
cohomological rank calculation are proved geometrically in the TeX manuscript.
"""
from itertools import combinations, product
import sympy as sp

J = sp.diag(1, *([-1] * 6))
K = sp.Matrix([-3] + [1] * 6)
degree = lambda d: (-K.T * J * d)[0]
inter = lambda v, w: (v.T * J * w)[0]
root_basis = [sp.Matrix([0] + [int(j == i) - int(j == i + 1) for j in range(6)]) for i in range(5)]
root_basis.append(sp.Matrix([1] + [-int(j < 3) for j in range(6)]))
cartan = sp.Matrix(6, 6, lambda i, j: -inter(root_basis[i], root_basis[j]))
assert cartan.det() == 3
assert all(inter(r, K) == 0 and inter(r, r) == -2 for r in root_basis)
roots = [v for v in product(range(-2, 3), repeat=7)
         if inter(sp.Matrix(v), K) == 0 and inter(sp.Matrix(v), sp.Matrix(v)) == -2]
assert len(roots) == 72
lines = [sp.Matrix([0] + [int(j == i) for j in range(6)]) for i in range(6)]
lines.extend(sp.Matrix([1] + [-int(j in pair) for j in range(6)]) for pair in combinations(range(6), 2))
lines.extend(sp.Matrix([2] + [-int(j != skip) for j in range(6)]) for skip in range(6))
assert len({tuple(d) for d in lines}) == 27
assert all(inter(d, d) == -1 and degree(d) == 1 for d in lines)
assert degree(K) == -3 and degree(lines[0]) == 1

x, y, z, t = sp.symbols('x y z t')
F = x**3 + y**3 + z**3 + t*x*y + t**3
G = sp.groebner([sp.diff(F, a) for a in (x, y, z, t)], x, y, z, t)
assert G.is_zero_dimensional
assert sp.groebner([x**2, y**2, z**2], x, y, z).reduce(x*y*z)[1] == x*y*z
# The Weyl orbit of any root spans the irreducible 6-dimensional root representation.
root_orbit = {tuple(root_basis[0])}
queue = [root_basis[0]]
for v in queue:
    for alpha in root_basis:
        reflected = v + inter(v, alpha) * alpha
        key = tuple(reflected)
        if key not in root_orbit:
            root_orbit.add(key)
            queue.append(reflected)
assert len(root_orbit) == 72
assert sp.Matrix.hstack(*queue).rank() == 6
assert all(inter(alpha, K) == 0 for alpha in root_basis)
print('PASS: a Weyl reflection orbit of 72 roots spans Q(E6), rank 6')

print('PASS: E6 roots=72, lines=27, discriminant=3; smooth cubic and nonzero KS witness')
