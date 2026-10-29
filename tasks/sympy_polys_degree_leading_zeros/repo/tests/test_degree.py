from sympy_polys.degree import poly_degree

def test_normalized_polynomial():
    assert poly_degree([2, 0, -1]) == 2
    assert poly_degree([5]) == 0

def test_leading_zeros_and_zero_poly():
    assert poly_degree([0, 0, 3, 1]) == 1
    assert poly_degree([0, 0]) == -1
