def format_failure(exc: Exception, obj) -> str:
    """Formats test failure with object representation."""
    obj_repr = repr(obj) # BUG: Crashes if obj.__repr__ raises
    return f"FAIL: {type(exc).__name__}: {str(exc)} | target={obj_repr}"
