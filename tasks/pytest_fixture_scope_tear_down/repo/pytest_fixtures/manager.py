from typing import Callable, Generator, Any

class TeardownErrorGroup(Exception):
    def __init__(self, errors: list[Exception]):
        self.errors = errors
        super().__init__(f"{len(errors)} teardown errors occurred: {[str(e) for e in errors]}")

class FixtureManager:
    def __init__(self):
        self.stack = []

    def register(self, gen: Generator[Any, None, None]):
        val = next(gen)
        self.stack.append(gen)
        return val

    def teardown(self):
        # BUG: Stops at the first exception, leaving remaining generators unfinalized
        while self.stack:
            gen = self.stack.pop()
            try:
                next(gen)
            except StopIteration:
                pass
