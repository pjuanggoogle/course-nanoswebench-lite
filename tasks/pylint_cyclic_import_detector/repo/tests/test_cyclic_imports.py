import pytest
from pylint_checker.cyclic_imports import CyclicImportChecker

def test_top_level_direct_cycle():
    checker = CyclicImportChecker()
    checker.add_import("mod_a", "mod_b", is_top_level=True)
    checker.add_import("mod_b", "mod_a", is_top_level=True)
    cycles = checker.find_cycles()
    assert len(cycles) == 1
    assert cycles[0] == ["mod_a", "mod_b", "mod_a"]

def test_type_checking_guard_ignored():
    checker = CyclicImportChecker()
    checker.add_import("mod_a", "mod_b", is_top_level=True)
    # mod_b only imports mod_a inside `if TYPE_CHECKING:`
    checker.add_import("mod_b", "mod_a", is_top_level=True, is_type_checking=True)
    assert checker.find_cycles() == []

def test_function_local_import_ignored():
    checker = CyclicImportChecker()
    checker.add_import("mod_a", "mod_b", is_top_level=True)
    # mod_b imports mod_a inside a function
    checker.add_import("mod_b", "mod_a", is_top_level=False, is_type_checking=False)
    assert checker.find_cycles() == []
