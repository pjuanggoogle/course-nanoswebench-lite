from requests_netrc.auth import get_netrc_login

def test_host_without_port():
    hosts = {"example.com": ("alice", "secret")}
    assert get_netrc_login("http://example.com/data", hosts) == ("alice", "secret")

def test_host_with_port():
    hosts = {"example.com": ("alice", "secret")}
    assert get_netrc_login("http://example.com:8080/data", hosts) == ("alice", "secret")
