from abc import ABC

from data_pack_item import DataPackItem


class BaseRecipe(DataPackItem, ABC):

    def __init__(self, name: str, result_item: str, result_amount: int, group: str = None):
        super().__init__('recipe', name)
        self.group = group
        self.result_item = result_item
        self.result_amount = result_amount
