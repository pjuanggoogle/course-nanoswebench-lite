from sklearn_text.stopwords import filter_stop_words

def test_lowercase_stopwords():
    assert filter_stop_words(["The", "cat"], {"the"}) == ["cat"]

def test_mixed_case_stopwords_set():
    assert filter_stop_words(["the", "Quick", "Fox"], {"The", "AND"}, lowercase=True) == ["quick", "fox"]
