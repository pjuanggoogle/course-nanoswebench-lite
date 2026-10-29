from sympy_ntheory.primality import is_prime

def test_odd_primes_and_composites():
    assert is_prime(3) is True
    assert is_prime(9) is False
    assert is_prime(17) is True

def test_boundary_one_and_two():
    assert is_prime(1) is False
    assert is_prime(2) is True
    assert is_prime(-5) is False
