class ClickException(Exception):
    pass

class NoSuchCommandError(ClickException):
    pass

class AmbiguousCommandError(ClickException):
    pass

class Context:
    def __init__(self, prefix_matching: bool = True):
        self.prefix_matching = prefix_matching

class Command:
    def __init__(self, name: str):
        self.name = name

class Group(Command):
    def __init__(self, name: str = "cli"):
        super().__init__(name)
        self.commands = {}

    def add_command(self, cmd: Command, name: str = None):
        self.commands[name or cmd.name] = cmd

    def get_command(self, ctx: Context, cmd_name: str) -> Command:
        if not ctx.prefix_matching:
            if cmd_name in self.commands:
                return self.commands[cmd_name]
            raise NoSuchCommandError(f"No such command '{cmd_name}'.")

        matches = [n for n in self.commands if n.startswith(cmd_name)]
        if len(matches) == 1:
            return self.commands[matches[0]]
        if len(matches) > 1:
            raise AmbiguousCommandError(f"Too many matches for '{cmd_name}': {matches}")
        raise NoSuchCommandError(f"No such command '{cmd_name}'.")
