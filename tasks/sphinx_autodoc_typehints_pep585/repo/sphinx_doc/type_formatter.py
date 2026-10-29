import types
from typing import get_origin, get_args, Union

def format_annotation(annotation) -> str:
    # BUG: Naive __name__ access fails on PEP 604 (int | str) and GenericAliases
    if annotation is None or annotation is type(None):
        return "None"
    if hasattr(annotation, "__name__"):
        return annotation.__name__
    return str(annotation)
