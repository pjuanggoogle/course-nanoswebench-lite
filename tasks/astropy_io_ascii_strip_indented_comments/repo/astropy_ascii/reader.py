def filter_data_lines(lines: list[str], comment: str = "#") -> list[str]:
    out = []
    for line in lines:
        if not line or line.startswith(comment):
            continue
        out.append(line.strip())
    return out
