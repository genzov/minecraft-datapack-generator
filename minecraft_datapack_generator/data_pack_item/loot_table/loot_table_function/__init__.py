from typing import Union, List

from data_pack_item.loot_table.loot_table_condition import LootTableCondition
from data_pack_item.loot_table.loot_table_meta import LootTableMeta


class LootTableFunction(LootTableMeta):

    def __init__(self, conditions: Union[LootTableCondition, List[LootTableCondition]] = None):
        if conditions is None:
            conditions = []
        if isinstance(conditions, List):
            self.conditions = conditions
        else:
            self.conditions = [conditions]

    def content(self):
        return {}
