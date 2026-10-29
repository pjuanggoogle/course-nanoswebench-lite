class CookieJar:
    def __init__(self):
        self.cookies = []

    def set_cookie(self, name: str, value: str, domain: str):
        self.cookies.append((name, value, domain.lower()))

    def get_for_host(self, host: str) -> dict[str, str]:
        host = host.lower()
        matched = {}
        for name, value, cdom in self.cookies:
            if host.endswith(cdom):
                matched[name] = value
        return matched
