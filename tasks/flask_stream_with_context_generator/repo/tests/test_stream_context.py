import pytest
from flask_ctx.helpers import AppContext, stream_with_context

def test_normal_stream_consumes_all():
    ctx = AppContext("req_1")
    def my_gen():
        yield "chunk1"
        yield "chunk2"

    streamed = list(stream_with_context(ctx, my_gen()))
    assert streamed == ["chunk1", "chunk2"]
    assert len(AppContext.active_stack) == 0

def test_early_generator_close_cleans_context():
    ctx = AppContext("req_2")
    def infinite_gen():
        i = 0
        while True:
            yield f"chunk_{i}"
            i += 1

    stream = stream_with_context(ctx, infinite_gen())
    # Consumer takes 1 item and closes
    item = next(stream)
    assert item == "chunk_0"
    assert len(AppContext.active_stack) == 1
    stream.close() # Early termination
    assert len(AppContext.active_stack) == 0

def test_generator_exception_cleans_context():
    ctx = AppContext("req_3")
    def faulty_gen():
        yield "start"
        raise ValueError("Stream failed midway")

    stream = stream_with_context(ctx, faulty_gen())
    assert next(stream) == "start"
    with pytest.raises(ValueError):
        next(stream)
    assert len(AppContext.active_stack) == 0
