from sympy_comb.permutations import permutation_parity

def test_identity_and_single_swap():
    assert permutation_parity([0, 1, 2]) == 0
    assert permutation_parity([1, 0, 2]) == 1

def test_three_cycle_is_even():
    assert permutation_parity([1, 2, 0]) == 0
    assert permutation_parity([2, 1, 0]) == 1
