from datetime import datetime, timedelta

def parse_iso_utc(ts: str) -> datetime:
    date_part, time_part = ts.split("T")
    y, m, d = (int(x) for x in date_part.split("-"))
    hh, mm, ss = (int(x) for x in time_part.split(":"))
    return datetime(y, m, d, hh, mm, ss)
