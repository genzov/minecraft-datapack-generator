import json
import os
from abc import ABC, abstractmethod
from typing import Dict


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
        return json.dumps(self.content(), indent=4, sort_keys=True)

    def write(self, base_path: str):
        path = os.path.join(base_path, self.sub_path, self.category, f'{self.name}.{self.file_extension}')
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w') as f:
            f.write(self.generate())
