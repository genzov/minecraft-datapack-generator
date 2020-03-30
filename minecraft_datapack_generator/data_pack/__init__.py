from typing import List

from data_pack_item import DataPackItem
from data_pack_item.pack_mcmeta import PackMcmeta


class DataPack:
    def __init__(self, name: str, description: str, minecraft_minor_version: str, items: List[DataPackItem]):
        self.name = name
        self.items = items
        self.items.append(PackMcmeta(description, minecraft_minor_version))
