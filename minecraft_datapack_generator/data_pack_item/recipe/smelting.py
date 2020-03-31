from abc import ABC
from typing import Dict

from data_pack_item.recipe import BaseRecipe
from item import Item


class BaseCooking(BaseRecipe, ABC):
    def __init__(self, name: str, ingredient: Item, result_item: Item, type: str,
                 experience: float = 0.1, cooking_time: int = 200, result_amount: int = 1):
        super().__init__(name, result_item, result_amount)
        self.type = type
        self.ingredient = ingredient
        self.experience = experience
        self.cooking_time = cooking_time

    def content(self) -> Dict:
        return {
            'type': self.type,
            'ingredient': {
                'item': self.ingredient
            },
            'result': self.result_item,
            'experience': self.experience,
            'cookingtime': self.cooking_time
        }


class Blast(BaseCooking):

    def __init__(self, name: str, ingredient: Item, result_item: Item,
                 experience: float = 0.1, cooking_time: int = 200, result_amount: int = 1):
        super().__init__(name, ingredient, result_item, 'minecraft:blasting', experience, cooking_time, result_amount)


class Campfire(BaseCooking):

    def __init__(self, name: str, ingredient: Item, result_item: Item,
                 experience: float = 0.1, cooking_time: int = 200, result_amount: int = 1):
        super().__init__(name, ingredient, result_item, 'minecraft:campfire_cooking',
                         experience, cooking_time, result_amount)


class Smelt(BaseCooking):

    def __init__(self, name: str, ingredient: Item, result_item: Item,
                 experience: float = 0.1, cooking_time: int = 200, result_amount: int = 1):
        super().__init__(name, ingredient, result_item, 'minecraft:smelting', experience, cooking_time, result_amount)


class Smoke(BaseCooking):

    def __init__(self, name: str, ingredient: Item, result_item: Item,
                 experience: float = 0.1, cooking_time: int = 200, result_amount: int = 1):
        super().__init__(name, ingredient, result_item, 'minecraft:smoking', experience, cooking_time, result_amount)
