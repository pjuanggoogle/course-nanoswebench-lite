import pytest
from requests_lib.models import PreparedRequest

def test_prepare_url_simple():
    req = PreparedRequest()
    req.prepare_url("https://example.com/api", {"user": "alice", "page": "1"})
    assert "user=alice" in req.url
    assert "page=1" in req.url

def test_prepare_url_empty_params():
    req = PreparedRequest()
    req.prepare_url("https://example.com/api", {})
    assert req.url == "https://example.com/api"

def test_prepare_url_existing_query():
    req = PreparedRequest()
    req.prepare_url("https://example.com/api?debug=true", {"format": "json"})
    assert "debug=true" in req.url
    assert "format=json" in req.url

def test_prepare_url_list_params():
    req = PreparedRequest()
    req.prepare_url("https://example.com/api", {"filter": ["active", "verified"]})
    assert "filter=active&filter=verified" in req.url
    assert "%5B" not in req.url
