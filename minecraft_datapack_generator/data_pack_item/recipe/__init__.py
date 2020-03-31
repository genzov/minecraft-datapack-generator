from abc import ABC

from data_pack_item import DataPackItem
from item import Item


class BaseRecipe(DataPackItem, ABC):

    def __init__(self, name: str, result_item: Item, result_amount: int, group: str = None):
        super().__init__('recipes', name)
        self.group = group
        self.result_item = result_item
        self.result_amount = result_amount
