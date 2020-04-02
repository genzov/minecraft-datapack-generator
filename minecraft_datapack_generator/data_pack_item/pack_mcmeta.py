import json

from data_pack_item import DataPackItem
from data_pack_item.custom_encoder import CustomEncoder


class PackMcmeta(DataPackItem):

    def __init__(self, description: str, minecraft_minor_version: str):
        super().__init__('', '', 'pack', 'mcmeta')
        self.description = description
        self.pack_format = int(minecraft_minor_version.split('.')[-1][-1])

    def content(self):
        return {
            'pack': {
                'description': self.description,
                'pack_format': self.pack_format,
            }
        }

    def generate(self) -> str:
        return json.dumps(self.content(), indent=4, sort_keys=True, cls=CustomEncoder)
