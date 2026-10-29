def decode_websocket_frame(data: bytes) -> dict:
    if len(data) < 2: raise ValueError("Frame too short")
    byte0, byte1 = data[0], data[1]
    fin = (byte0 & 0x80) != 0
    opcode = byte0 & 0x0F
    is_masked = (byte1 & 0x80) != 0
    payload_len = byte1 & 0x7F

    # BUG: Fails to handle masked frames (does not XOR payload) and fails on 16-bit extended length
    payload = data[2:2 + payload_len]
    return {"fin": fin, "opcode": opcode, "payload": payload}
