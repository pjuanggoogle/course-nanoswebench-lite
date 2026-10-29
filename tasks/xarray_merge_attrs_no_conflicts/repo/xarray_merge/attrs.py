def merge_attrs(attrs_list: list[dict]) -> dict:
    merged = {}
    for d in attrs_list:
        for k, v in d.items():
            merged[k] = v
    return merged
