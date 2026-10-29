import math

def log10_scale(values: list[float | None]) -> list[float | None]:
    return [math.log10(x) for x in values]
