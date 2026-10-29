import math
from xarray_nanops.nanreduce import nanmean

def test_partial_nan_mean():
    assert nanmean([1.0, float("nan"), 3.0]) == 2.0

def test_all_nan_returns_nan():
    res = nanmean([float("nan"), float("nan")])
    assert math.isnan(res)
