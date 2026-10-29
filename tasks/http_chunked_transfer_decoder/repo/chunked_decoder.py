def decode_chunked_stream(raw: bytes) -> bytes:
    body = bytearray()
    idx = 0
    while idx < len(raw):
        crlf = raw.find(b"\r\n", idx)
        if crlf == -1: break
        header = raw[idx:crlf]
        # BUG: Int conversion fails if chunk has extensions (e.g. '1f;ext=val')
        chunk_len = int(header, 16)
        if chunk_len == 0:
            break
        idx = crlf + 2
        chunk = raw[idx:idx + chunk_len]
        body.extend(chunk)
        idx += chunk_len + 2
    return bytes(body)
