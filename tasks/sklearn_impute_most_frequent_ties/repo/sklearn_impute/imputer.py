from collections import Counter

def most_frequent_impute(values: list) -> list:
    counts = Counter(values)
    fill_val = counts.most_common(1)[0][0]
    return [fill_val if v is None else v for v in values]
