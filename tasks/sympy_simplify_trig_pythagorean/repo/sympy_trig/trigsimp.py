def simplify_pythagorean(terms: dict[str, int]) -> dict[str, int]:
    out = dict(terms)
    if out.get("sin2") == 1 and out.get("cos2") == 1:
        out["const"] = out.get("const", 0) + 1
        del out["sin2"]
        del out["cos2"]
    return {k: v for k, v in out.items() if v != 0}
