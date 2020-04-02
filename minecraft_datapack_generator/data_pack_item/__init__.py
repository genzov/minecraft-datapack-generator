import os
from abc import ABC, abstractmethod


class DataPackItem(ABC):
    def __init__(self, namespace: str, kind: str, name: str, extension: str):
        self.namespace = namespace
        self.kind = kind
        self.name = name
        self.extension = extension

    @abstractmethod
    def content(self):
        raise NotImplementedError()

    @abstractmethod
    def generate(self) -> str:
        raise NotImplementedError()

    def write(self, path: str):
        with open(os.path.join(path, f'{self.name}.{self.extension}'), 'w') as f:
            f.write(self.generate())
