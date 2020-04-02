from abc import ABC, abstractmethod
from typing import Dict


class LootTableMeta(ABC):

    @abstractmethod
    def content(self) -> Dict:
        raise NotImplementedError()
