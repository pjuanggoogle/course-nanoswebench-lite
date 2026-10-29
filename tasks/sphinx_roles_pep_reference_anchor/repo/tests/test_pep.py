from sphinx_roles.pep import make_pep_url

def test_plain_pep():
    assert make_pep_url("8") == "https://peps.python.org/pep-0008/"
    assert make_pep_url("484") == "https://peps.python.org/pep-0484/"

def test_pep_with_anchor():
    assert make_pep_url("8#constants") == "https://peps.python.org/pep-0008/#constants"
