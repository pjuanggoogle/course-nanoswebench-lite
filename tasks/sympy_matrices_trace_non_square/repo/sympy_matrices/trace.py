def matrix_trace(rows: list[list[float]]) -> float:
    if not rows:
        return 0
    return sum(rows[i][i] for i in range(len(rows)))
