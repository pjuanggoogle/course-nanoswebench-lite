import logging
import pytest
from pytest_caplog.caplog import LogCapture

def test_normal_level_restore():
    lg = logging.getLogger("test_normal")
    lg.setLevel(logging.WARNING)
    cap = LogCapture(lg)
    with cap.at_level(logging.DEBUG):
        assert lg.level == logging.DEBUG
    assert lg.level == logging.WARNING

def test_restore_level_on_exception():
    lg = logging.getLogger("test_exc")
    lg.setLevel(logging.ERROR)
    cap = LogCapture(lg)
    with pytest.raises(RuntimeError):
        with cap.at_level(logging.INFO):
            raise RuntimeError("boom")
    assert lg.level == logging.ERROR
