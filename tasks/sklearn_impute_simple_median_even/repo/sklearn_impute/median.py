def impute_median(values: list[float | None]) -> list[float]:
    valid = sorted(x for x in values if x is not None)
    n = len(valid)
    med = float(valid[n // 2])
    return [med if x is None else float(x) for x in values]
