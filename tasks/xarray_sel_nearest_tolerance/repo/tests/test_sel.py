import pytest
from xarray_index.sel import sel_nearest

def test_nearest_without_tolerance():
    assert sel_nearest([10.0, 20.0, 30.0], 21.5) == 1

def test_nearest_with_tolerance_bound():
    assert sel_nearest([10.0, 20.0, 30.0], 20.4, tolerance=0.5) == 1
    with pytest.raises(KeyError):
        sel_nearest([10.0, 20.0, 30.0], 22.0, tolerance=0.5)
