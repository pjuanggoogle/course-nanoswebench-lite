from pytest_param.ids import make_parametrize_ids

def test_unique_ids():
    assert make_parametrize_ids([1, 2, 3]) == ["1", "2", "3"]

def test_duplicate_ids_disambiguated():
    assert make_parametrize_ids(["x", "y", "x", "x"]) == ["x", "y", "x_2", "x_3"]
