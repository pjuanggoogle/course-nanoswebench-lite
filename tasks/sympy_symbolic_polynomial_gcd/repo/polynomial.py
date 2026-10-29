def poly_gcd(p1: list[float], p2: list[float]) -> list[float]:
    """Compute monic polynomial GCD using Euclidean algorithm."""
    def degree(p):
        for i in range(len(p) - 1, -1, -1):
            if abs(p[i]) > 0: # BUG: exact zero check fails on float precision drift
                return i
        return -1

    def poly_div(num, den):
        deg_num, deg_den = degree(num), degree(den)
        if deg_den < 0: raise ZeroDivisionError()
        quot = [0.0] * max(0, deg_num - deg_den + 1)
        rem = list(num)
        while degree(rem) >= deg_den:
            d_rem = degree(rem)
            lead = rem[d_rem] / den[deg_den]
            diff = d_rem - deg_den
            quot[diff] += lead
            for i in range(deg_den + 1):
                rem[i + diff] -= lead * den[i]
        return quot, rem

    a, b = list(p1), list(p2)
    while degree(b) >= 0:
        _, rem = poly_div(a, b)
        a, b = b, rem

    deg_a = degree(a)
    if deg_a < 0: return [0.0]
    lead = a[deg_a]
    return [round(c / lead, 4) for c in a[:deg_a + 1]]
