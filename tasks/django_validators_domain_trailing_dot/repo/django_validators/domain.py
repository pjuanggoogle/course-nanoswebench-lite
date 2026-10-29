import re

LABEL_RE = re.compile(r"^(?!-)[A-Za-z0-9-]{1,63}(?<!-)$")

def is_valid_domain(value: str) -> bool:
    if not value or len(value) > 253:
        return False
    labels = value.split(".")
    if len(labels) < 2:
        return False
    return all(bool(LABEL_RE.match(label)) for label in labels)
