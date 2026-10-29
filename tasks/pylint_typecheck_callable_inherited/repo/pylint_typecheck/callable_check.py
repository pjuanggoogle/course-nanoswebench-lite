def is_callable_instance(cls_methods: set[str], base_method_sets: list[set[str]]) -> bool:
    return "__call__" in cls_methods
