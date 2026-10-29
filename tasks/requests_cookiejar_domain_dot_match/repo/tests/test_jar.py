from requests_cookies.jar import CookieJar

def test_exact_subdomain_match():
    jar = CookieJar()
    jar.set_cookie("sid", "123", ".example.com")
    assert jar.get_for_host("api.example.com") == {"sid": "123"}

def test_root_domain_and_suffix_boundary():
    jar = CookieJar()
    jar.set_cookie("sid", "123", ".example.com")
    jar.set_cookie("theme", "dark", "example.com")
    assert jar.get_for_host("example.com") == {"sid": "123", "theme": "dark"}
    assert jar.get_for_host("badexample.com") == {}
