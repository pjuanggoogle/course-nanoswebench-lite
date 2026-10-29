from django_http.cookies import parse_cookie

def test_basic_cookies():
    assert parse_cookie("sessionid=abc; theme=dark") == {"sessionid": "abc", "theme": "dark"}

def test_ignore_empty_key_segments():
    assert parse_cookie("=nameless; valid=1; ; =other") == {"valid": "1"}
