from pylint_vars.unused import find_unused_variables

def test_reports_normal_unused():
    code = "def f():\n    x = 1\n    y = 2\n    return x\n"
    assert find_unused_variables(code) == ["y"]

def test_ignores_underscore_prefixed_variables():
    code = "def f(pairs):\n    for k, _val in pairs:\n        _ = k\n        unused = 10\n"
    assert find_unused_variables(code) == ["unused"]
