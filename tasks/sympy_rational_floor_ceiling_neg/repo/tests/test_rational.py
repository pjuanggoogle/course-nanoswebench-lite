from sympy_rat.rational import Rational

def test_positive_rational():
    r = Rational(7, 3)
    assert r.floor() == 2
    assert r.ceiling() == 3

def test_negative_numerator_and_denominator():
    r1 = Rational(-7, 3)
    assert r1.floor() == -3
    assert r1.ceiling() == -2
    r2 = Rational(7, -3)
    assert (r2.p, r2.q) == (-7, 3)
    assert r2.floor() == -3
    assert r2.ceiling() == -2
