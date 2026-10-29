def digitize_bins(values: list[float], edges: list[float], include_lowest: bool = False) -> list[int]:
    out = []
    for v in values:
        placed = -1
        for i in range(len(edges) - 1):
            if edges[i] < v <= edges[i + 1]:
                placed = i
                break
        out.append(placed)
    return out
