import time, pytest
from rate_limiter import TokenBucket

def test_initial_burst_capacity():
    b = TokenBucket(capacity=5, refill_rate_per_sec=1.0)
    for _ in range(5):
        assert b.allow_request(1) is True
    assert b.allow_request(1) is False

def test_subsecond_fractional_token_refill():
    b = TokenBucket(capacity=2, refill_rate_per_sec=10.0)
    assert b.allow_request(2) is True
    assert b.allow_request(1) is False
    # Sleep 0.15s -> should refill 1.5 tokens
    time.sleep(0.15)
    assert b.allow_request(1) is True
