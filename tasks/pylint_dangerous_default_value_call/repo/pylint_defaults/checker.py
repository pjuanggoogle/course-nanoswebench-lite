import ast

def _is_mutable_default(node: ast.AST) -> bool:
    return isinstance(node, (ast.List, ast.Dict, ast.Set))

def find_dangerous_defaults(code: str) -> list[str]:
    tree = ast.parse(code)
    flagged = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            defaults = list(node.args.defaults) + [
                d for d in node.args.kw_defaults if d is not None
            ]
            if any(_is_mutable_default(d) for d in defaults):
                flagged.append(node.name)
    return flagged
