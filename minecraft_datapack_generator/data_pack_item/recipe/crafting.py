import string
from typing import Dict, List, Union

from data_pack_item.recipe import BaseRecipe
from item import Item


class Grid:

    def __init__(self, tl: Item = None, tm: Item = None, tr: Item = None, ml: Item = None, mm: Item = None,
                 mr: Item = None, bl: Item = None, bm: Item = None, br: Item = None):
        self.tl = tl
        self.tm = tm
        self.tr = tr
        self.ml = ml
        self.mm = mm
        self.mr = mr
        self.bl = bl
        self.bm = bm
        self.br = br
        self.br = br
        self.slots = [self.tl, self.tm, self.tr, self.ml, self.mm, self.mr, self.bl, self.bm, self.br]

    @staticmethod
    def _column_is_empty(rows, index):
        return all(row[index] == ' ' for row in rows)

    @staticmethod
    def _drop_column(rows, index):
        return [row[:index] + row[index+1:] for row in rows]

    @staticmethod
    def _row_is_empty(row):
        return all(True if slot == ' ' else False for slot in row)

    def get_keys(self) -> Dict[str, Item]:

        unique_items = list(set([s for s in self.slots if s is not None]))
        unique_keys = string.ascii_lowercase[0:len(unique_items)]

        merged = zip(unique_keys, unique_items)
        return {key: item for key, item in merged}

    def get_pattern(self) -> List[str]:

        # Invert dictionary to retrieve based on slot instead of key
        slot_keys = {v: k for k, v in self.get_keys().items()}

        pattern = []
        for slot in self.slots:
            key = slot_keys.get(slot)
            key = key if key is not None else ' '
            pattern.append(key)

        rows = [pattern[0:3], pattern[3:6], pattern[6:9]]

        # Remove empty columns
        # Start from the last column, otherwise the indexing gets messed up
        if self._column_is_empty(rows, 2):
            rows = self._drop_column(rows, 2)

        if self._column_is_empty(rows, 0):
            rows = self._drop_column(rows, 0)

        # Repeat index 0. If the previous index 0 was empty, it got dropped, in which case this run is the middle row.
        # This is important because otherwise this column might be dropped
        #   when the other two columns might have had a value, dropping the middle one would mess up the pattern.
        if self._column_is_empty(rows, 0):
            rows = self._drop_column(rows, 0)

        top_row = rows[0]
        middle_row = rows[1]
        bottom_row = rows[2]

        # Remove empty rows
        if self._row_is_empty(top_row):
            top_row = None

        if self._row_is_empty(bottom_row):
            bottom_row = None

        # Only drop the middle row if one of the previous rows were empty as well.
        # This is important for the same reason as with the columns, it might mess up the pattern otherwise.
        if self._row_is_empty(middle_row) and (top_row is None or bottom_row is None):
            middle_row = None

        # Join the arrays and filter out empty rows
        return [''.join(row) for row in (top_row, middle_row, bottom_row) if row is not None]


class CraftShape(BaseRecipe):

    def __init__(self, name: str, grid: Grid,
                 result_item: Item, result_amount: int = 1):
        super().__init__(name, result_item, result_amount)
        self.grid = grid

    def content(self) -> Dict:
        return {
            'type': 'minecraft:crafting_shaped',
            'pattern': self.grid.get_pattern(),
            'key': {k: {'item': v} for k, v in self.grid.get_keys().items()},
            'result': {
                'item': self.result_item,
                'count': self.result_amount
            },
        }


class CraftShapeless(BaseRecipe):

    def __init__(self, name: str, ingredients: List[Union[Item, List[Item]]],
                 result_item: Item, result_amount: int = 1):
        super().__init__(name, result_item, result_amount)
        self.ingredients = ingredients

    def transform_ingredients(self, ingredients):
        transformed = []
        for i in ingredients:
            if isinstance(i, Item):
                transformed.append({'item': i})
            elif isinstance(i, List):
                transformed.append(self.transform_ingredients(i))
        return transformed

    def content(self) -> Dict:
        return {
            "type": "minecraft:crafting_shapeless",
            "ingredients": self.transform_ingredients(self.ingredients),
            'result': {
                'item': self.result_item,
                'count': self.result_amount
            }
        }
