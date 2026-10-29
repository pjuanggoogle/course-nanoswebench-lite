from django_encoding.uri import iri_to_uri

def test_simple_path():
    assert iri_to_uri("/path/to/page") == "/path/to/page"

def test_unicode_iri_with_query_and_scheme():
    assert iri_to_uri("https://example.com/café?a=1&b=2") == "https://example.com/caf%C3%A9?a=1&b=2"
