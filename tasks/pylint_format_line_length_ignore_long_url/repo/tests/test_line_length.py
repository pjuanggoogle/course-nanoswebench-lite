from pylint_format.line_length import is_line_too_long

def test_short_and_long_code_lines():
    assert is_line_too_long("x = 1", max_len=20) is False
    assert is_line_too_long("x = " + "a" * 30, max_len=20) is True

def test_long_url_comment_exempt():
    url_line = "    # https://example.com/very/long/documentation/path/that/exceeds/limit"
    assert is_line_too_long(url_line, max_len=40) is False
