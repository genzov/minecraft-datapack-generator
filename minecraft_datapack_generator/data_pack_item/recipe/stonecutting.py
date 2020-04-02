from abc import ABC

from data_pack_item.recipe import Recipe
from util.item import Item


class StoneCut(Recipe, ABC):
    def __init__(self, name: str, input_item: Item, output_item: Item, output_amount: int = 1,
                 namespace: str = 'minecraft'):
        super().__init__(namespace, name, output_item, output_amount)
        self.type = type
        self.input_item = input_item

    def content(self):
        return {
            'type': 'minecraft:stonecutting',
            'ingredient': {
                'item': self.input_item
            },
            'result': self.output_item,
            'count': self.output_amount
        }
