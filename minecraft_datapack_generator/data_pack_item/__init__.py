import json
import os
from abc import ABC, abstractmethod
from json import JSONEncoder
from typing import Dict

from item import Item


class CustomEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, Item):
            return o.__str__()
        return json.JSONEncoder.default(self, o)


class DataPackItem(ABC):
    def __init__(self, category: str, name: str, sub_path: str = 'data/minecraft', file_extension: str = 'json'):
        self.category = category
        self.name = name
        self.file_extension = file_extension
        self.sub_path = sub_path

    @abstractmethod
    def content(self) -> Dict:
        raise NotImplementedError()

    def generate(self) -> str:
        return json.dumps(self.content(), indent=4, sort_keys=True, cls=CustomEncoder)

    def write(self, base_path: str):
        path = os.path.join(base_path, self.sub_path, self.category, f'{self.name}.{self.file_extension}')
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w') as f:
            f.write(self.generate())
