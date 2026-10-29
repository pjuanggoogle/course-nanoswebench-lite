import pytest
from chunked_decoder import decode_chunked_stream

def test_basic_chunks():
    stream = b"4\r\nWiki\r\n5\r\npedia\r\n0\r\n\r\n"
    assert decode_chunked_stream(stream) == b"Wikipedia"

def test_empty_payload():
    stream = b"0\r\n\r\n"
    assert decode_chunked_stream(stream) == b""

def test_chunk_with_semicolon_extensions():
    stream = b"4;name=quote\r\nWiki\r\n0\r\n\r\n"
    assert decode_chunked_stream(stream) == b"Wiki"

def test_trailing_headers_after_final_chunk():
    stream = b"3\r\nfoo\r\n0\r\nExpires: Wed, 21 Oct 2026 07:28:00 GMT\r\n\r\n"
    assert decode_chunked_stream(stream) == b"foo"
