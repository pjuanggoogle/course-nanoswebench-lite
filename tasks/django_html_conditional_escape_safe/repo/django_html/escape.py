import html

class SafeString(str):
    def __html__(self):
        return str(self)

def conditional_escape(text) -> str:
    return html.escape(str(text))
