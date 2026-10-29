class AppContext:
    active_stack = []

    def __init__(self, name: str):
        self.name = name

    def push(self):
        AppContext.active_stack.append(self)

    def pop(self):
        if AppContext.active_stack and AppContext.active_stack[-1] is self:
            AppContext.active_stack.pop()

def stream_with_context(ctx: AppContext, gen):
    # BUG: Does not wrap in generator try/finally to pop ctx if generator is closed early
    ctx.push()
    for item in gen:
        yield item
    ctx.pop()
