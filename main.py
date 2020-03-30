from data_pack import DataPack
from data_pack_item.recipe.shapeless import RecipeShapeless

if __name__ == "__main__":

    data_pack_items = [
        RecipeShapeless('backcraft_iron_bars', ['iron_bars'] * 3, 'iron_ingot'),
    ]

    DataPack('Baristo', 'Random utilities', '1.15', data_pack_items).write()
