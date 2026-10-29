import pytest
from sklearn_scaler.scaler import StandardScaler

def test_normal_scaling():
    X = [[0.0], [2.0]]
    assert StandardScaler().fit_transform(X) == [[-1.0], [1.0]]

def test_constant_feature_column():
    X = [[1.0, 5.0], [3.0, 5.0]]
    assert StandardScaler().fit_transform(X) == [[-1.0, 0.0], [1.0, 0.0]]
