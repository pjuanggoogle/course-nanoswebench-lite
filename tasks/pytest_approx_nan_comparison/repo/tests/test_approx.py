from pytest_approx.approx import ApproxScalar

def test_finite_approx():
    assert 1.0000001 == ApproxScalar(1.0)
    assert float("nan") != ApproxScalar(float("nan"), nan_ok=False)

def test_nan_ok_and_infinities():
    assert float("nan") == ApproxScalar(float("nan"), nan_ok=True)
    assert float("inf") == ApproxScalar(float("inf"))
    assert float("-inf") != ApproxScalar(float("inf"))
