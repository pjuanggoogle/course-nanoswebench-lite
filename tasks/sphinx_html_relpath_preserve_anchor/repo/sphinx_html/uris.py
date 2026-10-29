import os

def relative_uri(base_doc: str, target_uri: str) -> str:
    base_dir = os.path.dirname(base_doc) or "."
    return os.path.relpath(target_uri, base_dir)
