def get_debug_flag(val: str | None) -> bool:
    if not val:
        return False
    return bool(val)
