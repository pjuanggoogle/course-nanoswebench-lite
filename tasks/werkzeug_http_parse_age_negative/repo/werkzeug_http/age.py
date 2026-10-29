def parse_age(value: str | None) -> int | None:
    try:
        return int(value)
    except ValueError:
        return None
