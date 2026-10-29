from xarray_fmt.truncate import maybe_truncate

def test_short_and_long():
    assert maybe_truncate("hello", maxlen=10) == "hello"
    assert maybe_truncate("hello world!", maxlen=10) == "hello w..."

def test_exact_maxlen_not_truncated():
    assert maybe_truncate("0123456789", maxlen=10) == "0123456789"
