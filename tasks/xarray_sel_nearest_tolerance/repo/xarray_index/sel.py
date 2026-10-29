def sel_nearest(coords: list[float], target: float, tolerance: float = None) -> int:
    best_idx = min(range(len(coords)), key=lambda i: abs(coords[i] - target))
    return best_idx
