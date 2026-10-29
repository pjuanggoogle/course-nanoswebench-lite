import pytest
from requests_transport.chunked import encode_chunked_request

def test_basic_chunked_encoding():
    chunks = [b"hello", b"world"]
    res = encode_chunked_request(chunks)
    assert res == b"5\r\nhello\r\n5\r\nworld\r\n0\r\n\r\n"

def test_empty_intermediate_chunks_filtered():
    chunks = [b"start", b"", b"end"]
    res = encode_chunked_request(chunks)
    assert res == b"5\r\nstart\r\n3\r\nend\r\n0\r\n\r\n"

def test_chunked_with_trailers():
    chunks = [b"data"]
    trailers = {"X-Checksum": "abc123", "Expires": "Wed"}
    res = encode_chunked_request(chunks, trailers=trailers)
    expected = b"4\r\ndata\r\n0\r\nX-Checksum: abc123\r\nExpires: Wed\r\n\r\n"
    assert res == expected
