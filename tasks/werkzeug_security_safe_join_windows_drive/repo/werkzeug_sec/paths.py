import posixpath

def safe_join(base: str, *paths: str) -> str | None:
    for p in paths:
        if p.startswith("/") or ".." in p.split("/"):
            return None
    return posixpath.join(base, *paths)
