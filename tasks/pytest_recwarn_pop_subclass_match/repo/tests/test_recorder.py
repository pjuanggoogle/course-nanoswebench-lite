from pytest_warnings.recorder import pop_warning

def test_exact_warning_class():
    items = [UserWarning("u")]
    w = pop_warning(items, UserWarning)
    assert str(w) == "u"

def test_subclass_warning_match():
    items = [DeprecationWarning("deprecated api")]
    w = pop_warning(items, Warning)
    assert isinstance(w, DeprecationWarning)
