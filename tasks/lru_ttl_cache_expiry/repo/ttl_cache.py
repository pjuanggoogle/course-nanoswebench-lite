from collections import OrderedDict
import time

class TTLCache:
    def __init__(self, capacity: int, default_ttl: float = 60.0):
        self.capacity = capacity
        self.default_ttl = default_ttl
        self.cache = OrderedDict()
        self.expiry = {}

    def get(self, key):
        # BUG: Does not check expiration timestamp, returning expired data
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return None

    def put(self, key, value, ttl: float = None):
        if ttl is None: ttl = self.default_ttl
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        self.expiry[key] = time.time() + ttl
        if len(self.cache) > self.capacity:
            oldest, _ = self.cache.popitem(last=False)
            self.expiry.pop(oldest, None)
