from xarray_bins.groupby import digitize_bins

def test_strict_right_closed_bins():
    assert digitize_bins([0.0, 5.0, 10.0], [0.0, 5.0, 10.0], include_lowest=False) == [-1, 0, 1]

def test_include_lowest_left_edge():
    assert digitize_bins([0.0, 5.0, 10.0], [0.0, 5.0, 10.0], include_lowest=True) == [0, 0, 1]
