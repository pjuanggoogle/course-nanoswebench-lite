from urllib.parse import urlencode

def _fmt(val, normalize_bool: bool) -> str:
    return str(val)

def encode_query_params(data, normalize_bool: bool = False) -> str:
    if not data:
        return ""
    result = []
    items = data.items() if isinstance(data, dict) else data
    for k, v in items:
        if isinstance(v, (list, tuple)):
            for item in v:
                result.append((k, _fmt(item, normalize_bool)))
        else:
            result.append((k, _fmt(v, normalize_bool)))
    return urlencode(result)
