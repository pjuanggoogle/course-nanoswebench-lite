from sklearn_prep.minmax import minmax_scale

def test_varying_values():
    assert minmax_scale([10.0, 20.0, 30.0]) == [0.0, 0.5, 1.0]

def test_constant_values():
    assert minmax_scale([5.0, 5.0, 5.0]) == [0.0, 0.0, 0.0]
