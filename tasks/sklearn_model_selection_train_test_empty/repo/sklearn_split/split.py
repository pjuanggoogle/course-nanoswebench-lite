import math

def split_sizes(n_samples: int, test_size: float = 0.25) -> tuple[int, int]:
    n_test = int(n_samples * test_size)
    n_train = n_samples - n_test
    return n_train, n_test
