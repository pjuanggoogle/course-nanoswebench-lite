from sphinx_intersphinx.inventory import resolve_uri

def test_explicit_uri_without_placeholder():
    assert (
        resolve_uri("https://docs.python.org/3/", "library/os.html#os.path", "os.path")
        == "https://docs.python.org/3/library/os.html#os.path"
    )

def test_dollar_placeholder_expansion():
    assert (
        resolve_uri("https://docs.python.org/3", "library/functions.html#$", "len")
        == "https://docs.python.org/3/library/functions.html#len"
    )
