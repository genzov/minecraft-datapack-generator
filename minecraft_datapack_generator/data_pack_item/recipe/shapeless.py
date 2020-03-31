from typing import List, Union, Dict

from data_pack_item.recipe import BaseRecipe
from item import Item


class RecipeShapeless(BaseRecipe):

    def __init__(self, name: str, ingredients: List[Union[Item, List[Item]]],
                 result_item: Item, result_amount: int = 1):
        super().__init__(name, result_item, result_amount)
        self.ingredients = ingredients

    def transform_ingredients(self, ingredients):
        transformed = []
        for i in ingredients:
            if isinstance(i, Item):
                transformed.append({'item': i})
            elif isinstance(i, List):
                transformed.append(self.transform_ingredients(i))
        return transformed

    def content(self) -> Dict:
        return {
            "type": "minecraft:crafting_shapeless",
            "ingredients": self.transform_ingredients(self.ingredients),
            'result': {
                'item': self.result_item,
                'count': self.result_amount
            }
        }
