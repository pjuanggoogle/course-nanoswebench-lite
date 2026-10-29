import json

def load_prefixed_env(env: dict[str, str], prefix: str = "FLASK") -> dict:
    out = {}
    full_prefix = f"{prefix}_"
    for k, v in env.items():
        if not k.startswith(full_prefix):
            continue
        conf_key = k.replace(full_prefix, "")
        out[conf_key] = json.loads(v)
    return out
