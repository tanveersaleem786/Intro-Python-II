# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room
from item import Item


class Player:
    def __init__(self, current_room: Room):
        self.current_room: Room = current_room
        self.inventory: list = []

    def __str__(self):
        return str(self.current_room)

    def __repr__(self):
        return f"Player: [current_room={self.current_room}]"

    def move(self, *command):
        direction, obj_str = command

        move_to: dict = {
            "n": self.current_room.n_to,
            "north": self.current_room.n_to,
            "e": self.current_room.e_to,
            "east": self.current_room.e_to,
            "s": self.current_room.s_to,
            "south": self.current_room.s_to,
            "w": self.current_room.w_to,
            "west": self.current_room.w_to,
        }

        new_room = move_to[direction]
        if new_room:
            print(direction)
            self.current_room = new_room
        else:
            print("Sorry, you can't go in that direction")

    def search_inventory(self, item_name: str):
        result = [item for item in self.inventory if item_name in item.alias_list]
        return result[0] if len(result) > 0 else None

    def remove_item(self, item_name: str):
        item = self.search_inventory(item_name)

        if item:
            self.inventory.remove(item)

        return item

    def take(self, *command):
        cmd_str, item_name = command

        if not(item_name):
            print("Umm! You picked up nothing... Congratulations!")
            return

        item_from_room = self.current_room.remove_item(item_name)
        if item_from_room:
            self.inventory.append(item_from_room)
            item_from_room.on_take()
        else:
            print(f"There is no {item_name} here!")

    def drop(self, *command):
        cmd_str, item_name = command

        if not(item_name):
            print("Umm! You need to choose something to drop.")
            return

        item_dropped = self.remove_item(item_name)
        if item_dropped:
            self.current_room.add_item(item_dropped)
            item_dropped.on_drop()
        else:
            print(f"You don't have a {item_name}!")
