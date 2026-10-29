import pytest
from sklearn_encode.onehot import OneHotEncoder

def test_known_categories_and_error_mode():
    enc = OneHotEncoder(handle_unknown="error").fit(["b", "a"])
    assert enc.transform(["a", "b"]) == [[1, 0], [0, 1]]
    with pytest.raises(ValueError):
        enc.transform(["c"])

def test_handle_unknown_ignore():
    enc = OneHotEncoder(handle_unknown="ignore").fit(["b", "a"])
    assert enc.transform(["a", "unseen"]) == [[1, 0], [0, 0]]
