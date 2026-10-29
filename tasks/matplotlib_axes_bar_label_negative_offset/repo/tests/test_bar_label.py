from mpl_bars.bar_label import bar_label_positions

def test_positive_bars():
    assert bar_label_positions([10.0, 0.0], padding=2.0) == [12.0, 2.0]

def test_negative_bars_padded_outward():
    assert bar_label_positions([10.0, -5.0, -1.0], padding=2.0) == [12.0, -7.0, -3.0]
