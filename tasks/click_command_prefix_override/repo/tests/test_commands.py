import pytest
from click_cli.core import Group, Command, Context, AmbiguousCommandError, NoSuchCommandError

def test_basic_command():
    g = Group()
    g.add_command(Command("status"))
    assert g.get_command(Context(prefix_matching=False), "status").name == "status"

def test_unique_prefix_match():
    g = Group()
    g.add_command(Command("deploy"))
    assert g.get_command(Context(prefix_matching=True), "dep").name == "deploy"

def test_exact_match_priority():
    g = Group()
    g.add_command(Command("run"))
    g.add_command(Command("runner"))
    assert g.get_command(Context(prefix_matching=True), "run").name == "run"
    with pytest.raises(AmbiguousCommandError):
        g.get_command(Context(prefix_matching=True), "ru")
