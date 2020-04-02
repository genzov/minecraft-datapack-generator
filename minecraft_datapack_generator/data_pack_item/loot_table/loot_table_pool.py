from typing import Union, List

from data_pack_item.loot_table.loot_table_entry import LootTableEntry
from data_pack_item.loot_table.loot_table_meta import LootTableMeta


class LootTablePool(LootTableMeta):

    def __init__(self, entries: Union[LootTableEntry, List[LootTableEntry]], rolls: int = 1):
        self.rolls = rolls
        if isinstance(entries, List):
            self.entries = entries
        else:
            self.entries = [entries]

    def content(self):
        return {
            'rolls': 1,
            'entries': [e.content() for e in self.entries]
        }
