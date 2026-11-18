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
    # Hilbert polynomial with an arbitrary normalized structure line.
    degree_v = product(-canonical, divisor)
    degree_o = product(-canonical, other)
    base = (1, other, product(other, other)/2)
    hilbert = sp.Rational(3,2)*rank*m*(m+1)+(degree_v-rank*degree_o)*m+chi(base,v)
    assert sp.expand(chi(base,twist(v,m))-hilbert) == 0
    # Conditional root-simple evaluation: C^2=-2, K.C=0, s=C.D0+c.
    c, root_dot_base, base_square = sp.symbols('c root_dot_base base_square')
    root_square = -2
    kernel_square = base_square-2*c*root_dot_base+c*c*root_square
    kernel_ch2 = base_square/2-c*(root_dot_base+c)
    assert sp.expand(kernel_square/2-kernel_ch2) == 0
    assert 1-c*c-c*c+2*c*c == 1
    # A root C has C^2=-2. For a=s_T-D.C=h-b, the universal
    # extension by b copies of T has defect -b*h.
    hdim, bdim, dc, dsq = sp.symbols('hdim bdim dc dsq')
    sval = dc + hdim - bdim
    extension_square = dsq + 2*bdim*dc - 2*bdim**2
    extension_ch2 = dsq/2 + bdim*sval
    assert sp.expand(extension_square/2-extension_ch2+bdim*hdim) == 0
    aval = sval-dc
    reflected_square = dsq-2*aval*dc-2*aval**2
    reflected_ch2 = dsq/2-aval*sval
    assert sp.expand(reflected_square/2-reflected_ch2) == 0
    reflected_pairing = dc+2*aval
    assert sp.expand(sval-reflected_pairing+aval) == 0
    # (H-1)^2 v = (0,0,3r), used to recognize rank intrinsically.
    hv, hhv = twist(v, 1), twist(v, 2)
    assert hhv[0]-2*hv[0]+v[0] == 0
    assert hhv[1]-2*hv[1]+v[1] == sp.zeros(7, 1)
    assert sp.expand(hhv[2]-2*hv[2]+v[2]-3*rank) == 0
    # Twisting identities retained as numerical checks only.
    structure = (1, sp.zeros(7, 1), 0)
    theta_v = twist(v, -1)
    degree = product(-canonical, divisor)
    assert sp.expand(chi(structure,theta_v)-chi(structure,v)+degree) == 0
    assert sp.expand(product(-canonical,theta_v[1]-divisor)+3*rank) == 0
    assert sp.expand(product(-canonical,divisor-theta_v[1])-3*rank) == 0
    # D^2 - K.D is even for every integral D, checked on the diagonal parity formula.
    parity_difference = sp.expand(product(divisor,divisor)-product(canonical,divisor))
    expected = divisor[0]*(divisor[0]+3)-sum(divisor[i]*(divisor[i]-1) for i in range(1,7))
    assert sp.expand(parity_difference-expected) == 0
    # Non-exceptional rank-one example with one-point defect.
    assert chi(ideal,ideal).subs(n,1) == -1
    print('PASS: self Euler=1-2n, Ext1 numerical value=2n; anticanonical Hilbert polynomial')
    print('PASS: Serre duality, H-invariance, same-class negative quotient degree=-3; parity')
    print('PASS: arbitrary-base Hilbert polynomial; conditional root-evaluation defect=0')
    print('PASS: root universal-extension defect=-b*h; affine reflection and involution')
    print('PASS: (H-1)^2 v=3r[point]')
    print('PASS: twist quotient degree=3r, theta Euler difference=-degree')
    print('LIMIT: categorical existence, positivity (EP), and heart/rank comparison are not tested')


if __name__ == '__main__':
    main()
