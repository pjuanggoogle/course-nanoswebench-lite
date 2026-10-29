import pytest
from astropy_modeling.bbox import validate_bounds

def test_valid_and_inverted_bounds():
    assert validate_bounds(-1.0, 2.0) == (-1.0, 2.0)
    with pytest.raises(ValueError):
        validate_bounds(5.0, 1.0)

def test_nan_bounds_rejected():
    with pytest.raises(ValueError):
        validate_bounds(float("nan"), 1.0)
    with pytest.raises(ValueError):
        validate_bounds(0.0, float("nan"))
