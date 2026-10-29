from sklearn_split.kfold import kfold_indices

def test_even_division():
    assert kfold_indices(6, 3) == [[0, 1], [2, 3], [4, 5]]

def test_uneven_remainder_distributed_across_first_folds():
    assert kfold_indices(10, 3) == [[0, 1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert kfold_indices(5, 3) == [[0, 1], [2, 3], [4]]
