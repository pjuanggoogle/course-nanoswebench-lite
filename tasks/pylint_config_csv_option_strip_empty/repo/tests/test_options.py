from pylint_config.options import parse_csv_option

def test_standard_csv():
    assert parse_csv_option("C0114, C0115") == ["C0114", "C0115"]

def test_empty_and_trailing_comma():
    assert parse_csv_option("") == []
    assert parse_csv_option("   ") == []
    assert parse_csv_option("C0114, , C0115,") == ["C0114", "C0115"]
