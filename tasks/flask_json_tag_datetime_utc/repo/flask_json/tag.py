from datetime import datetime, timezone

def serialize_datetime(dt: datetime) -> str:
    if dt.tzinfo is None:
        return dt.isoformat()
    utc_dt = dt.astimezone(timezone.utc)
    return utc_dt.isoformat() + "Z"
