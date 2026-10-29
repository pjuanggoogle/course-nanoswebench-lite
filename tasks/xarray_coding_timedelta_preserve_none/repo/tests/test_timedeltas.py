from xarray_coding.timedeltas import decode_timedeltas

def test_numeric_timedeltas():
    assert decode_timedeltas([1, 2], "h") == [3600, 7200]

def test_preserves_none_entries():
    assert decode_timedeltas([1, None, 3], "m") == [60, None, 180]
