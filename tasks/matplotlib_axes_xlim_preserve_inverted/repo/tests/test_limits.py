from mpl_axes.limits import normalize_xlim

def test_ascending_and_singular():
    assert normalize_xlim(0.0, 10.0) == (0.0, 10.0)
    assert normalize_xlim(0.0, 0.0) == (-0.5, 0.5)

def test_inverted_limits_preserved():
    assert normalize_xlim(10.0, 0.0) == (10.0, 0.0)
