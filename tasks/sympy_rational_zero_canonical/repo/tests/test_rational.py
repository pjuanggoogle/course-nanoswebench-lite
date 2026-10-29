from sympy_core.rational import canonical_rational

def test_positive_reduction():
    assert canonical_rational(6, 9) == (2, 3)

def test_negative_denominator_and_zero():
    assert canonical_rational(2, -4) == (-1, 2)
    assert canonical_rational(-2, -4) == (1, 2)
    assert canonical_rational(0, -7) == (0, 1)
