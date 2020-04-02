from abc import ABC

from data_pack_item import DataPackItem
from item import Item


class Recipe(DataPackItem, ABC):

    def __init__(self, namespace: str, name: str, output_item: Item, output_amount: int):
        super().__init__(namespace, 'recipes', name, 'json')
        self.output_item = output_item
        self.output_amount = output_amount
