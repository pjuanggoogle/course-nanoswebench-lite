def convert_with_equivalencies(val: float, from_unit: str, to_unit: str, equivalencies: list) -> float:
    if from_unit == to_unit:
        return float(val)
    for u1, u2, fwd, bwd in equivalencies:
        if u1 == from_unit and u2 == to_unit:
            return fwd(val)
    raise ValueError(f"Cannot convert {from_unit} to {to_unit}")
