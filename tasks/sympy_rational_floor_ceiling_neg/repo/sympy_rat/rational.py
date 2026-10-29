import math

class Rational:
    def __init__(self, p: int, q: int = 1):
        if q == 0:
            raise ZeroDivisionError("Denominator cannot be zero")
        g = math.gcd(p, q)
        self.p = p // g
        self.q = q // g

    def floor(self) -> int:
        return int(self.p / self.q)

    def ceiling(self) -> int:
        return int(self.p / self.q) + (1 if self.p % self.q != 0 else 0)
