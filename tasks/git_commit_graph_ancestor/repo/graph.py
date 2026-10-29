def find_lowest_common_ancestors(graph: dict[str, list[str]], a: str, b: str) -> set[str]:
    """Find lowest common ancestor commits (merge bases)."""
    def get_ancestors(node):
        visited = set()
        queue = [node]
        while queue:
            cur = queue.pop(0)
            if cur not in visited:
                visited.add(cur)
                queue.extend(graph.get(cur, []))
        return visited

    anc_a = get_ancestors(a)
    anc_b = get_ancestors(b)
    common = anc_a.intersection(anc_b)
    # BUG: Returns all common ancestors without filtering redundant ones (ancestors of ancestors)
    return common
