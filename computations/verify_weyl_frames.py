#!/usr/bin/env python3
"""Exact E6/AOU frame checks; no categorical realization is inferred.

Only Python's standard library is needed. Divisors have coordinates
(h,e1,...,e6); Chern vectors use (rank,c1,2*ch2) to avoid fractions.
"""
from itertools import combinations, product
from math import factorial


ZERO = (0,) * 7
BASIS = tuple(tuple(int(i == j) for i in range(7)) for j in range(7))
h, *e = BASIS


def add(*vectors):
    return tuple(sum(items) for items in zip(*vectors))


def scale(n, v):
    return tuple(n * x for x in v)


def sub(v, w):
    return add(v, scale(-1, w))


def dot(v, w):
    return v[0] * w[0] - sum(a * b for a, b in zip(v[1:], w[1:]))


K = add(scale(-3, h), *e)


def reflection(v, alpha):
    return add(v, scale(dot(v, alpha), alpha))


def chi(d, f):
    difference = sub(f, d)
    numerator = dot(difference, difference) - dot(K, difference)
    assert numerator % 2 == 0
    return 1 + numerator // 2


def ch(d):
    return (1, *d, dot(d, d))


def main():
    lines = list(e)
    lines += [sub(h, add(e[i], e[j])) for i, j in combinations(range(6), 2)]
    lines += [sub(scale(2, h), add(*(e[j] for j in range(6) if j != i)))
              for i in range(6)]
    assert len(set(lines)) == 27
    assert all(dot(v, v) == -1 and dot(K, v) == -1 for v in lines)
    # If v=(t,b1,...,b6), the two equations imply sum(b)=1-3t and
    # sum(b^2)=t^2+1. Cauchy gives 3t^2-6t-5 <= 0, so t=0,1,2
    # and |bi|<=2. Thus this finite search is exhaustive.
    numerical_lines = {(t, *b) for t in range(3)
                       for b in product(range(-2, 3), repeat=6)
                       if sum(b) == 1 - 3*t and sum(n*n for n in b) == t*t + 1}
    assert set(lines) == numerical_lines
    # Orthogonal six-tuples are enumerated as unordered cliques, then ordered.
    sixes = []

    def extend(chosen, candidates):
        if len(chosen) == 6:
            sixes.append(chosen)
            return
        if len(chosen) + len(candidates) < 6:
            return
        for place, i in enumerate(candidates):
            extend(chosen + (i,), tuple(j for j in candidates[place + 1:]
                                       if dot(lines[i], lines[j]) == 0))

    extend((), tuple(range(27)))
    assert len(sixes) == 72
    assert len(sixes) * factorial(6) == 51840
    for six in sixes:
        exceptional = [lines[i] for i in six]
        numerator = sub(add(*exceptional), K)
        assert all(n % 3 == 0 for n in numerator)
        plane = tuple(n // 3 for n in numerator)
        assert dot(plane, plane) == 1
        assert all(dot(plane, v) == 0 for v in exceptional)

    a, b = add(K, h), sub(add(*e[:3]), h)
    x, y = e[:3], [sub(h, v) for v in e[3:]]
    roots = [sub(e[i], e[i + 1]) for i in range(5)] + [sub(a, b)]
    cartan = [[-dot(v, w) for w in roots] for v in roots]
    assert cartan == [
        [2, -1, 0, 0, 0, 0], [-1, 2, -1, 0, 0, 0],
        [0, -1, 2, -1, 0, -1], [0, 0, -1, 2, -1, 0],
        [0, 0, 0, -1, 2, 0], [0, 0, -1, 0, 0, 2]]
    for alpha in roots:
        assert dot(alpha, alpha) == -2 and dot(alpha, K) == 0
        for v in BASIS:
            assert reflection(reflection(v, alpha), alpha) == v
    for i, j in combinations(range(6), 2):
        order = 3 if cartan[i][j] == -1 else 2
        for v in BASIS:
            w = v
            for _ in range(order):
                w = reflection(reflection(w, roots[j]), roots[i])
            assert w == v

    vertices = [ZERO, a, b, *x, *y]
    expected_euler = [[int(i == j) if i // 3 == j // 3 else
                       (j // 3 - i // 3 if i // 3 < j // 3 else 0)
                       for j in range(9)] for i in range(9)]
    assert [[chi(v, w) for w in vertices] for v in vertices] == expected_euler
    recovered_h = sub(add(*x), b)
    assert [recovered_h, *x, *(sub(recovered_h, v) for v in y)] == list(BASIS)
    # Five of the six simple reflections only relabel orthogonal vertices.
    for root_index, (i, j) in [(0, (3, 4)), (1, (4, 5)),
                                (3, (6, 7)), (4, (7, 8)), (5, (1, 2))]:
        expected = vertices.copy()
        expected[i], expected[j] = expected[j], expected[i]
        assert [reflection(v, roots[root_index]) for v in vertices] == expected

    moved = [ZERO, a, sub(add(x[0], x[1]), y[0]), x[0], x[1],
             sub(h, y[0]), sub(h, x[2]), y[1], y[2]]
    assert [reflection(v, roots[2]) for v in vertices] == moved
    old = [ch(v) for v in vertices]
    assert sub(add(old[3], old[4]), old[6]) == ch(moved[2])
    assert sub(add(old[3], old[4]), old[2]) == ch(moved[6])
    assert sub(add(old[3], old[4], old[5]), add(old[2], old[6])) == ch(moved[5])
    print('PASS: 27 numerical (-1)-classes; 72 sixers; 51840 ordered frames')
    print('PASS: E6 simple roots, K preservation, all Coxeter relations')
    print('PASS: AOU Euler matrix, frame recovery, five block relabelings')
    print('PASS: cross-block reflection and three candidate K0/Chern formulas')
    print('LIMIT: line existence, exactness of candidate maps, and helix conditions are not tested')


if __name__ == '__main__':
    main()
