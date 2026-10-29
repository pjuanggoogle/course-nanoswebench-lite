def make_parametrize_ids(values: list, idfn=None) -> list[str]:
    ids = []
    for idx, val in enumerate(values):
        raw = idfn(val) if idfn is not None else str(val)
        ids.append(str(raw))
    return ids
