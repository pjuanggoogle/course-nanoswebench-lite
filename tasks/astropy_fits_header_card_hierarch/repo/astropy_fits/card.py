def format_card(keyword: str, value) -> str:
    key = keyword.upper()[:8].ljust(8)
    return f"{key}= {value}"
