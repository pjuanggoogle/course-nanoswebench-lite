def approx_equal(actual, expected, tol: float = 1e-6) -> bool:
    if isinstance(actual, (int, float)) and isinstance(expected, (int, float)):
        return abs(actual - expected) <= tol
    return actual == expected
