def parse_csv_option(raw: str) -> list[str]:
    return [item.strip() for item in raw.split(",")]
