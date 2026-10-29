from werkzeug_range.byterange import format_byte_range

def test_standard_ranges():
    assert format_byte_range(0, 500) == "bytes=0-499"
    assert format_byte_range(500, None) == "bytes=500-"

def test_suffix_byte_range():
    assert format_byte_range(-500, None) == "bytes=-500"
