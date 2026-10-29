class Form:
    def __init__(self, data: dict, initial: dict = None):
        self.data = data or {}
        self.initial = initial or {}

    @property
    def changed_data(self) -> list[str]:
        changed = []
        for name, bound_val in self.data.items():
            init_val = self.initial.get(name)
            if bound_val != init_val:
                changed.append(name)
        return changed
