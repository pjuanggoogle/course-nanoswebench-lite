from urllib.parse import urlparse

def get_netrc_login(url: str, netrc_hosts: dict[str, tuple[str, str]]):
    host = urlparse(url).netloc
    if not host:
        return None
    return netrc_hosts.get(host)
