# Implement a class to hold room information. This should have name and
# description attributes.
from textwrap import fill
from item import Item


class Room:
    __SPACER: str = "   "

    def __init__(self, name: str, description: str, items: list = None):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.items_list = items or []

    def __str__(self):
        output = f"{self.name}\n{fill(self.description)}"

        if (len(self.items_list) > 0):
            items = "\n"
            items = items.join([self.__SPACER + str(item)
                                for item in self.items_list])
            output = output + f"\n\nItems in view:\n{items}"

        return output

    def __repr__(self):
        return f"Room: [name={self.name}, description={self.description}]"

    def find_item(self, item_name: str):
        result = [item for item in self.items_list if item_name in item.alias_list]
        return result[0] if len(result) > 0 else None

    def add_item(self, item: Item):
        self.items_list.append(item)

    def remove_item(self, item_name: str):
        item = self.find_item(item_name)

        if item:
            self.items_list.remove(item)

        return item
