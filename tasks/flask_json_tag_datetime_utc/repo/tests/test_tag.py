from datetime import datetime, timezone, timedelta
from flask_json.tag import serialize_datetime

def test_naive_datetime():
    dt = datetime(2024, 5, 1, 12, 30, 0)
    assert serialize_datetime(dt) == "2024-05-01T12:30:00"

def test_aware_utc_and_offset_datetime():
    dt_utc = datetime(2024, 5, 1, 12, 30, 0, tzinfo=timezone.utc)
    assert serialize_datetime(dt_utc) == "2024-05-01T12:30:00Z"
    tz_plus2 = timezone(timedelta(hours=2))
    dt_offset = datetime(2024, 5, 1, 14, 30, 0, tzinfo=tz_plus2)
    assert serialize_datetime(dt_offset) == "2024-05-01T12:30:00Z"
