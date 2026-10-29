import inspect
import pytest
from sphinx_mock.mock import MockObject

def test_normal_attribute_mocked():
    m = MockObject()
    assert isinstance(m.submodule.func, MockObject)

def test_dunder_raises_attribute_error_and_unwrap_works():
    m = MockObject()
    with pytest.raises(AttributeError):
        _ = m.__wrapped__
    assert inspect.unwrap(m) is m
