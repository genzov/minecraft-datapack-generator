from typing import Dict, List

from data_pack_item.recipe import BaseRecipe
from item import Item


class RecipeShaped(BaseRecipe):

    def __init__(self, name: str, keys: Dict[str, Item], pattern: List[str],
                 result_item: Item, result_amount: int = 1, group: str = None):
        super().__init__(name, result_item, result_amount, group)
        self.keys = keys
        self.pattern = pattern

    def content(self) -> Dict:
        content = {
            'type': 'minecraft:crafting_shaped',
            'pattern': self.pattern,
            'key': {k: {'item': v} for k, v in self.keys.items()},
            'result': {
                'item': self.result_item,
                'count': self.result_amount
            },
        }

        if self.group:
            content['group'] = self.group

        return content
