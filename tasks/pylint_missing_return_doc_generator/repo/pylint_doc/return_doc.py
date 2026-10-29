import ast

def needs_return_doc(func_code: str) -> bool:
    tree = ast.parse(func_code)
    func = tree.body[0]
    for node in ast.walk(func):
        if isinstance(node, ast.Return):
            return node.value is not None
    return False
