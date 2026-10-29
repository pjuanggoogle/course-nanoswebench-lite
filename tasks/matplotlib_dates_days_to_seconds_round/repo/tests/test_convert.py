from mpl_dates.convert import days_to_seconds

def test_whole_and_half_days():
    assert days_to_seconds(1.0) == 86400
    assert days_to_seconds(0.5) == 43200

def test_one_hour_float_precision():
    assert days_to_seconds(29.0 / 86400.0) == 29
    assert days_to_seconds(58.0 / 86400.0) == 58
