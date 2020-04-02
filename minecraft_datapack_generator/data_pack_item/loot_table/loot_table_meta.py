from abc import ABC, abstractmethod


class LootTableMeta(ABC):

    @abstractmethod
    def content(self):
        raise NotImplementedError()
