import pytest
from pytest_monkeypatch.env import delenv

def test_delenv_existing_and_raising():
    d = {"API_KEY": "123"}
    assert delenv(d, "API_KEY") == "123"
    with pytest.raises(KeyError):
        delenv(d, "API_KEY", raising=True)

def test_delenv_missing_not_raising():
    d = {}
    assert delenv(d, "MISSING", raising=False) is None
