from sklearn_impute.median import impute_median

def test_odd_count_median():
    assert impute_median([1.0, None, 3.0, 9.0]) == [1.0, 3.0, 3.0, 9.0]

def test_even_count_median():
    assert impute_median([1.0, 2.0, None, 4.0, 10.0]) == [1.0, 2.0, 3.0, 4.0, 10.0]
