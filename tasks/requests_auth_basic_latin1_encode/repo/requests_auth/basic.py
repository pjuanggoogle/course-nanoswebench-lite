import base64

def basic_auth_header(username: str, password: str) -> str:
    raw = f"{username}:{password}".encode("ascii")
    token = base64.b64encode(raw).decode("ascii")
    return f"Basic {token}"
