from datetime import datetime
from astropy_time.iso import parse_iso_utc

def test_standard_iso_timestamp():
    assert parse_iso_utc("2020-01-01T12:30:45") == datetime(2020, 1, 1, 12, 30, 45)

def test_leap_second_rollover():
    assert parse_iso_utc("2016-12-31T23:59:60") == datetime(2017, 1, 1, 0, 0, 0)
