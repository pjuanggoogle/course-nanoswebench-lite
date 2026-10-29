from pytest_nodes.nodeid import normalize_nodeid

def test_simple_windows_path():
    assert normalize_nodeid("tests\\unit\\test_app.py") == "tests/unit/test_app.py"

def test_preserves_backslashes_in_parametrize_id():
    raw = "tests\\test_str.py::test_escape[line1\\nline2]"
    assert normalize_nodeid(raw) == "tests/test_str.py::test_escape[line1\\nline2]"
