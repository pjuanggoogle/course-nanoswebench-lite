import math

def eval_taylor(derivs: list[float], x0: float, x: float) -> float:
    total = 0.0
    for k, d in enumerate(derivs):
        total += d * (x ** k)
    return total
