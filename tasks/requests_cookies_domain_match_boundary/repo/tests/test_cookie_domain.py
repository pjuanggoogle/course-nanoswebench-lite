from requests_cookies.domain import cookie_domain_matches

def test_exact_and_subdomain_match():
    assert cookie_domain_matches("example.com", "example.com") is True
    assert cookie_domain_matches("sub.example.com", ".example.com") is True

def test_rejects_partial_host_suffix():
    assert cookie_domain_matches("badexample.com", "example.com") is False
