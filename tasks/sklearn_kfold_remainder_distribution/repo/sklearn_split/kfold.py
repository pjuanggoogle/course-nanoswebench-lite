def kfold_indices(n_samples: int, n_splits: int) -> list[list[int]]:
    base = n_samples // n_splits
    folds = []
    curr = 0
    for i in range(n_splits):
        end = n_samples if i == n_splits - 1 else curr + base
        folds.append(list(range(curr, end)))
        curr = end
    return folds
