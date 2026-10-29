import pytest
from graph import find_lowest_common_ancestors

def test_linear_history():
    # c3 -> c2 -> c1
    g = {"c3": ["c2"], "c2": ["c1"], "c1": []}
    assert find_lowest_common_ancestors(g, "c3", "c2") == {"c2"}

def test_simple_branch_fork():
    # c3 -> c1, c2 -> c1
    g = {"c3": ["c1"], "c2": ["c1"], "c1": []}
    assert find_lowest_common_ancestors(g, "c3", "c2") == {"c1"}

def test_prune_redundant_ancestors_in_diamond_graph():
    # c4 -> c2, c3
    # c2 -> c1
    # c3 -> c1
    g = {"c4": ["c2", "c3"], "c2": ["c1"], "c3": ["c1"], "c1": []}
    # Ancestors of c2 and c3 include c1, and lowest common ancestor is {c1}
    assert find_lowest_common_ancestors(g, "c2", "c3") == {"c1"}
    # Ancestors of c4 and c1 is {c1}
    assert find_lowest_common_ancestors(g, "c4", "c1") == {"c1"}

def test_criss_cross_multiple_merge_bases():
    # Criss-cross merge:
    # m1 -> c1, c2
    # m2 -> c1, c2
    g = {"m1": ["c1", "c2"], "m2": ["c1", "c2"], "c1": ["root"], "c2": ["root"], "root": []}
    assert find_lowest_common_ancestors(g, "m1", "m2") == {"c1", "c2"}
