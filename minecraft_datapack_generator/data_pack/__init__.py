import os
import sys
from typing import List

from data_pack_item import DataPackItem
from data_pack_item.function import Function
from data_pack_item.loot_table import LootTable
from data_pack_item.pack_mcmeta import PackMcmeta
from data_pack_item.recipe import Recipe


class DataPack:
    def __init__(self, name: str, description: str, minecraft_minor_version: str, items: List[DataPackItem]):
        self.name = name
        self.items = items
        self.items.append(PackMcmeta(description, minecraft_minor_version))

    def write(self):
        project_root = os.path.dirname(sys.modules['__main__'].__file__)
        base_path = os.path.join(project_root, 'target', self.name)
        for item in self.items:
            sub_path = 'data' if isinstance(item, (Function, LootTable, Recipe)) else ''
            path = os.path.join(base_path, sub_path, item.namespace, item.kind)
            os.makedirs(path, exist_ok=True)
            item.write(path)
