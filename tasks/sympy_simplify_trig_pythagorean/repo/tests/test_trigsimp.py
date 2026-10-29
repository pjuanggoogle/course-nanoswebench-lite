from sympy_trig.trigsimp import simplify_pythagorean

def test_unit_pythagorean():
    assert simplify_pythagorean({"sin2": 1, "cos2": 1}) == {"const": 1}

def test_scaled_and_offset_pythagorean():
    assert simplify_pythagorean({"sin2": 5, "cos2": 5, "const": 2}) == {"const": 7}
    assert simplify_pythagorean({"sin2": -3, "cos2": -3, "const": 3}) == {}
