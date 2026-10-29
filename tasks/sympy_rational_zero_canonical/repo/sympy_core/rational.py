import math

def canonical_rational(p: int, q: int) -> tuple[int, int]:
    if q == 0:
        raise ZeroDivisionError("denominator cannot be zero")
    g = math.gcd(p, q)
    return (p // g, q // g)
