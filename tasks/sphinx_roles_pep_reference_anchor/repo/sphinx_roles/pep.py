def make_pep_url(target: str) -> str:
    num = int(target)
    return f"https://peps.python.org/pep-{num:04d}/"
