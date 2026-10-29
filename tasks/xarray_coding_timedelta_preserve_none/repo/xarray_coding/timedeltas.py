SCALE = {"s": 1, "m": 60, "h": 3600, "D": 86400}

def decode_timedeltas(values: list[int | None], unit: str) -> list[int | None]:
    factor = SCALE[unit]
    return [x * factor for x in values]
