def dodge_offsets(n_levels: int, width: float = 0.8) -> list[float]:
    step = width / (n_levels - 1)
    return [round(-width / 2 + i * step, 6) for i in range(n_levels)]
