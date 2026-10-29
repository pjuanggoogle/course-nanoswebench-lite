from pylint_vars.unused import is_ignored_arg

def test_single_underscore_and_normal():
    assert is_ignored_arg("_") is True
    assert is_ignored_arg("count") is False

def test_underscore_and_dummy_prefixes():
    assert is_ignored_arg("_ctx") is True
    assert is_ignored_arg("dummy_req") is True
