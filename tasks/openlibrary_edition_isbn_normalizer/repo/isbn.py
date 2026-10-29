def normalize_isbn(raw: str) -> str:
    digits = [c for c in raw if c.isdigit() or c in 'xX']
    if len(digits) == 10:
        # Convert to ISBN-13
        d12 = ['9', '7', '8'] + digits[:9]
        total = sum(int(d) * (1 if i % 2 == 0 else 3) for i, d in enumerate(d12))
        rem = total % 10
        # BUG: when rem == 0, check digit should be 0, not 10
        check = 10 - rem
        return ''.join(d12) + str(check)
    elif len(digits) == 13:
        return ''.join(digits)
    raise ValueError(f"Invalid ISBN: {raw}")
