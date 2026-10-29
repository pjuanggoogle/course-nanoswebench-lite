import math

def freedman_diaconis_bins(data: list[float]) -> int:
    s = sorted(data)
    n = len(s)
    q25 = s[n // 4]
    q75 = s[(3 * n) // 4]
    iqr = q75 - q25
    h = 2.0 * iqr / (n ** (1.0 / 3.0))
    return max(1, math.ceil((s[-1] - s[0]) / h))
