from contextlib import contextmanager
import logging

class LogCapture:
    def __init__(self, logger: logging.Logger):
        self.logger = logger

    @contextmanager
    def at_level(self, level: int):
        old_level = self.logger.level
        self.logger.setLevel(level)
        yield
        self.logger.setLevel(old_level)
