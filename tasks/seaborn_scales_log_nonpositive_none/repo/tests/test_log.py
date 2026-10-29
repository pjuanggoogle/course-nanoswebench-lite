from seaborn_scales.log import log10_scale

def test_positive_values():
    assert log10_scale([1.0, 10.0, 100.0]) == [0.0, 1.0, 2.0]

def test_nonpositive_and_none_mapped_to_none():
    assert log10_scale([10.0, 0.0, -5.0, None]) == [1.0, None, None, None]
