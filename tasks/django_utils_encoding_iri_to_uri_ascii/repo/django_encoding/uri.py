import urllib.parse

def iri_to_uri(iri: str) -> str:
    if not iri:
        return iri
    return urllib.parse.quote(iri)
