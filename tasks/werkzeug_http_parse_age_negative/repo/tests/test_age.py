from werkzeug_http.age import parse_age

def test_valid_and_invalid_age():
    assert parse_age("120") == 120
    assert parse_age("abc") is None

def test_negative_and_none_age():
    assert parse_age("-10") is None
    assert parse_age(None) is None
    assert parse_age("0") == 0
