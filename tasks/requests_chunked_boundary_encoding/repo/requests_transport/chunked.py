from typing import Iterable, Optional

CRLF = b"\r\n"

def encode_chunked_request(chunks: Iterable[bytes], trailers: Optional[dict[str, str]] = None) -> bytes:
    body = bytearray()
    for c in chunks:
        hex_len = f"{len(c):X}".encode("ascii") + CRLF
        body.extend(hex_len)
        body.extend(c)
        body.extend(CRLF)
    return bytes(body)
