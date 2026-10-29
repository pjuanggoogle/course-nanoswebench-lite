class CyclicImportChecker:
    def __init__(self):
        self.graph = {}

    def add_import(self, from_mod: str, to_mod: str, is_top_level: bool = True, is_type_checking: bool = False):
        # BUG: Records all imports identically regardless of scope
        if from_mod not in self.graph:
            self.graph[from_mod] = set()
        self.graph[from_mod].add(to_mod)

    def find_cycles(self) -> list[list[str]]:
        cycles = []
        visited = set()
        rec_stack = []

        def dfs(node):
            visited.add(node)
            rec_stack.append(node)
            for neighbor in sorted(self.graph.get(node, [])):
                if neighbor not in visited:
                    dfs(neighbor)
                elif neighbor in rec_stack:
                    idx = rec_stack.index(neighbor)
                    cycles.append(rec_stack[idx:] + [neighbor])
            rec_stack.pop()

        for node in sorted(self.graph.keys()):
            if node not in visited:
                dfs(node)
        return cycles
