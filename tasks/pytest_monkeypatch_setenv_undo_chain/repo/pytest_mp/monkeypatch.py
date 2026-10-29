class MonkeyPatch:
    def __init__(self, env: dict[str, str]):
        self.env = env
        self._saved_env = []

    def setenv(self, name: str, value: str):
        self._saved_env.append((name, self.env.get(name)))
        self.env[name] = str(value)

    def undo(self):
        for name, old_val in self._saved_env:
            if old_val is None:
                self.env.pop(name, None)
            else:
                self.env[name] = old_val
        self._saved_env.clear()
