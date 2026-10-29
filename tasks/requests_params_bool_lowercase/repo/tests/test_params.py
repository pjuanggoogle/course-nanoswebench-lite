from requests_params.models import encode_query_params

def test_basic_string_and_int_params():
    qs = encode_query_params({"q": "test", "one": 1, "zero": 0}, normalize_bool=True)
    assert "q=test" in qs
    assert "one=1" in qs
    assert "zero=0" in qs

def test_bool_param_serialization():
    qs = encode_query_params({"active": True, "flags": [False, True]}, normalize_bool=True)
    assert qs == "active=true&flags=false&flags=true"
