import math

class ApproxScalar:
    def __init__(self, expected: float, rel: float = 1e-6, abs_tol: float = 1e-12, nan_ok: bool = False):
        self.expected = expected
        self.rel = rel
        self.abs_tol = abs_tol
        self.nan_ok = nan_ok

    def __eq__(self, actual: float) -> bool:
        if math.isnan(self.expected) or math.isnan(actual):
            return False
        tol = max(self.abs_tol, abs(self.expected) * self.rel)
        return abs(actual - self.expected) <= tol
