from typing import List


class Item:

    def __init__(self, name: str, namespace: str = 'minecraft'):
        self.name = name
        self.namespace = namespace

    def __str__(self):
        return f'{self.namespace}:{self.name}'

    def __add__(self, other):
        if isinstance(other, Item):
            return [self, other]
        elif isinstance(other, List):
            return [self] + other

    def __mul__(self, other):
        return [self] * other
