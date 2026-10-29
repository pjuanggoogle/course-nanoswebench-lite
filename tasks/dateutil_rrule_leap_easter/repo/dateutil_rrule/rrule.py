from datetime import date

YEARLY = 1
MONTHLY = 2

class rrule:
    def __init__(self, freq: int, dtstart: date, count: int = 5):
        self.freq = freq
        self.dtstart = dtstart
        self.count = count

    def between(self, after: date, before: date) -> list[date]:
        res = []
        year, month, day = self.dtstart.year, self.dtstart.month, self.dtstart.day
        for _ in range(100):
            if len(res) >= self.count:
                break
            candidate = date(year, month, day)
            if after <= candidate <= before:
                res.append(candidate)
            if self.freq == YEARLY:
                year += 1
            else:
                month = 1 if month == 12 else month + 1
                if month == 1:
                    year += 1
        return res
