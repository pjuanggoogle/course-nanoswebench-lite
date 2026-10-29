import pytest
from sklearn_split.split import split_sizes

def test_even_multiple():
    assert split_sizes(8, 0.25) == (6, 2)

def test_ceil_small_sample_and_bounds():
    assert split_sizes(3, 0.25) == (2, 1)
    with pytest.raises(ValueError):
        split_sizes(10, 1.0)
