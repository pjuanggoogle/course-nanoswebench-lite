import pytest
from patcher import apply_patch

def test_exact_line_hunk():
    orig = "line1\nline2\nline3\n"
    res = apply_patch(orig, 2, ["line2\n"], ["modified2\n"])
    assert res == "line1\nmodified2\nline3\n"

def test_offset_hunk_context_search():
    # Preamble inserted 2 new lines, shifting target from line 2 to line 4
    orig = "extra1\nextra2\nline1\nline2\nline3\n"
    res = apply_patch(orig, 2, ["line2\n"], ["modified2\n"])
    assert "modified2\n" in res
