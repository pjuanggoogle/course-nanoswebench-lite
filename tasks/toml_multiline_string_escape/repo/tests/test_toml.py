import pytest
from toml_strings import parse_multiline_basic_string

def test_simple_multiline():
    raw = '"""hello\nworld"""'
    assert parse_multiline_basic_string(raw) == "hello\nworld"

def test_multiline_immediate_leading_newline_trim():
    raw = '"""\nThe quick brown fox"""'
    assert parse_multiline_basic_string(raw) == "The quick brown fox"

def test_multiline_escaped_line_continuation():
    raw = '"""\nThe quick \\   \n    brown fox"""'
    assert parse_multiline_basic_string(raw) == "The quick brown fox"
