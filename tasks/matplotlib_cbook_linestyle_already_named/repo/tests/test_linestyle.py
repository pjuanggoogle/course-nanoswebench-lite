import pytest
from mpl_cbook.linestyle import resolve_linestyle

def test_short_codes():
    assert resolve_linestyle("--") == "dashed"
    with pytest.raises(ValueError):
        resolve_linestyle("invalid")

def test_full_names_accepted():
    assert resolve_linestyle("dashed") == "dashed"
    assert resolve_linestyle("solid") == "solid"
