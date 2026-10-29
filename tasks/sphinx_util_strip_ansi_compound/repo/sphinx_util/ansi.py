import re

ANSI_RE = re.compile(r"\x1b\[\d+m")

def strip_ansi_codes(text: str) -> str:
    return ANSI_RE.sub("", text)
