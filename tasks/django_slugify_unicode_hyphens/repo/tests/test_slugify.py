from django_text.text import slugify

def test_basic_slugify():
    assert slugify("Hello, World!") == "hello-world"

def test_leading_trailing_underscores_and_spaces():
    assert slugify("  --- _Hello   World_ ---  ") == "hello-world"
    assert slugify("__init_file__") == "init_file"
