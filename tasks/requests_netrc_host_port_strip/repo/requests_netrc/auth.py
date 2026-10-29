import urllib.parse

def get_netrc_login(url: str, netrc_hosts: dict):
    parsed = urllib.parse.urlsplit(url)
    host = parsed.netloc
    return netrc_hosts.get(host)
