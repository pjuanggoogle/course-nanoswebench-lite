from pytest_mp.monkeypatch import MonkeyPatch

def test_single_setenv_undo():
    env = {"HOME": "/home/user"}
    mp = MonkeyPatch(env)
    mp.setenv("NEW_VAR", "1")
    mp.undo()
    assert env == {"HOME": "/home/user"}

def test_repeated_setenv_restores_original():
    env = {"MODE": "prod"}
    mp = MonkeyPatch(env)
    mp.setenv("MODE", "stage")
    mp.setenv("MODE", "dev")
    mp.setenv("TEMP", "x")
    mp.setenv("TEMP", "y")
    mp.undo()
    assert env == {"MODE": "prod"}
