from item import Item


class Inventory:
    __SPACER: str = "   "

    def __init__(self, items: list = None):
        self.items_list: list = items or []

    def __str__(self):
        items = ""

        if (len(self.items_list) > 0):
            items = "\n"
            items = items.join([self.__SPACER + str(item)
                                for item in self.items_list])

        return items

    def __repr__(self):
        return f"Inventory: [items_list={self.items_list}]"

    def __len__(self):
        return len(self.items_list)

    def search_items(self, item_name: str) -> Item:
        result = [item for item in self.items_list if item_name in item.alias_list]
        return result[0] if len(result) > 0 else None

    def remove_item(self, item_name: str) -> Item:
        item = self.search_items(item_name)

        if item:
            self.items_list.remove(item)

        return item

    def add_item(self, item: Item):
        self.items_list.append(item)
