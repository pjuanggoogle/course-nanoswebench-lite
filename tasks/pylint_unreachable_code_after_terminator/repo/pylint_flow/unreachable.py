import ast

TERMINATORS = (ast.Return, ast.Raise)

def _check_block(stmts: list[ast.stmt], out: list[int]):
    terminated = False
    for s in stmts:
        if terminated:
            out.append(s.lineno)
        if isinstance(s, TERMINATORS):
            terminated = True
        for attr in ("body", "orelse", "finalbody"):
            sub = getattr(s, attr, None)
            if isinstance(sub, list):
                _check_block(sub, out)

def find_unreachable_lines(code: str) -> list[int]:
    tree = ast.parse(code)
    out = []
    _check_block(tree.body, out)
    return out
