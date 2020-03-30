import json
from abc import ABC, abstractmethod
from typing import Dict


class DataPackItem(ABC):
    def __init__(self, kind: str, name: str):
        self.kind = kind
        self.name = name

    @abstractmethod
    def content(self) -> Dict:
        raise NotImplementedError()

    def generate(self) -> str:
        return json.dumps(self.content(), indent=4, sort_keys=True)

    def write(self, path: str):
        with open(path, 'w') as f:
            f.write(self.generate())
