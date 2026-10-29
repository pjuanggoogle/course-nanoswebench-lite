def cookie_domain_matches(request_host: str, cookie_domain: str) -> bool:
    request_host = request_host.lower()
    target = cookie_domain.lstrip(".").lower()
    return request_host.endswith(target)
