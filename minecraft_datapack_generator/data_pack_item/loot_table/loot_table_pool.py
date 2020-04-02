from typing import Union, List, Dict

from data_pack_item.loot_table.loot_table_condition import LootTableCondition
from data_pack_item.loot_table.loot_table_entry import LootTableEntry
from data_pack_item.loot_table.loot_table_meta import LootTableMeta


class LootTablePool(LootTableMeta):

    def __init__(self, entries: Union[LootTableEntry, List[LootTableEntry]],
                 conditions: Union[LootTableCondition, List[LootTableCondition]] = None, rolls: int = 1):
        self.rolls = rolls
        if isinstance(entries, List):
            self.entries = entries
        else:
            self.entries = [entries]

        if conditions is None:
            conditions = []
        if isinstance(conditions, List):
            self.functions = conditions
        else:
            self.functions = [conditions]

    def content(self) -> Dict:
        # TODO: include conditions
        return {
            'rolls': 1,
            'entries': [e.content() for e in self.entries]
        }
