def parse_cookie(cookie: str) -> dict:
    if not cookie:
        return {}
    cookiedict = {}
    for chunk in cookie.split(";"):
        if "=" in chunk:
            key, val = chunk.split("=", 1)
        else:
            key, val = "", chunk
        key, val = key.strip(), val.strip()
        cookiedict[key] = val
    return cookiedict
