from sphinx_pycode.unparse import format_expr

def test_empty_and_multi_tuple():
    assert format_expr("()") == "()"
    assert format_expr("(1, 2)") == "(1, 2)"

def test_single_element_tuple_trailing_comma():
    assert format_expr("(1,)") == "(1,)"
    assert format_expr("(('a',),)") == "(('a',),)"
