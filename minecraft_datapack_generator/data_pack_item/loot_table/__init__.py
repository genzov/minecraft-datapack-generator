import json
from typing import Union, List

from data_pack_item import DataPackItem
from data_pack_item.custom_encoder import CustomEncoder
from data_pack_item.loot_table.loot_table_pool import LootTablePool


class LootTable(DataPackItem):

    def __init__(self, name: str, pools: Union[LootTablePool, List[LootTablePool]], namespace: str = 'minecraft'):
        super().__init__(namespace, 'loot_tables', name, 'json')
        if isinstance(pools, List):
            self.pools = pools
        else:
            self.pools = [pools]

    def content(self):
        return {
            'pools': [p.content() for p in self.pools]
        }

    def generate(self) -> str:
        return json.dumps(self.content(), indent=4, sort_keys=True, cls=CustomEncoder)
