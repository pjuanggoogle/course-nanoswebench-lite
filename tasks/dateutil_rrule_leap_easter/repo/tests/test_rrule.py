from datetime import date
from dateutil_rrule.rrule import rrule, YEARLY, MONTHLY

def test_yearly_standard():
    rule = rrule(YEARLY, dtstart=date(2020, 1, 15), count=3)
    assert rule.between(date(2020, 1, 1), date(2025, 1, 1)) == [
        date(2020, 1, 15), date(2021, 1, 15), date(2022, 1, 15)
    ]

def test_leap_year_feb29_recurrence():
    rule = rrule(YEARLY, dtstart=date(2020, 2, 29), count=2)
    assert rule.between(date(2020, 1, 1), date(2025, 12, 31)) == [
        date(2020, 2, 29), date(2024, 2, 29)
    ]
