from sphinx_domains.arglist import split_arglist

def test_simple_args():
    assert split_arglist("a, b, c") == ["a", "b", "c"]

def test_nested_brackets_and_parens():
    s = "x: tuple[int, str], y: list[int] = [1, 2], z = (3, 4)"
    assert split_arglist(s) == ["x: tuple[int, str]", "y: list[int] = [1, 2]", "z = (3, 4)"]
