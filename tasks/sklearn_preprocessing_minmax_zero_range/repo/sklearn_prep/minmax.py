def minmax_scale(values: list[float]) -> list[float]:
    if not values:
        return []
    vmin, vmax = min(values), max(values)
    span = vmax - vmin
    return [(x - vmin) / span for x in values]
