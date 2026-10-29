def filter_stop_words(tokens: list[str], stop_words: set[str], lowercase: bool = True) -> list[str]:
    out = []
    for tok in tokens:
        w = tok.lower() if lowercase else tok
        if w not in stop_words:
            out.append(w)
    return out
