import urllib.parse

def sanitize_url(raw: str) -> dict:
    # BUG: Does not prepend default 'http://' scheme before urlsplit or escape stray '%' as '%25'
    parsed = urllib.parse.urlsplit(raw)
    scheme = parsed.scheme or "http"
    netloc = parsed.netloc
    path = urllib.parse.unquote(parsed.path)
    return {
        "scheme": scheme,
        "host": parsed.hostname,
        "port": parsed.port,
        "path": path,
        "query": parsed.query
    }
