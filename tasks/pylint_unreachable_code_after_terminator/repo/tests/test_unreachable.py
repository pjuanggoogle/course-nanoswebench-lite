from pylint_flow.unreachable import find_unreachable_lines

def test_unreachable_after_return():
    code = "def f():\n    return 1\n    x = 2\n"
    assert find_unreachable_lines(code) == [3]

def test_unreachable_after_break_and_continue():
    code = "def g():\n    for i in range(3):\n        break\n        y = 1\n"
    assert find_unreachable_lines(code) == [4]
