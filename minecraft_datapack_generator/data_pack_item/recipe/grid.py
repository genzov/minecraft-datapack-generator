import string
from typing import Dict, List

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
    def column_is_empty(rows, index):
        return all(row[index] == ' ' for row in rows)

    @staticmethod
    def drop_column(rows, index):
        return [row[:index] + row[index+1:] for row in rows]

    @staticmethod
    def row_is_empty(row):
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
        if self.column_is_empty(rows, 2):
            rows = self.drop_column(rows, 2)

        if self.column_is_empty(rows, 0):
            rows = self.drop_column(rows, 0)

        # Repeat index 0. If the previous index 0 was empty, it got dropped, in which case this run is the middle row.
        # This is important because otherwise this column might be dropped
        #   when the other two columns might have had a value, dropping the middle one would mess up the pattern.
        if self.column_is_empty(rows, 0):
            rows = self.drop_column(rows, 0)

        top_row = rows[0]
        middle_row = rows[1]
        bottom_row = rows[2]

        # Remove empty rows
        if self.row_is_empty(top_row):
            top_row = None

        if self.row_is_empty(bottom_row):
            bottom_row = None

        # Only drop the middle row if one of the previous rows were empty as well.
        # This is important for the same reason as with the columns, it might mess up the pattern otherwise.
        if self.row_is_empty(middle_row) and (top_row is None or bottom_row is None):
            middle_row = None

        # Join the arrays and filter out empty rows
        return [''.join(row) for row in (top_row, middle_row, bottom_row) if row is not None]
