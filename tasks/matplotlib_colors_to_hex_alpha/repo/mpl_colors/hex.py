def to_hex(color: tuple[float, ...], keep_alpha: bool = False) -> str:
    channels = [round(c * 255) for c in color[:3]]
    return "#" + "".join(f"{c:02x}" for c in channels)
