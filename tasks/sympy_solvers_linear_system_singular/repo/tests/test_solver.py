import pytest
from sympy_linsolve.solver import solve_2x2

def test_unique_and_inconsistent():
    assert solve_2x2(1, 1, 3, 1, -1, 1) == (2.0, 1.0)
    assert solve_2x2(1, 2, 3, 2, 4, 7) is None

def test_dependent_infinite_solutions():
    with pytest.raises(ValueError, match="Infinite solutions"):
        solve_2x2(1, 2, 3, 2, 4, 6)
