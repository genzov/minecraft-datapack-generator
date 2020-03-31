import os
import sys
from typing import List

from data_pack_item import DataPackItem
from data_pack_item.pack_mcmeta import PackMcmeta


class DataPack:
    def __init__(self, name: str, description: str, minecraft_minor_version: str, items: List[DataPackItem]):
        self.name = name
        self.items = items
        self.items.append(PackMcmeta(description, minecraft_minor_version))

    def write(self):
        project_root = os.path.dirname(sys.modules['__main__'].__file__)
        base_path = os.path.join(project_root, 'target', self.name)
        for item in self.items:
            item.write(base_path)
