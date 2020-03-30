from typing import Dict

from data_pack_item import DataPackItem


class PackMcmeta(DataPackItem):

    def __init__(self, description: str, minecraft_minor_version: str):
        super().__init__('', 'pack.mcmeta')
        self.description = description
        self.pack_format = int(minecraft_minor_version.split('.')[-1][-1])

    def content(self) -> Dict:
        return {
            'pack': {
                'description': self.description,
                'pack_format': self.pack_format,
            }
        }
