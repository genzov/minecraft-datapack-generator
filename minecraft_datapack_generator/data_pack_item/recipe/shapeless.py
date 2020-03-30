from typing import List, Union, Dict

from data_pack_item.recipe import BaseRecipe


class RecipeShapeless(BaseRecipe):

    def __init__(self, name: str, ingredients: List[Union[str, List[str]]],
                 result_item: str, result_amount: int = 1, group: str = None):
        super().__init__(name, result_item, result_amount, group)
        self.ingredients = ingredients

    def transform_ingredients(self, ingredients):
        transformed = []
        for i in ingredients:
            if isinstance(i, str):
                transformed.append({'item': f'minecraft:{i}'})
            elif isinstance(i, List):
                transformed.append(self.transform_ingredients(i))
        return transformed

    def content(self) -> Dict:
        content = {
            "type": "crafting_shapeless",
            "ingredients": self.transform_ingredients(self.ingredients),
            'result': {
                'item': f'minecraft:{self.result_item}',
                'count': self.result_amount
            }
        }

        if self.group:
            content['group'] = self.group

        return content
