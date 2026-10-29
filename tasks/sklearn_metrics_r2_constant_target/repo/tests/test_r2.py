from sklearn_metrics.regression import r2_score

def test_standard_r2():
    assert r2_score([1.0, 2.0, 3.0], [1.0, 2.0, 3.0]) == 1.0

def test_constant_y_true():
    assert r2_score([2.0, 2.0, 2.0], [2.0, 2.0, 2.0]) == 1.0
    assert r2_score([2.0, 2.0, 2.0], [1.0, 2.0, 3.0]) == 0.0
