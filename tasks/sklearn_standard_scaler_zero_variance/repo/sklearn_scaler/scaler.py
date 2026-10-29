import math

class StandardScaler:
    def fit_transform(self, X: list[list[float]]) -> list[list[float]]:
        n = len(X)
        n_cols = len(X[0])
        means = [sum(row[j] for row in X) / n for j in range(n_cols)]
        stds = [
            math.sqrt(sum((row[j] - means[j]) ** 2 for row in X) / n)
            for j in range(n_cols)
        ]
        return [[(row[j] - means[j]) / stds[j] for j in range(n_cols)] for row in X]
