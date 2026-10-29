from mpl_ticker.locator import linear_ticks

def test_standard_range():
    assert linear_ticks(0.0, 4.0, nbins=4) == [0.0, 1.0, 2.0, 3.0, 4.0]

def test_singular_and_inverted_range():
    assert linear_ticks(5.0, 5.0, nbins=2) == [4.0, 5.0, 6.0]
    assert linear_ticks(4.0, 0.0, nbins=4) == [0.0, 1.0, 2.0, 3.0, 4.0]
