import math

def validate_bounds(lower: float, upper: float) -> tuple[float, float]:
    if lower > upper:
        raise ValueError("lower bound cannot exceed upper bound")
    return (float(lower), float(upper))
