from typing import Dict, Union, List

from data_pack_item import DataPackItem
from data_pack_item.loot_table.loot_table_pool import LootTablePool


class LootTable(DataPackItem):

    def __init__(self, name: str, pools: Union[LootTablePool, List[LootTablePool]], namespace: str = 'minecraft'):
        super().__init__(namespace, 'loot_tables', name, 'json')
        if isinstance(pools, List):
            self.pools = pools
        else:
            self.pools = [pools]

    def content(self) -> Dict:
        return {
            'pools': self.pools
        }
