import json

def load_prefixed_env(env: dict, prefix: str = "FLASK") -> dict:
    full_prefix = f"{prefix}_"
    out = {}
    for k, v in env.items():
        if k.startswith(full_prefix):
            key = k[len(full_prefix):]
            out[key] = v
    return out
