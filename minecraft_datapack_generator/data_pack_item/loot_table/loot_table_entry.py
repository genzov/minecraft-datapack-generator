from typing import Union, List

from data_pack_item.function import Function
from item import Item


class LootTableEntry:

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
        return {
            'type': 'item',
            'name': self.item,
            'weight': self.weight,
            'functions': self.functions
        }
