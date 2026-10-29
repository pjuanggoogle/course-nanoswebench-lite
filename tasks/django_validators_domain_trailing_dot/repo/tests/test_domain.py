from django_validators.domain import is_valid_domain

def test_standard_domains():
    assert is_valid_domain("example.com") is True
    assert is_valid_domain("-bad.com") is False

def test_fqdn_single_trailing_dot():
    assert is_valid_domain("example.com.") is True
    assert is_valid_domain("example.com..") is False
