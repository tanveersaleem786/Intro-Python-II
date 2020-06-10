from textwrap import fill


class Item:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Item: [name={self.name}, description={self.description}]"
