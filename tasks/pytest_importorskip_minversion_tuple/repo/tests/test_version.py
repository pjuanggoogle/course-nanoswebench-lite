from pytest_outcomes.version import check_minversion

def test_single_digit_versions():
    assert check_minversion("1.3.0", "1.2.0") is True
    assert check_minversion("1.1.0", "1.2.0") is False

def test_multi_digit_minor_version():
    assert check_minversion("1.10.0", "1.2.0") is True
    assert check_minversion("2.0", "1.99.9") is True
