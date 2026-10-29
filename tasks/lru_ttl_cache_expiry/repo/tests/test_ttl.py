import time, pytest
from ttl_cache import TTLCache

def test_basic_get_put():
    c = TTLCache(capacity=2)
    c.put("a", 1)
    assert c.get("a") == 1

def test_lru_eviction():
    c = TTLCache(capacity=2)
    c.put("a", 1)
    c.put("b", 2)
    c.get("a") # access a -> b becomes LRU
    c.put("c", 3) # evicts b
    assert c.get("a") == 1
    assert c.get("b") is None
    assert c.get("c") == 3

def test_ttl_expiration_returns_none():
    c = TTLCache(capacity=2, default_ttl=0.1)
    c.put("expiring", 42, ttl=0.1)
    time.sleep(0.15)
    assert c.get("expiring") is None

def test_evict_expired_before_active_lru():
    c = TTLCache(capacity=2)
    c.put("expiring", 1, ttl=0.1)
    c.put("active", 2, ttl=60.0)
    time.sleep(0.15)
    c.put("new_key", 3)
    assert c.get("active") == 2
    assert c.get("new_key") == 3
    assert c.get("expiring") is None
