from pylint_typecheck.callable_check import is_callable_instance

def test_direct_call_method():
    assert is_callable_instance({"__call__"}, []) is True
    assert is_callable_instance({"run"}, []) is False

def test_inherited_call_method():
    assert is_callable_instance({"helper"}, [{"__init__"}, {"__call__"}]) is True
