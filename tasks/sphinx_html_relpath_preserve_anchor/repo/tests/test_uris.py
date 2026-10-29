from sphinx_html.uris import relative_uri

def test_cross_directory():
    assert relative_uri("guide/intro.html", "api/index.html") == "../api/index.html"

def test_same_doc_with_anchor():
    assert relative_uri("guide/intro.html", "guide/intro.html#install") == "#install"
    assert relative_uri("guide/intro.html", "api/index.html#top") == "../api/index.html#top"
