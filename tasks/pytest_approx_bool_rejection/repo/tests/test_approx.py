from pytest_approx.compare import approx_equal

def test_numeric_approx():
    assert approx_equal(1.0000001, 1.0) is True
    assert approx_equal(1.1, 1.0) is False

def test_bool_not_approx_number():
    assert approx_equal(True, 1.0) is False
    assert approx_equal(False, 0) is False
    assert approx_equal(True, True) is True
