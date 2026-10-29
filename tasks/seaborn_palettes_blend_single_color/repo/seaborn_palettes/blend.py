def blend_rgb(c1: tuple[float, float, float], c2: tuple[float, float, float], n_colors: int) -> list[tuple[float, float, float]]:
    out = []
    for i in range(n_colors):
        t = i / (n_colors - 1)
        out.append(tuple(round(c1[j] + t * (c2[j] - c1[j]), 4) for j in range(3)))
    return out
