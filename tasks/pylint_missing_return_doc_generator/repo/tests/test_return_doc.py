from pylint_doc.return_doc import needs_return_doc

def test_regular_functions():
    assert needs_return_doc("def f(x):\n    return x + 1\n") is True
    assert needs_return_doc("def g(x):\n    return\n") is False

def test_generator_with_early_bare_return():
    code = "def gen(items):\n    if not items:\n        return\n    yield items[0]\n"
    assert needs_return_doc(code) is True
