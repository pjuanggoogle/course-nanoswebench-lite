import pytest
from sympy_matrices.trace import matrix_trace

def test_square_matrix_trace():
    assert matrix_trace([[1, 2], [3, 4]]) == 5

def test_non_square_raises_value_error():
    with pytest.raises(ValueError, match="square"):
        matrix_trace([[1, 2, 3], [4, 5, 6]])
