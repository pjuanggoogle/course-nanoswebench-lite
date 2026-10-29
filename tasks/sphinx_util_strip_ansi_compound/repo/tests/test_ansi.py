from sphinx_util.ansi import strip_ansi_codes

def test_single_code():
    assert strip_ansi_codes("\x1b[32mok\x1b[0m") == "ok"

def test_compound_and_empty_reset():
    assert strip_ansi_codes("\x1b[31;1mERROR\x1b[m") == "ERROR"
