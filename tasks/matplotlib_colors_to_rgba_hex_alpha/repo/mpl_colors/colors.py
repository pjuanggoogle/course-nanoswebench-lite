def hex_to_rgba(hex_str: str, alpha: float = None) -> tuple[float, float, float, float]:
    h = hex_str.lstrip("#")
    r = int(h[0:2], 16) / 255.0
    g = int(h[2:4], 16) / 255.0
    b = int(h[4:6], 16) / 255.0
    a = 1.0 if alpha is None else float(alpha)
    return (round(r, 4), round(g, 4), round(b, 4), round(a, 4))
