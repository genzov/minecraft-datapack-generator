from typing import Dict

from data_pack_item.recipe import BaseRecipe
from data_pack_item.recipe.grid import Grid
from item import Item


class RecipeShaped(BaseRecipe):

    def __init__(self, name: str, grid: Grid,
                 result_item: Item, result_amount: int = 1):
        super().__init__(name, result_item, result_amount)
        self.grid = grid

    def content(self) -> Dict:
        return {
            'type': 'minecraft:crafting_shaped',
            'pattern': self.grid.get_pattern(),
            'key': {k: {'item': v} for k, v in self.grid.get_keys().items()},
            'result': {
                'item': self.result_item,
                'count': self.result_amount
            },
        }
