# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:

    def __init__(self, name, current_room, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def take_item(self, item):
        self.inventory.append(item)

    def drop_item(self, item):
        self.inventory.remove(item)
    
    def find_item(self, item_name: str):
        result = [item for item in self.inventory if item_name == item.name]
        return result[0] if len(result) > 0 else None

    


        
   # def __str__(self):
    #    return f'self.name = {self.name} \nself.current_room = {self.current_room}'



