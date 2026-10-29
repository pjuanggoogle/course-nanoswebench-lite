def pop_warning(recorded: list, expected_cls: type):
    for i, w in enumerate(recorded):
        if type(w) is expected_cls:
            return recorded.pop(i)
    raise AssertionError(f"{expected_cls.__name__} not found")
