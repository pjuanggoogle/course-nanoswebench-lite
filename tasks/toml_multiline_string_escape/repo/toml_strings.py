def parse_multiline_basic_string(raw: str) -> str:
    content = raw[3:-3]
    # BUG: Does not strip leading newline when immediately following opening quotes
    # and does not handle line continuation backslash
    return content.replace('\\n', '\n').replace('\\t', '\t')
