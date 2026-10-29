from django_html.escape import SafeString, conditional_escape

def test_escapes_plain_string():
    assert conditional_escape("<b>hi</b>") == "&lt;b&gt;hi&lt;/b&gt;"

def test_preserves_safe_string():
    s = SafeString("<b>safe</b>")
    assert conditional_escape(s) == "<b>safe</b>"
