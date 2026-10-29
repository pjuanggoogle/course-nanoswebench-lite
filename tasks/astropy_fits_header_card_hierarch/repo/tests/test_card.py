from astropy_fits.card import format_card

def test_short_standard_keyword():
    assert format_card("EXPTIME", 120) == "EXPTIME = 120"

def test_long_or_spaced_hierarch_keyword():
    assert format_card("ESO DET CHIP1 ID", 4) == "HIERARCH ESO DET CHIP1 ID = 4"
    assert format_card("LONGKEYWORD", 99) == "HIERARCH LONGKEYWORD = 99"
