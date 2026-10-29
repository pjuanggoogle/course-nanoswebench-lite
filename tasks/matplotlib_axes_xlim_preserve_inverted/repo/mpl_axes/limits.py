def normalize_xlim(left: float, right: float) -> tuple[float, float]:
    if left == right:
        delta = 0.5 if left == 0 else 0.05 * abs(left)
        return (left - delta, right + delta)
    return (min(left, right), max(left, right))
