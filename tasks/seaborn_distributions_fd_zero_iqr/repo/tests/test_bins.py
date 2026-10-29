from seaborn_dist.bins import freedman_diaconis_bins

def test_positive_iqr_bins():
    assert freedman_diaconis_bins([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]) == 2

def test_zero_iqr_falls_back_to_sturges():
    data = [0.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 10.0]
    assert freedman_diaconis_bins(data) == 4
