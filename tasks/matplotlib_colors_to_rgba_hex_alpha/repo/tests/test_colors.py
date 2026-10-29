from mpl_colors.colors import hex_to_rgba

def test_six_digit_hex():
    assert hex_to_rgba("#ff0000") == (1.0, 0.0, 0.0, 1.0)

def test_shorthand_and_eight_digit_alpha():
    assert hex_to_rgba("#f00") == (1.0, 0.0, 0.0, 1.0)
    assert hex_to_rgba("#00ff0080") == (0.0, 1.0, 0.0, round(128 / 255.0, 4))
    assert hex_to_rgba("#00ff0080", alpha=0.25) == (0.0, 1.0, 0.0, 0.25)
