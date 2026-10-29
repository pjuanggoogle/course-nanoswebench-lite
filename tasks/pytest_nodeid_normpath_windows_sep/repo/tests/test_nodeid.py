from pytest_nodes.nodeid import normalize_nodeid

def test_simple_windows_path():
    assert normalize_nodeid("tests\\unit\\test_core.py") == "tests/unit/test_core.py"

def test_preserves_backslash_in_parametrize_id():
    raw = "tests\\unit\\test_core.py::TestCls::test_regex[\\d+\\w+]"
    assert normalize_nodeid(raw) == "tests/unit/test_core.py::TestCls::test_regex[\\d+\\w+]"
