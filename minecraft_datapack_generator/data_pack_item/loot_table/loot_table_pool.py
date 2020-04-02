from typing import Union, List, Dict

from data_pack_item.loot_table.loot_table_entry import LootTableEntry


class LootTablePool:

    def __init__(self, entries: Union[LootTableEntry, List[LootTableEntry]], rolls: int = 1):
        self.rolls = rolls
        if isinstance(entries, List):
            self.entries = entries
        else:
            self.entries = [entries]

    def content(self) -> Dict:
        return {
            'rolls': 1,
            'entries': self.entries
        }
