def check_exit_signature(args: list[str]) -> bool:
    if not args or args[0] != "self":
        return False
    return len(args) == 4
