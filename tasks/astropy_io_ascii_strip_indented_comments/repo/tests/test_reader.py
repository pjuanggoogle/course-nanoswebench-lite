from astropy_ascii.reader import filter_data_lines

def test_unindented_comments():
    assert filter_data_lines(["# col1 col2", "1 2", "3 4"]) == ["1 2", "3 4"]

def test_indented_comments_and_blank_lines():
    assert filter_data_lines(["   # indented", "   ", "10 20"]) == ["10 20"]
