def resolve_uri(base_uri: str, uri_template: str, obj_name: str) -> str:
    base = base_uri.rstrip("/")
    rel = uri_template.lstrip("/")
    return f"{base}/{rel}"
