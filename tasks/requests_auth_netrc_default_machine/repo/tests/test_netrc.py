from requests_auth.netrc_auth import get_netrc_login

def test_exact_host_lookup():
    hosts = {"api.example.com": ("alice", "secret")}
    assert get_netrc_login("https://api.example.com/v1", hosts) == ("alice", "secret")

def test_host_with_port_and_default_fallback():
    hosts = {"api.example.com": ("alice", "secret"), "default": ("guest", " token")}
    assert get_netrc_login("https://api.example.com:8443/v1", hosts) == ("alice", "secret")
    assert get_netrc_login("https://other.example.org/v1", hosts) == ("guest", " token")
