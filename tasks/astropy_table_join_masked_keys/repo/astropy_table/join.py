def inner_join(left_rows: list[dict], right_rows: list[dict], key: str) -> list[dict]:
    joined = []
    for lrow in left_rows:
        for rrow in right_rows:
            if lrow.get(key) == rrow.get(key):
                joined.append({**lrow, **rrow})
    return joined
