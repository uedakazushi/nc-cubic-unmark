#!/usr/bin/env python3
"""Exact cubic Riemann--Roch checks, not proofs of existence or of (EP)."""
import sympy as sp


def main() -> None:
    gram = sp.diag(1, *([-1] * 6))
    canonical = sp.Matrix([-3, 1, 1, 1, 1, 1, 1])
    divisor = sp.Matrix(sp.symbols('d0:7'))
    other = sp.Matrix(sp.symbols('f0:7'))
    rank, other_rank, s, t, m, n = sp.symbols('r rprime s t m n')
    product = lambda a, b: (a.T * gram * b)[0]

    def chi(v, w):
        r, d, c = v
        rp, dp, cp = w
        return sp.expand(r*rp+r*cp+rp*c-product(d,dp)
                         -product(canonical, r*dp-rp*d)/2)

    def twist(v, power):
        r, d, c = v
        return (r, d-power*r*canonical,
                c-power*product(d,canonical)+power**2*r*sp.Rational(3,2))

    assert product(canonical, canonical) == 3
    v = (rank, divisor, s)
    w = (other_rank, other, t)
    line = (1, divisor, product(divisor,divisor)/2)
    ideal = (1, divisor, product(divisor,divisor)/2-n)
    assert sp.expand(chi(v, w)-chi(twist(v,m),twist(w,m))) == 0
    assert sp.expand(chi(v,w)-chi(w,twist(v,-1))) == 0  # S = H^{-1}[2]
    assert sp.expand(chi(ideal,ideal)-(1-2*n)) == 0
    assert sp.expand(chi(line,twist(line,m))-(1+3*m*(m+1)/2)) == 0
    assert sp.expand(product(-canonical,twist(line,-1)[1]-line[1])) == -3
    # D^2 - K.D is even for every integral D, checked on the diagonal parity formula.
    parity_difference = sp.expand(product(divisor,divisor)-product(canonical,divisor))
    expected = divisor[0]*(divisor[0]+3)-sum(divisor[i]*(divisor[i]-1) for i in range(1,7))
    assert sp.expand(parity_difference-expected) == 0
    # Non-exceptional rank-one example with one-point defect.
    assert chi(ideal,ideal).subs(n,1) == -1
    print('PASS: self Euler=1-2n, Ext1 numerical value=2n; anticanonical Hilbert polynomial')
    print('PASS: Serre duality, H-invariance, same-class negative quotient degree=-3; parity')
    print('LIMIT: categorical existence, positivity (EP), and heart/rank comparison are not tested')


if __name__ == '__main__':
    main()
