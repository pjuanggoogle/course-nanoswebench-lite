import re

OPT_GROUP_RE = re.compile(r"\(\?:([^()]*\(\?P<(\w+)>[^()]+\)[^()]*)\)\?")
NAMED_GROUP_RE = re.compile(r"\(\?P<(\w+)>[^()]+\)")

def reverse_pattern(pattern: str, **kwargs) -> str:
    def _replace_opt(m):
        inner, name = m.group(1), m.group(2)
        val = kwargs.get(name)
        return NAMED_GROUP_RE.sub(str(val), inner)

    out = OPT_GROUP_RE.sub(_replace_opt, pattern)
    for m in NAMED_GROUP_RE.finditer(out):
        name = m.group(1)
        if name not in kwargs or kwargs[name] is None:
            raise ValueError(f"Missing required parameter: {name}")
    return NAMED_GROUP_RE.sub(lambda m: str(kwargs[m.group(1)]), out)
