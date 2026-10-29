def poly_degree(coeffs: list[float]) -> int:
    if not coeffs:
        return -1
    return len(coeffs) - 1
