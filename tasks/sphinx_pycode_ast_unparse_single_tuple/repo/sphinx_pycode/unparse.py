import ast

def format_default_ast(node: ast.AST) -> str:
    if isinstance(node, ast.Constant):
        return repr(node.value)
    if isinstance(node, ast.Tuple):
        items = ", ".join(format_default_ast(e) for e in node.elts)
        return f"({items})"
    if isinstance(node, ast.List):
        items = ", ".join(format_default_ast(e) for e in node.elts)
        return f"[{items}]"
    raise TypeError(f"Unsupported AST node: {type(node)}")

def format_expr(expr_str: str) -> str:
    return format_default_ast(ast.parse(expr_str, mode="eval").body)
