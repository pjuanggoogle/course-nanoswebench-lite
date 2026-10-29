import pytest
from xarray_merge.coords import merge_coords

def test_disjoint_and_identical_merge():
    assert merge_coords({"x": 1}, {"y": 2}) == {"x": 1, "y": 2}
    assert merge_coords({"x": 1}, {"x": 1}) == {"x": 1}

def test_conflict_and_override_modes():
    with pytest.raises(ValueError, match="Conflict in coord"):
        merge_coords({"x": 1}, {"x": 2}, compat="no_conflicts")
    assert merge_coords({"x": 1}, {"x": 2}, compat="override") == {"x": 1}
