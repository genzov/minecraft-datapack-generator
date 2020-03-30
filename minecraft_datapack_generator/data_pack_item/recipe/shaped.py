from typing import Dict, List

from data_pack_item.recipe import BaseRecipe


class RecipeShaped(BaseRecipe):

    def __init__(self, name: str, keys: Dict[str, str], pattern: List[str],
                 result_item: str, result_amount: int = 1, group: str = None):
        super().__init__(name, result_item, result_amount, group)
        self.keys = keys
        self.pattern = pattern

    def content(self) -> Dict:
        content = {
            'type': 'minecraft:crafting_shaped',
            'pattern': self.pattern,
            'key': {k: {'item': f'minecraft:{v}'} for k, v in self.keys.items()},
            'result': {
                'item': f'minecraft:{self.result_item}',
                'count': self.result_amount
            },
        }

        if self.group:
            content['group'] = self.group

        return content
