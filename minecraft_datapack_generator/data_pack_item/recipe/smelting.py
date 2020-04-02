from abc import ABC

from data_pack_item.recipe import Recipe
from util.item import Item


class BaseCooking(Recipe, ABC):
    def __init__(self, namespace: str, name: str, input_item: Item, output_item: Item, cooking_type: str,
                 experience: float = 0.1, cooking_time: int = 200, output_amount: int = 1):
        super().__init__(namespace, name, output_item, output_amount)
        self.cooking_type = cooking_type
        self.input_item = input_item
        self.experience = experience
        self.cooking_time = cooking_time

    def content(self):
        return {
            'type': self.cooking_type,
            'ingredient': {
                'item': self.input_item
            },
            'result': self.output_item,
            'experience': self.experience,
            'cookingtime': self.cooking_time
        }


class Blast(BaseCooking):

    def __init__(self, name: str, input_item: Item, output_item: Item, experience: float = 0.1,
                 cooking_time: int = 200, output_amount: int = 1, namespace: str = 'minecraft'):
        super().__init__(namespace, name, input_item, output_item, 'minecraft:blasting',
                         experience, cooking_time, output_amount)


class Campfire(BaseCooking):

    def __init__(self, name: str, input_item: Item, output_item: Item, experience: float = 0.1,
                 cooking_time: int = 200, output_amount: int = 1, namespace: str = 'minecraft'):
        super().__init__(namespace, name, input_item, output_item, 'minecraft:campfire_cooking',
                         experience, cooking_time, output_amount)


class Smelt(BaseCooking):

    def __init__(self, name: str, input_item: Item, output_item: Item, experience: float = 0.1,
                 cooking_time: int = 200, output_amount: int = 1, namespace: str = 'minecraft'):
        super().__init__(namespace, name, input_item, output_item, 'minecraft:smelting',
                         experience, cooking_time, output_amount)


class Smoke(BaseCooking):

    def __init__(self, name: str, input_item: Item, output_item: Item, experience: float = 0.1,
                 cooking_time: int = 200, output_amount: int = 1, namespace: str = 'minecraft'):
        super().__init__(namespace, name, input_item, output_item, 'minecraft:smoking',
                         experience, cooking_time, output_amount)
