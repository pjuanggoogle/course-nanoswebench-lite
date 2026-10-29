def merge_coords(left: dict, right: dict, compat: str = "no_conflicts") -> dict:
    out = dict(left)
    for k, v in right.items():
        out[k] = v
    return out
