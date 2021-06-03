from collections.abc import MutableMapping
from typing import Dict, Callable, Iterator

class Commands(MutableMapping):
    def __init__(self) -> None:
        self.commands: Dict[str, Callable] = {'help' : self.help}

    def __repr__(self) -> str:
        return f'Commands(' + ', '.join(cmd for cmd in self.commands) + ')'

    def __getitem__(self, cmd) -> Callable:
        try:
            return self.commands[cmd]
        except KeyError:
            raise KeyError(f'command not found: {cmd}')

    def __setitem__(self, cmd: str, callback: Callable) -> None:
        self.commands[cmd] = callback

    def __delitem__(self, cmd) -> None:
        del self.commands[cmd]

    def __iter__(self) -> Iterator:
        return iter(self.commands)

    def __len__(self) -> int:
        return len(self.commands)

    def execute(self, cmd: str, *args) -> None:
        '''Execute the command from the CLI'''

        command = self.commands.get(cmd)
        if command:
            try:
                command(*args)
            except TypeError as e:
                print(e)
        else:
            raise ValueError('there is no command with that name')

    def help(self) -> None:
        '''Prints the help for all registered functions'''

        for cmd in self.commands.values():
            print(cmd.__name__)
            print('  ', cmd.__doc__)

    @property
    def completer(self) -> tuple:
        '''returns the commands which can be used for autocomplete'''

        return tuple(self.commands.keys())