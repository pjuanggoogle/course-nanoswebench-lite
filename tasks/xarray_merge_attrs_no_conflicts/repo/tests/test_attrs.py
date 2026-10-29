import pytest
from xarray_merge.attrs import merge_attrs

def test_compatible_attrs():
    assert merge_attrs([{"units": "m"}, {"units": "m", "long_name": "height"}]) == {
        "units": "m",
        "long_name": "height",
    }

def test_conflicting_attrs_raises():
    with pytest.raises(ValueError, match="Conflicting"):
        merge_attrs([{"units": "m"}, {"units": "km"}])
