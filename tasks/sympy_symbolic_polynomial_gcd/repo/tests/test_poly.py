import pytest
from polynomial import poly_gcd

def test_simple_gcd():
    # (x - 1)*(x - 2) = x^2 - 3x + 2 -> [2, -3, 1]
    # (x - 1)*(x - 3) = x^2 - 4x + 3 -> [3, -4, 1]
    # GCD is (x - 1) -> [-1.0, 1.0]
    assert poly_gcd([2.0, -3.0, 1.0], [3.0, -4.0, 1.0]) == [-1.0, 1.0]

def test_coprime_polynomials():
    # x - 1 and x + 1 -> GCD is 1.0
    assert poly_gcd([-1.0, 1.0], [1.0, 1.0]) == [1.0]

def test_near_zero_coefficient_snapping():
    # Floating point arithmetic drift
    p1 = [2.000000000001, -3.0, 1.0]
    p2 = [3.000000000001, -4.0, 1.0]
    assert poly_gcd(p1, p2) == [-1.0, 1.0]
