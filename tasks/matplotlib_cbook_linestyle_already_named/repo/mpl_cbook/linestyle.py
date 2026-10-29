SHORT_TO_LONG = {
    "-": "solid",
    "--": "dashed",
    "-.": "dashdot",
    ":": "dotted",
}

def resolve_linestyle(ls: str) -> str:
    if ls in SHORT_TO_LONG:
        return SHORT_TO_LONG[ls]
    raise ValueError(f"Unknown linestyle: {ls}")
