class OneHotEncoder:
    def __init__(self, handle_unknown: str = "error"):
        self.handle_unknown = handle_unknown
        self.categories_ = []

    def fit(self, values: list[str]):
        self.categories_ = sorted(set(values))
        return self

    def transform(self, values: list[str]) -> list[list[int]]:
        out = []
        for v in values:
            if v not in self.categories_:
                raise ValueError(f"Unknown category: {v}")
            out.append([1 if c == v else 0 for c in self.categories_])
        return out
