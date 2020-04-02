from typing import Union, List

from data_pack_item import DataPackItem
from data_pack_item.function.command import Command


class Function(DataPackItem):

    def __init__(self, name: str, commands: Union[Command, List[Command]], namespace: str = 'minecraft'):
        super().__init__(namespace, 'functions', name, 'mcfunction')
        if isinstance(commands, List):
            self.commands = commands
        else:
            self.commands = [commands]

    def content(self):
        return '\n'.join(c.value for c in self.commands)
