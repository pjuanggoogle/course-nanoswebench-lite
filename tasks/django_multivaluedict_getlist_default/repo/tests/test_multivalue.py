from django_datastructures.multivalue import MultiValueDict

def test_getlist_existing_and_empty():
    d = MultiValueDict({"a": [1, 2]})
    assert d.getlist("a") == [1, 2]
    assert d.getlist("missing") == []

def test_getlist_custom_default():
    d = MultiValueDict()
    assert d.getlist("missing", default=["fallback"]) == ["fallback"]
    assert d.getlist("missing", default=[]) == []
