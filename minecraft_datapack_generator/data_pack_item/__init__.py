import json
import os
from abc import ABC, abstractmethod
from json import JSONEncoder

from item import Item


class CustomEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, Item):
            return o.__str__()
        return json.JSONEncoder.default(self, o)


class DataPackItem(ABC):
    def __init__(self, namespace: str, kind: str, name: str, extension: str):
        self.namespace = namespace
        self.kind = kind
        self.name = name
        self.extension = extension

    @abstractmethod
    def content(self):
        raise NotImplementedError()

    # TODO: Make this variable as not all files will be JSON
    def generate(self) -> str:
        return json.dumps(self.content(), indent=4, sort_keys=True, cls=CustomEncoder)

    def write(self, path: str):
        with open(os.path.join(path, f'{self.name}.{self.extension}'), 'w') as f:
            f.write(self.generate())
