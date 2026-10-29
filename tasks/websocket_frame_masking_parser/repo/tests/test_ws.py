import pytest
from ws_frame import decode_websocket_frame

def test_unmasked_small_text_frame():
    raw = bytes([0x81, 0x05]) + b"Hello"
    res = decode_websocket_frame(raw)
    assert res["fin"] is True
    assert res["opcode"] == 1
    assert res["payload"] == b"Hello"

def test_masked_text_frame():
    mask_key = bytes([0x37, 0xfa, 0x21, 0x3d])
    original = b"Hello"
    masked = bytes(b ^ mask_key[i % 4] for i, b in enumerate(original))
    raw = bytes([0x81, 0x85]) + mask_key + masked
    res = decode_websocket_frame(raw)
    assert res["payload"] == b"Hello"

def test_extended_16bit_length_frame():
    payload = b"A" * 200
    raw = bytes([0x82, 126, 0, 200]) + payload
    res = decode_websocket_frame(raw)
    assert res["payload"] == payload
