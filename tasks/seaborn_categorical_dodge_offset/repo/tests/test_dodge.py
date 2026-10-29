from seaborn_cat.dodge import dodge_offsets

def test_zero_width_offsets():
    assert dodge_offsets(3, width=0.0) == [0.0, 0.0, 0.0]

def test_single_and_multiple_hue_levels():
    assert dodge_offsets(1, width=0.8) == [0.0]
    assert dodge_offsets(2, width=0.8) == [-0.2, 0.2]
    assert dodge_offsets(4, width=0.8) == [-0.3, -0.1, 0.1, 0.3]
