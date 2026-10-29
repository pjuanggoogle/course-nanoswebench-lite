def apply_patch(original: str, hunk_target_line: int, old_lines: list[str], new_lines: list[str]) -> str:
    lines = original.splitlines(keepends=True)
    # BUG: Fails when hunk_target_line does not match exact offset due to previous changes
    idx = hunk_target_line - 1
    if lines[idx:idx + len(old_lines)] == old_lines:
        lines[idx:idx + len(old_lines)] = new_lines
        return ''.join(lines)
    raise ValueError("Hunk could not be applied at specified line")
