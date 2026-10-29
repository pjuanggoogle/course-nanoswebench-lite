from seaborn_palettes.blend import blend_rgb

def test_three_color_blend():
    assert blend_rgb((0.0, 0.0, 0.0), (1.0, 1.0, 1.0), 3) == [
        (0.0, 0.0, 0.0), (0.5, 0.5, 0.5), (1.0, 1.0, 1.0)
    ]

def test_single_and_zero_color_blend():
    assert blend_rgb((0.2, 0.4, 0.6), (1.0, 1.0, 1.0), 1) == [(0.2, 0.4, 0.6)]
    assert blend_rgb((0.2, 0.4, 0.6), (1.0, 1.0, 1.0), 0) == []
