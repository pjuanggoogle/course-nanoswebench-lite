def despine(spines: dict[str, dict], data_bounds: tuple[float, float], trim: bool = False, hide: tuple = ("top", "right")):
    for name in hide:
        if name in spines:
            spines[name]["visible"] = False
    if trim:
        for name, sp in spines.items():
            sp["bounds"] = data_bounds
    return spines
