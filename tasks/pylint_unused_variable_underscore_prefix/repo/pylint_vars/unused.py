import ast

def find_unused_variables(code: str) -> list[str]:
    tree = ast.parse(code)
    stored = []
    loaded = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            if isinstance(node.ctx, ast.Store) and node.id not in stored:
                stored.append(node.id)
            elif isinstance(node.ctx, ast.Load):
                loaded.add(node.id)
    return [name for name in stored if name not in loaded]
