# Implement a class to hold room information. This should have name and
# description attributes.

class Room:

    def __init__(self, name, description, items=[]):
        
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = items
    
    def add_item(self, item):
        self.items.append(item)
    
    def remove_item(self, item):
        self.items.remove(item)

    def find_item(self, item_name: str):
        #result = [item for item in self.items if item_name in item.name]
        result = [item for item in self.items if item_name == item.name]
        return result[0] if len(result) > 0 else None