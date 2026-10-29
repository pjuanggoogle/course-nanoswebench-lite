from seaborn_utils.despine import despine

def test_basic_despine_no_trim():
    sp = {"top": {"visible": True, "bounds": None}, "left": {"visible": True, "bounds": None}}
    despine(sp, (0, 10), trim=False)
    assert sp["top"]["visible"] is False
    assert sp["left"]["bounds"] is None

def test_trim_only_visible_spines():
    sp = {"top": {"visible": True, "bounds": None}, "left": {"visible": True, "bounds": None}}
    despine(sp, (1, 9), trim=True)
    assert sp["left"]["bounds"] == (1, 9)
    assert sp["top"]["bounds"] is None
