from sklearn_impute.imputer import most_frequent_impute

def test_clear_winner():
    assert most_frequent_impute([1, 2, 2, None]) == [1, 2, 2, 2]

def test_tie_breaking_and_majority_none():
    assert most_frequent_impute([None, None, None, 5, 2, 5, 2]) == [2, 2, 2, 5, 2, 5, 2]
