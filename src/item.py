from textwrap import fill


class Item:
    def __init__(self, alias_list: tuple, name: str, description: str):
        self.alias_list = alias_list
        self.name = name
        self.description = description

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Item: [alias_list={self.alias_list}, name={self.name}, description={self.description}]"

    def __eq__(self, other):
        if not(isinstance(other, (Item))):
            return False

        if other.alias_list != self.alias_list:
            return False

        if other.name != self.name:
            return False

        if other.description != self.description:
            return False

        return True

    def on_take(self):
        print(f"You pickup the {self.name}")

    def on_drop(self):
        print(f"You drop the {self.name}")
