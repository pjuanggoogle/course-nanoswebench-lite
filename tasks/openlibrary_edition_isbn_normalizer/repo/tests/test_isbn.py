import pytest
from isbn import normalize_isbn

def test_valid_isbn13_unchanged():
    assert normalize_isbn("978-0-306-40615-7") == "9780306406157"

def test_strip_hyphens_and_spaces():
    assert normalize_isbn(" 978 0 306 40615 7 ") == "9780306406157"

def test_isbn10_with_x_checksum():
    # 0-8044-2957-X -> valid ISBN-10
    assert normalize_isbn("0-8044-2957-X") == "9780804429573"

def test_isbn13_checksum_zero_remainder():
    # 0-306-40615-2 converts to 978-0-306-40615-7
    assert normalize_isbn("0-306-40615-2") == "9780306406157"
