class Commands:
    def __init__(self) -> None:
        self.commands = {
            'help' : self.help
        }

    def __repr__(self) -> str:
        return f'Commands(' + ', '.join(cmd for cmd in self.commands) + ')'

    def register(self, cmd, callback):
        if cmd in self.commands:
            raise ValueError('a function has already been registed to this command')

        self.commands[cmd] = callback

    def execute(self, cmd, *args):
        command = self.commands.get(cmd)
        if command:
            try:
                command(*args)
            except TypeError as e:
                print(e)
        else:
            raise ValueError('there is no command with that name')

    def help(self):
        '''Prints the help for all registered functions'''

        for cmd in self.commands.values():
            print(cmd.__name__)
            print('  ', cmd.__doc__)

    @property
    def completer(self):
        return tuple(self.commands.keys())