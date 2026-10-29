from requests_auth.basic import basic_auth_header

def test_ascii_credentials():
    assert basic_auth_header("user", "pass") == "Basic dXNlcjpwYXNz"

def test_latin1_credentials():
    assert basic_auth_header("user", "päss") == "Basic dXNlcjpw5HNz"
