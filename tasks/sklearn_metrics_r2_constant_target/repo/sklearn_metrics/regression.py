def r2_score(y_true: list[float], y_pred: list[float]) -> float:
    mean_y = sum(y_true) / len(y_true)
    ss_res = sum((t - p) ** 2 for t, p in zip(y_true, y_pred))
    ss_tot = sum((t - mean_y) ** 2 for t in y_true)
    return 1.0 - (ss_res / ss_tot)
