from abc import ABC
from typing import Dict

from data_pack_item.recipe import BaseRecipe
from item import Item


class StoneCut(BaseRecipe, ABC):
    def __init__(self, name: str, ingredient: Item, result_item: Item, result_amount: int = 1):
        super().__init__(name, result_item, result_amount)
        self.type = type
        self.ingredient = ingredient

    def content(self) -> Dict:
        return {
            'type': 'minecraft:stonecutting',
            'ingredient': {
                'item': self.ingredient
            },
            'result': self.result_item,
            'count': self.result_amount
        }
