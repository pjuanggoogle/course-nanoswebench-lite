def maybe_truncate(text: str, maxlen: int = 20) -> str:
    if len(text) >= maxlen:
        return text[: maxlen - 3] + "..."
    return text
