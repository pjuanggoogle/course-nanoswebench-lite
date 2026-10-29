def split_arglist(arglist: str) -> list[str]:
    if not arglist.strip():
        return []
    return [p.strip() for p in arglist.split(",")]
