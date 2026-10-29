from pylint_defaults.checker import find_dangerous_defaults

def test_literal_mutable_defaults():
    code = "def a(x=[]): pass\ndef b(x=()): pass\n"
    assert find_dangerous_defaults(code) == ["a"]

def test_builtin_call_mutable_defaults():
    code = "def c(x=dict()): pass\ndef d(y=set()): pass\ndef e(z=tuple()): pass\n"
    assert find_dangerous_defaults(code) == ["c", "d"]
