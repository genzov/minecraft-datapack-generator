from typing import Union, List

from data_pack_item.function import Function
from data_pack_item.loot_table.loot_table_meta import LootTableMeta
from item import Item


class LootTableEntry(LootTableMeta):

    def __init__(self, item: Item, weight: int = 1, functions: Union[Function, List[Function]] = None):
        self.item = item
        self.weight = weight

        if functions is None:
            functions = []
        if isinstance(functions, List):
            self.functions = functions
        else:
            self.functions = [functions]

    def content(self):
        result = {
            'type': 'item',
            'name': self.item,
            'weight': self.weight,
        }

        if self.functions:
            result['functions'] = self.functions

        return result
