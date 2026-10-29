import pytest
from sphinx_doc.type_formatter import format_annotation

def test_primitive_types():
    assert format_annotation(int) == "int"
    assert format_annotation(str) == "str"
    assert format_annotation(None) == "None"

def test_pep604_union():
    ann = int | str
    assert format_annotation(ann) == "int | str"

def test_nested_pep585_generics():
    ann = list[str | None]
    assert format_annotation(ann) == "list[str | None]"

def test_dict_generic():
    ann = dict[str, list[int]]
    assert format_annotation(ann) == "dict[str, list[int]]"
