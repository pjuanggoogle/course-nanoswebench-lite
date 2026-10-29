def format_byte_range(start: int, end: int | None = None) -> str:
    if end is None:
        return f"bytes={start}-"
    return f"bytes={start}-{end - 1}"
