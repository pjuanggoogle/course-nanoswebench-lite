from flask_helpers.debug import get_debug_flag

def test_truthy_and_none():
    assert get_debug_flag("1") is True
    assert get_debug_flag("true") is True
    assert get_debug_flag(None) is False

def test_falsy_strings():
    assert get_debug_flag("0") is False
    assert get_debug_flag("false") is False
    assert get_debug_flag("False") is False
    assert get_debug_flag("no") is False
