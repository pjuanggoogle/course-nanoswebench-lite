import pytest
from pytest_fixtures.manager import FixtureManager, TeardownErrorGroup

def test_clean_fixtures():
    fm = FixtureManager()
    cleaned = []
    def f1():
        yield 1
        cleaned.append(1)
    def f2():
        yield 2
        cleaned.append(2)
    fm.register(f1())
    fm.register(f2())
    fm.teardown()
    assert cleaned == [2, 1]

def test_teardown_all_fixtures_even_if_first_fails():
    fm = FixtureManager()
    cleaned = []
    def f1():
        yield 1
        cleaned.append(1)
    def f2_failing():
        yield 2
        raise RuntimeError("Failure in f2 teardown")
    def f3():
        yield 3
        cleaned.append(3)

    fm.register(f1())
    fm.register(f2_failing())
    fm.register(f3())

    with pytest.raises(TeardownErrorGroup) as excinfo:
        fm.teardown()

    assert cleaned == [3, 1]
    assert len(excinfo.value.errors) == 1
    assert "Failure in f2 teardown" in str(excinfo.value.errors[0])
