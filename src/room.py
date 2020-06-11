# Implement a class to hold room information. This should have name and
# description attributes.
from textwrap import fill
from inventory import Inventory
from item import Item


class Room:
    def __init__(self, name: str, description: str, *items):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.items_list: Inventory = Inventory(list(items))

    def __str__(self):
        output = f"{self.name}\n{fill(self.description)}"

        if len(self.items_list) > 0:
            output += f"\n\nItems in view:\n"
            output += str(self.items_list)

        return output

    def __repr__(self):
        return f"Room: [name={self.name}, description={self.description}, items_list={self.items_list}]"

    def add_item(self, item: Item):
        self.items_list.add_item(item)

    def remove_item(self, item_name: str):
        return self.items_list.remove_item(item_name)
