# Implement a class to hold room information. This should have name and
# description attributes.
from textwrap import fill
from item import Item


class Room:
    __SPACER: str = "   "

    def __init__(self, name: str, description: str, items: list = []):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.items_list = items

    def __str__(self):
        output = f"{self.name}\n{fill(self.description)}"

        if (len(self.items_list) > 0):
            items = "\n"
            items = items.join([self.__SPACER + str(item)
                                for item in self.items_list])
            output = output + f"\n\nItems:\n{items}"

        return output

    def __repr__(self):
        return f"Room: [name={self.name}, description={self.description}]"

    def find_item(self, item_name: str):
        result = [item for item in self.items_list if
                  item.name.lower() == item_name]
        return result[0] or None

    def add_item(self, item: Item):
        pass

    def remove_item(self, item: Item):
        self.items_list.remove(item)
        print(f"Removed {item.name}")
