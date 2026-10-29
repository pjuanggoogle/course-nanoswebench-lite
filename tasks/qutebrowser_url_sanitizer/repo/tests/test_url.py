import pytest
from url_utils import sanitize_url

def test_simple_http_url():
    u = sanitize_url("http://example.com:8080/path?a=1")
    assert u["host"] == "example.com"
    assert u["port"] == 8080

def test_default_scheme_inference():
    u = sanitize_url("google.com/search")
    assert u["scheme"] == "http"
    assert u["host"] == "google.com"

def test_ipv6_bracketed_host_with_port():
    u = sanitize_url("http://[::1]:9000/api")
    assert u["host"] == "::1"
    assert u["port"] == 9000

def test_unescaped_percent_sign_in_query():
    u = sanitize_url("https://example.com/search?q=100%discount")
    assert u["query"] == "q=100%25discount"
