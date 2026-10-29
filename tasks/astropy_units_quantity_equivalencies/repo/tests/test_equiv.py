from astropy_units.equiv import convert_with_equivalencies

EQUIVS = [("nm", "Hz", lambda x: 3e17 / x, lambda y: 3e17 / y)]

def test_forward_equivalency():
    assert convert_with_equivalencies(500.0, "nm", "Hz", EQUIVS) == 6e14

def test_reverse_equivalency():
    assert convert_with_equivalencies(6e14, "Hz", "nm", EQUIVS) == 500.0
