from mpl_colors.hex import to_hex

def test_rgb_only():
    assert to_hex((1.0, 0.0, 0.5)) == "#ff0080"
    assert to_hex((1.0, 0.0, 0.0, 0.5), keep_alpha=False) == "#ff0000"

def test_keep_alpha_channel():
    assert to_hex((1.0, 0.0, 0.0, 0.5), keep_alpha=True) == "#ff000080"
    assert to_hex((0.0, 1.0, 0.0), keep_alpha=True) == "#00ff00ff"
