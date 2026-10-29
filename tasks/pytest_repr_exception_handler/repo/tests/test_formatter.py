import pytest
from failure_formatter import format_failure

class CrashingRepr:
    def __repr__(self):
        raise RuntimeError("Cannot serialize dynamic state")

def test_format_normal_object():
    assert format_failure(ValueError("bad"), [1, 2]) == "FAIL: ValueError: bad | target=[1, 2]"

def test_format_exception_message():
    assert "FAIL: KeyError: 'missing'" in format_failure(KeyError("missing"), "item")

def test_safely_catch_crashing_repr():
    res = format_failure(TypeError("invalid"), CrashingRepr())
    assert "unhandled exception in __repr__" in res
    assert "RuntimeError" in res

def test_include_exception_type_in_fallback_repr():
    class CustomErr(Exception): pass
    class ExplodingRepr:
        def __repr__(self): raise CustomErr("boom")
    res = format_failure(Exception("test"), ExplodingRepr())
    assert "CustomErr: boom" in res
