import urllib.parse

class PreparedRequest:
    def __init__(self):
        self.url = None

    def prepare_url(self, url: str, params: dict = None) -> None:
        if not params:
            self.url = url
            return

        scheme, netloc, path, query, fragment = urllib.parse.urlsplit(url)
        # BUG: doseq is not set to True, so lists are stringified as brackets
        new_query = urllib.parse.urlencode(params)

        if query:
            final_query = f"{query}&{new_query}"
        else:
            final_query = new_query

        self.url = urllib.parse.urlunsplit((scheme, netloc, path, final_query, fragment))
