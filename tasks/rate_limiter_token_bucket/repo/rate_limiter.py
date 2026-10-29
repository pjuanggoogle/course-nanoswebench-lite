import time

class TokenBucket:
    def __init__(self, capacity: int, refill_rate_per_sec: float):
        self.capacity = float(capacity)
        self.tokens = float(capacity)
        self.refill_rate = refill_rate_per_sec
        self.last_time = time.time()

    def allow_request(self, tokens: int = 1) -> bool:
        now = time.time()
        # BUG: Truncating elapsed time to int loses fractional refill on rapid requests
        elapsed = int(now - self.last_time)
        if elapsed > 0:
            self.tokens = min(self.capacity, self.tokens + elapsed * self.refill_rate)
            self.last_time = now
        if self.tokens >= tokens:
            self.tokens -= tokens
            return True
        return False
