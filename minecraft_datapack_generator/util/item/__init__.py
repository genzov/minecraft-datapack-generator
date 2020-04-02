from typing import List

from util import Util


class Item(Util):

    def __add__(self, other):
        if isinstance(other, Item):
            return [self, other]
        elif isinstance(other, List):
            return [self] + other

    def __mul__(self, other):
        return [self] * other
