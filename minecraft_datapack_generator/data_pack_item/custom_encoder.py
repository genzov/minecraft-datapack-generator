import json
from json import JSONEncoder

from util.item import Item


class CustomEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, Item):
            return o.__str__()
        # elif isinstance(o, DataPackItem):
        #     return o.generate()
        return json.JSONEncoder.default(self, o)
