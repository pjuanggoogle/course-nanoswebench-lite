from astropy_table.join import inner_join

def test_basic_inner_join():
    l = [{"id": 1, "a": "x"}]
    r = [{"id": 1, "b": "y"}]
    assert inner_join(l, r, "id") == [{"id": 1, "a": "x", "b": "y"}]

def test_masked_none_keys_do_not_match():
    l = [{"id": 1, "a": "x"}, {"id": None, "a": "m1"}]
    r = [{"id": 1, "b": "y"}, {"id": None, "b": "m2"}]
    assert inner_join(l, r, "id") == [{"id": 1, "a": "x", "b": "y"}]
