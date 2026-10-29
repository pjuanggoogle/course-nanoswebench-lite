import pytest
from sympy_series.taylor import eval_taylor

def test_linear_at_zero():
    assert eval_taylor([2.0, 3.0], 0.0, 4.0) == pytest.approx(14.0)

def test_higher_order_shifted_center():
    # f(x) = x^2 at x0 = 1 -> f(1)=1, f'(1)=2, f''(1)=2 -> at x=3, f(3)=9
    assert eval_taylor([1.0, 2.0, 2.0], 1.0, 3.0) == pytest.approx(9.0)
